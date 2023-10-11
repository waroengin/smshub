import os
import requests
from datetime import datetime
import subprocess

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_console()

def input_nama_dan_api_key():
    nama = input("Masukkan Nama Anda: ")
    api_key = input("Masukkan API Key Anda: ")

    with open("nama.txt", "w") as nama_file:
        nama_file.write(nama)

    with open("key.txt", "w") as key_file:
        key_file.write(api_key)

def get_ip_address():
    # Ganti dengan logika untuk mendapatkan alamat IP pengguna
    return "192.168.0.1"

def get_sms_hub_info(api_key):
    url = f"https://smshub.org/stubs/handler_api.php?api_key={api_key}&action=getBalance"
    response = requests.get(url)
    if response.status_code == 200:
        info = response.text
        info = info.replace("ACCESS_BALANCE:", "")  # Menghapus "ACCESS_BALANCE:"
        return info
    else:
        return "Gagal mendapatkan informasi SMSHub."
    
def buka_file_list_py():
    try:
        subprocess.run(["python", "list.py"])
    except Exception as e:
        print(f"Error: {e}")

def buka_file_services_py():
    try:
        subprocess.run(["python", "services.py"])
    except Exception as e:
        print(f"Error: {e}")

def buka_file_gmail_py():
    try:
        subprocess.run(["python", "gmail.py"])
    except Exception as e:
        print(f"Error: {e}")

def buka_file_spo_py():
    try:
        subprocess.run(["python", "spo.py"])
    except Exception as e:
        print(f"Error: {e}")

def tampilkan_dashboard():
    with open("nama.txt", "r") as nama_file:
        nama = nama_file.read()

    api_key = ""
    with open("key.txt", "r") as key_file:
        api_key = key_file.read()

    ip_address = get_ip_address()
    tanggal_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sms_hub_info = get_sms_hub_info(api_key)

    grey = "\033[1;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[1;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    white = "\033[0;37m"

    print(f"Selamat datang, {yellow}{nama}!{white}")
    print(f"IP Address   : {ip_address}")
    print(f"Tanggal      : {tanggal_sekarang}")
    print(f"{yellow}SMSHub Balance {sms_hub_info} Rub{white}")

    print("\nMenu:")
    print("1. List Country ID")
    print("2. List Services ID")
    print("3. List Harga Services")
    print("4. SMSHub OTP | Gmail ID")
    print("5. SMSHub OTP | Spotify CHL")
    print("6. Lainnya")
    print("0. Keluar")

    while True:
        pilihan = input("Pilih opsi (0-6): ")

        if pilihan == "1":
            buka_file_list_py()
            pass
        elif pilihan == "2":
            buka_file_services_py()
            pass
        elif pilihan == "3":
            buka_file_list_py()
            pass
        elif pilihan == "4":
            buka_file_gmail_py()
            pass
        elif pilihan == "5":
            buka_file_spo_py()
            pass
        elif pilihan == "6":
            # buka_file_custom_py()
            pass
        elif pilihan == "0":
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

if __name__ == "__main__":
    if not os.path.exists("nama.txt") or not os.path.exists("key.txt"):
        input_nama_dan_api_key()

    tampilkan_dashboard()
