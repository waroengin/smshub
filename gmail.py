import requests
import threading
import colorama
from colorama import Fore, Style
from colorama import init
init(autoreset=True)

with open("key.txt", "r") as key_file:
    api_key = key_file.read().strip()

service_id = 'go'
country_code = '6'
operator = 'ANY'
running = True
previous_status = ""

def get_phone_number(api_key, service_id, country_code, operator):
    number_url = f'https://smshub.org/stubs/handler_api.php?action=getNumber&api_key={api_key}&service={service_id}&country={country_code}&operator={operator}&forward=0'
    response = requests.get(number_url)
    number_info = response.text.strip()
    
    if ':' in number_info:
        number_id = number_info.split(':')[1]
        number = number_info.split(':')[2]
        return number_id, number
    else:
        print(f'Error: Respons tidak memiliki format yang benar: {number_info}')
        return None, None

def check_number_status(api_key, number_id):
    status_url = f'https://smshub.org/stubs/handler_api.php?api_key={api_key}&action=getStatus&id={number_id}'
    response = requests.get(status_url)
    status = response.text.strip()
    return status

def check_balance(api_key):
    balance_url = f'https://smshub.org/stubs/handler_api.php?api_key={api_key}&action=getBalance'
    response = requests.get(balance_url)
    if response.status_code == 200:
        try:
            balance_data = response.text.strip().split(':')
            if len(balance_data) == 2 and balance_data[0] == 'ACCESS_BALANCE':
                balance = float(balance_data[1])
                return balance
            else:
                print(f'Error: Respons tidak valid. Data saldo tidak ditemukan.')
                return None
        except ValueError:
            print(f'Error: Gagal mendapatkan saldo. Respons tidak valid.')
            return None
    else:
        print(f'Error: Gagal mendapatkan saldo. Kode status: {response.status_code}')
        return None
    
grey = "\033[1;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[1;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"

rub_to_idr_exchange_rate = 156

balance_rub = check_balance(api_key)

if balance_rub is not None:
    balance_idr = balance_rub * rub_to_idr_exchange_rate

def main_loop():
    global running
    global previous_status
    print(Style.BRIGHT + '\n-------------------------------')
    print(Style.BRIGHT + '\nSMSHub OTP | Gmail IDR')
    balance = check_balance(api_key)
    if balance is not None:
        print(f"\nSaldo SMSHub: {yellow}{balance} Rub | Rp.{balance_idr}")
        print(Fore.LIGHTBLACK_EX + "[TEKAN ENTER / CTRL+C UNTUK EXIT]\n")
        
        country_mapping = {
    '6': 'Indonesia',
    '151': 'Chille',
}
        country_name = country_mapping.get(country_code, 'Unknown')
    running = True
    while running:
        number_id, number = get_phone_number(api_key, service_id, country_code, operator)
        if number_id and number:
            print(f'Country  : {country_name}')
            print(f'Operator : {operator}')
            print(f'Services : {service_id}')
            print(f'Nomor HP : {yellow}{number}')
            while running:
                inbox_url = f'https://smshub.org/stubs/handler_api.php?action=getInbox&api_key={api_key}&id={number_id}'
                inbox_response = requests.get(inbox_url)
                
                if inbox_response.status_code == 200:
                    try:
                        inbox_data = inbox_response.json()
                        for message in inbox_data:
                            print(f'Pesan masuk: {message["text"]}')
                    except ValueError:
                        None
                status = check_number_status(api_key, number_id)
                
                status_parts = status.split(':')
                if len(status_parts) > 1:
                    status = status_parts[0]
                    status_detail = status_parts[1]
                    print(f'OTP      : {green}{status_detail}')
                
                if status == 'STATUS_OK':
                    resend_url = f'https://smshub.org/stubs/handler_api.php?api_key={api_key}&action=setStatus&status=3&id={number_id}'
                    response = requests.get(resend_url)
                    if response.status_code == 200:
                        print(f"OTP      : {yellow}SUCCES_RESEND")
                    else:
                        print(f'FAILED. {response.status_code}')
                
                if status == 'STATUS_CANCEL':
                    print(f'OTP      : {red}CANCELED')
                    running = False
                    break 
                elif status != previous_status:
                    print(f'OTP      : {status}')
                    previous_status = status

main_thread = threading.Thread(target=main_loop)
main_thread.start()

input('')
running = False
main_thread.join()
