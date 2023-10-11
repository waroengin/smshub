import os
import subprocess

grey = "\033[1;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[1;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"


print(f"""
{yellow}ID	Name{white}
rx	Sheerid
ef	Nextdoor
xb	RummyOla
wf	YandexGo
ahx	Bitrue
sg	OZON
et	Clubhouse
acv	A23
pm	AOL
kq	FotoCasa
fu	Snapchat
bp	GoFundMe
vd	Betfair
wv	AIS
ub	Uber
qd	Taobao
aeu	TheFork
abw	SOKOLOV
mq	GMNG
ev	Picpay
jm	Mzadqatar
aem	AstraPay
aij	NEQUI
bj	Вита экспресс
ds	Discord
zv	Digikala
po	Premium.one
ry	McDonalds
agy	Baihe
lo	OPPO
ajt	Город
oz	Poshmark
adb	PoshVine
uj	СhampionСasino
ako	Ryde
afu	ВсеИнструменты
ol	KazanExpress
mn	RRSA
iz	Global24
ax	CrefisaMais
od	FWDMAX
nr	Tosla
su	LOCO
pl	Perekrestok
mr	Fastmail
qs	МирЗнакомств
rz	EasyPay
xj	СберМаркет
abq	Upwork
tz	Лейка
wa	Whatsapp
rc	Skype
acw	YouDo
ye	ZaleyCash
akh	Prenagen Club
cw	PaddyPower
afj	SKCAPITAL
tw	Twitter
ha	My11Circle
kx	Vivo
ig	Instagram
nq	Trip
ahw	Zasilkovna
aep	ONBUKA
akf	Ollis
ct	КухняНаРайоне
ks	Hirect
au	Haraj
aej	Autoru
bx	Dosi
qc	Праймериз 2020
ts	PayPal
eu	LiveScore
aq	Glovo
nb	Верный
agv	DoneDeal
di	Loanflix
ww	BIP
acl	Tiv
aja	G2A
fq	Контур
aey	Next
mu	MyMusicTaste
ue	Onet
agw	Adverts
md	Банки
ahb	Ubisoft
ahf	Fugeelah
el	Bisu
le	E bike Gewinnspiel
bl	BIGO LIVE
ae	MyGLO
cs	AgriDevelop
adj	RummyCircle
gg	PagSmile
akz	Panvel
aag	Pockit
ck	BeReal
yw	Grindr
mt	Steam
adv	Cian
rt	Hily
ago	Servify
ai	CELEBe
gp	Ticketmaster
abo	WEBDE
rj	Детский мир
ic	JoGo
aap	Tiptapp
yu	Xiaomi
uh	Yubo
aga	Publi24
cb	Bazos
abl	Gpnbonus
sb	Lamoda
fz	KFC
adr	Boosty
vt	Budget4me
acs	Tata CLiQ Palette
acq	Suntec
afd	Astra Otoshop
tm	Akulaku
alj	Spotify
dv	NoBroker
zb	FreeNow
aed	Kamatera
alu	BC Game
agn	Flik
aco	AR Lens
sf	SneakersnStuff
adh	Frizza
agh	Anibis
aeh	Аптека Апрель
ahr	This Fate
tc	Rambler
bt	Alfa
dq	IceCasino
yl	Yalla
qr	MEGA
aec	JinJiang
ms	NovaPoshta
xf	LightChat
fx	PGbonus
agb	Smiles
fm	Touchance
az	CityBase
zk	Deliveroo
os	Dhani
aes	Золотое Яблоко
ald	Nice88
aw	Taikang
ajb	Бери заряд
gm	Mocospace
vm	OkCupid
jx	Swiggy
jr	Самокат
aaq	Netease
dz	Dominos Pizza
yx	JTExpress
uk	Airbnb
tu	Lyft
cu	炙热星河
sz	Pivko24
acf	Winter Loan
vw	CoinField
ly	Olacabs
dr	OpenAI
aat	TamTam
qm	RosaKhutor
akn	Chakra Rewards
eb	Voltz
ra	KeyPay
ahv	Surveybell
akk	Dagangan
lz	Things
tq	Swvl
ur	MyDailyCash
kv	Rush
ade	Magicpin
uy	Meliuz
nt	Sravni
ahd	OpenPhone
ajw	INDOBA
up	Magnolia
xe	GalaxyChat
er	Kwork
tg	Telegram
io	ЗдравСити
sx	Crowdtap
ain	SpaceWeb
gh	GyFTR
acu	CityMall
ud	Disney Hotstar
hm	Globus
ep	Temu
aby	Couponscom
rq	AptekiPlus
aim	Smartfren
sw	NCsoft
fg	IndianOil
gq	Freelancer
aau	RockeTreach
ajq	MyValue
ij	Revolut
adz	Шоколадница
aeg	Flowwow
du	AUBANK
si	Cita Previa
afh	Banrisul
zu	BigC
xx	Joyride
dh	EBay
fv	Vidio
og	Okko
nh	AlloBank
abp	D5BET
zg	Setel
aj	OneAset
agg	OneForma
nw	Ximalaya
lp	Algida
jh	PingPong
abg	PagBank
aar	Bearwww
ob	Onlinerby
agz	Jiva Petani
aip	AfreecaTV
alb	Guiche Web
kg	FreeChargeApp
kr	Eyecon
ou	Gabi
hn	1688
ach	Haleon
yp	Payzapp
mc	Michat
afq	MagaLu
bq	Adani
afi	Ame Digital
ace	Tata Neu
bb	LazyPay
ajg	Fortumo
we	DrugVokrug
alh	Lion Parcel
nk	Gittigidiyor
alr	Qunar
pj	Podeli
aee	Amway
xc	SynotTip
am	Amazon
kj	YAPPY
gw	CallApp
np	Siply
abr	Privy
qt	MoneyСontrol
yz	Около
lb	Mailru Group
px	Nifty
sq	KuCoinPlay
pw	SellMonitor
il	IQOS
gv	Humta
afp	VFS GLOBAL
zf	OnTaxi
tk	МВидео
rd	Lenta
hy	Ininal
ahl	Maxim
um	Belwest
td	ChaingeFinance
akd	Feels
vq	LadyMaria
kb	Kufarby
rp	Hamrahaval
abe	Foodora
sn	OLX
ld	Cashmine
ew	Nike
acd	CheckDomain
abs	Playerzpot
wt	IZI
ajd	Bankera
akl	DOKU
pd	IFood
ahk	БлинБери
zl	Airtel
aiv	Striving in the Lion City
aje	CupidMedia
ym	Youla.ru
te	EFood
ki	99app
fe	CliQQ
hw	Alipay/Alibaba
ao	UU163
ys	ZCity
ng	FunPay
sy	Brahma
sm	YoWin
aek	EnerGO
ajz	MotionPay
ot	Any other
sa	AGIBANK
hg	Switips
zp	Pinduoduo
jw	Br777
xl	Wmaraci
ko	AdaKami
qh	Oriflame
agx	MeiQFashion
ca	SuperS
zx	CommunityGaming
iu	Bykea
go	Google,youtube,Gmail
iv	Inboxlv
gb	YouStar
xr	Tango
hf	Cleartrip
agu	Marlboro
ahn	Рив Гош
lm	FarPost
aif	Royal Canin
abx	Kaching
ir	Chispa
uf	Eneba
abf	Mercado Pago
xv	Wish
aks	Hanya
akg	Book My Play
iw	MyLavash
ady	ТОКИО-CITY
rs	Lotus
ss	Hezzl
op	MIRATORG
ip	Burger King
alt	Segari
oc	DealShare
qp	Максавит
afy	Tuul
akm	LOTTE Mart
akr	Voi
aiw	СушиВёсла
fa	XadrezFeliz
ahh	Cumbuca
cv	WashXpress
xy	Depop
afg	Zenvia
no	Virgo
wr	Walmart
ni	Gojek
qj	Whoosh
vr	MotorkuX
agl	Betano
mz	Zolushka
ju	Indomaret
jq	Paysafecard
adc	PlayOJO
aha	Angel One
jd	GiraBank
abd	BeeBoo
aiy	Nloto
ps	Zdorov
afl	Vsesmart
ajy	All Access
dl	Lazada
kz	NimoTV
gu	Fora
ux	Домовой
jp	Rbt
bn	Alfagift
ua	BlaBlaCar
kh	Bukalapak
alq	Etsy
be	СберМегаМаркет
afo	KION
cm	Prom
ce	Mosru
kw	Foody
adq	Uzum
vl	Ортека
afk	Chevron
my	CAIXA
ji	Monobank
ais	Schibsted
oi	Tinder
aew	Flip
hr	JKF
zt	Budweiser
cz	Getmega
ht	Bitso
ul	Getir
wg	Skout
gr	Astropay
zs	Bilibili
hc	MOMO
cf	Irancell
ku	RoyalWin
aca	Sunlight
ll	888casino
lh	24betting
ky	SpatenOktoberfest
aeb	GoPayz
bu	MonobankIndia
ya	Yandex
jc	IVI
aaa	Nubank
sc	Voggt
lq	Potato
rm	Faberlic
zm	OfferUp
ex	Linode
afb	Maybank
zi	LoveLocal
kd	Author24
lr	Okta
aer	PlayerAuctions
nv	Naver
acg	CollabAct
aeo	Allofresh
mh	Ашан
yr	Miravia
ea	JamesDelivery
aba	Rappi
afr	Ultragaz
bz	Blizzard
vo	Brand20ua
xp	MonetaRu
lg	MediBuddy
xt	Flipkart
ael	Cloud Manager
hk	4Fun
yh	Hh
ty	Окей
abh	Vulkan Vegas
wk	Mobile01
ajv	ShareParty
age	MTR Mobile
aay	JioMart
qa	MyFishka
vn	Yaay
ln	Grofers
ma	Mail.ru
qz	Faceit
cr	TenChat
iy	FoodHub
acz	Claude
bi	勇仕网络Ys4fun
vh	Штолле
rv	Kotak811
ads	GoChat
fs	Şikayet var
bv	Metro
alk	Singcity
xg	FortunaSK
gx	Hepsiburadacom
xz	Paycell
ka	Shopee
va	SportGully
ac	DoorDash
vs	WinzoGame
lt	BitClout
qo	Moneylion
lv	Megogo
je	Nanovest
cn	Fiverr
qi	23red
db	Ezbuy
tp	IndiaGold
aeq	Godrej
pb	SkyTV
eg	ContactSys
rw	BLS-SPAIN
alc	Facily
yj	EWallet
vp	Kwai
la	Ssoidnet
aex	Neon
dt	Delivery Club
pz	Lidl
lf	TikTok/Douyin
ajj	Rebtel
ei	Taksheel
at	Perfluence
tf	Noon
aht	MockGuru
jb	Wing Money
aln	Remotasks
ahq	SEEDS
ve	Dream11
im	Imo
ho	Cathay
li	Baidu
acc	LuckyLand Slots
aix	Move It
ajn	Gopuff
akb	Gurmanika
ze	Shpock
ut	Энергобум
qk	Bit
aii	Hinge Dating
ajh	WAUG
aka	LinkAja
hj	Stoloto
lx	DewuPoison
ri	BillMill
kk	Idealista
xs	GroupMe
kp	HQ Trivia
js	GolosZa
als	Greggs
acp	BonusLink
aio	Prakerja
nn	Giftcloud
aid	Kia
fl	RummyLoot
ff	AVON
wj	1хbet
yk	СпортМастер
cx	Icrypex
za	JDcom
sj	HandyPick
ox	Damejidlo
aaw	Aya Bank
abn	Namars
dw	Divar
ala	GetResponse
do	Leboncoin
ro	PingCode
ow	RegRu
agr	Yonogames
yy	Venmo
acy	Airtime
fb	Facebook
bo	Wise
ey	Miloan
aky	GOMOFY
br	Вкусно и Точка
adw	Профи
bf	Keybase
bh	Uteka
ee	Twilio
sr	Starbucks
adp	Cabify
dy	Zomato
acm	Razer
vb	Кораблик
un	Humblebundle
alg	Ankama
aiu	GetNinjas
xd	Tokopedia
kf	Weibo
ali	StockyDodo
rl	InDriver
zz	Dent
wx	Apple
aih	Fups
alm	Muzz
hz	Drom
ajm	Gener8
mk	LongHu
pp	Huya
ge	Paytm
kn	Verse
agq	Bajaj Finserv
fh	Lalamove
afx	Gamesofa
wd	CasinoPlus
agt	Uralairlines
se	Feeld
it	CashApp
xo	Notifire
yg	CourseHero
oj	LoveRu
nu	Stripe
aji	МИГРАНТ СЕРВИС
fr	Dana
afm	Myboost
tt	Ziglu
xh	OVO
km	Rozetka
ajs	GetPlus
eh	Telegram 2.0
aef	Велобайк
ql	CMTcuzdan
tj	DbrUA
qq	Tencent QQ
iq	Icq
rb	Tick
yn	Allegro
mb	Yahoo
yo	Amasia
aas	XXGame
cl	UWIN
fo	MobiKwik
pc	Casino/bet/gambling
fk	BLIBLI
akj	Easycash
wy	Yami
ch	Pocket52
zd	Zilch
adi	Zepto
af	GalaxyWin
jl	Hopi
kc	Vinted
dg	Mercari
mx	SoulApp
wu	PrivetMir
adt	Willhaben
akt	Xworldwallet
ahi	Daki
ajx	Kemnaker RI
uu	Wildberries
nl	Myntra
ik	GuruBets
agd	Grailed
bc	GCash
vf	Q12 Trivia
ajf	IPanelOnline
wm	SMO71
aax	Boyaa
zq	IndiaPlays
da	MTS CashBack
ahe	Bunq
gc	TradingView
aik	ZUS Coffee
oo	LigaPro
abu	BPJSTK
akc	Paybis
tn	LinkedIN
ar	Wondermart
agf	Meitu
pq	CDkeys
eo	Sizeer
wn	GameArena
sl	СберАптека
hl	Band
rf	Akudo
ags	Abbott
hx	AliExpress
abj	Trembet
ack	Tomato
aen	Redigame
wz	FoxFord
ia	Socios
mo	Bumble
mw	Transfergo
gs	SamsungShop
ti	Cryptocom
jn	CloudBet
adg	Marwadi
bm	MarketGuru
bs	TradeUP
aei	Tanoti
aev	BankKaro
cq	Mercado
qw	Qiwi
cj	Dotz
re	Coinbase
nc	Payoneer
lc	Subito
gl	GlobalTel
of	Urent/jet/RuSharing
lj	Santander
adl	EarnEasy
aea	Taptap Send
xw	Taki
gk	AptekaRU
hs	Asda
aet	Greywoods
nz	Foodpanda
eq	Qoo10
sk	Skroutz
mf	Weidian
agc	VIMpay
alp	Mera Gaon
qx	WorldRemit
gz	LYKA
bw	Signal
bd	X5ID
cd	SpotHit
aaz	Ozan
dd	CloudChat
uv	BinBin
py	Monese
yb	Система Город
ej	MrQ
ta	Wink
dp	ProtonMail
ft	Букмекерские
sh	Vkusvill
rk	Fotka
ja	Weverse
jt	TurkiyePetrolleri
xa	УлыбкаРадуги
tl	Truecaller
abc	Taptap Send
agk	Ipsos iSay
hi	JungleeRummy
acr	QwikCilver
hb	Twitch
ab	Alibaba
aie	Фотострана
vk	Vk.com
ne	Coindcx
act	Maxis
mj	Zalo
afc	Bunda
yv	IPLwin
aiq	Prime Opinion
jv	Consultant
aez	Shein
dm	Iwplay
hh	Uplay
gt	Gett
pt	Bitaqaty
ajk	Venteny
air	TipTip
adu	Seznam
lk	PurePlatfrom
pf	Pof.com
an	Adidas
qg	MoneyPay
ml	ApostaGanha
abv	Халва
pv	Koshelek
ale	Lydia
acj	Meituan
hu	Ukrnet
ait	FeetFinder
adf	BCA Syariah
ahz	Кузбасс Онлайн
xq	MPL
jg	Grab
qu	Agroinform
zy	Nttgame
wl	YouGotaGift
acx	Beboo
afa	CDEK
aft	Neocrypto
abz	Friendtech
abt	ArenaPlus
mg	Magnit
ajo	CoffeeTea
aiz	Brevo
uo	CafeBazaar
fi	Dundle
fd	Mamba
ajc	Почта России
ak	Douyu
wo	Parkplus
ov	Beget
ad	Iti
dc	YikYak
zh	Zoho
co	Rediffmail
vg	ShellBox
pn	CoffeeLike
ws	Indodax
kt	KakaoTalk
ail	Zoo Game
qb	Payberry
aab	BharatPe
abb	Coca-Cola
akq	Blank Street
ay	Ruten
qn	Blued
abi	BytePlus
rh	Ace2Three
en	Hermes
afv	Джилекс
mm	Microsoft
pa	Gamekit
afn	Roomster
gi	Hotline
abm	Утконос
qe	GG
bg	MIXMART
ny	Pyro Music
lu	Crickpe
tv	Flink
pr	Trendyol
aa	Probo
bk	G2G
so	RummyWealth
ajl	Av100pro
aho	UangMe
ahg	Credcesta
ec	RummyCulture
zj	ROBINHOOD
ph	SnappFood
adx	BusyFly
akp	Her
rn	Neftm
us	IRCTC
dk	Pairs
ih	TeenPattiStarpro
akw	WINDS
uq	TopDetal
aav	Alchemy
acn	Radium
fy	Mylove
agp	Hdfcbank
akx	Sony LIV
afe	GovBr
wp	163СOM
ahj	Strato
yd	米画师Mihuashi
xi	InFund
ke	Эльдорадо
uw	Kirana
vz	Hinge
jz	Kaya
rg	Porbet
jj	Aitu
sv	Dostavista
aki	Tiketcom
gd	Surveytime
es	IQIYI
ahy	Fliff
fc	PharmEasy
oh	MapleSEA
zo	Kaggle
lw	MrGreen
acb	Spark Driver
hp	Meesho
ga	Roposo
agi	Njuškalo
qy	Zhihu
xn	Familia
vv	Seosprint
zw	Quack
jo	SticPay
adk	Khatabook
qv	Badoo
ah	EscapeFromTarkov
dj	LUKOIL-AZS
ru	HOP
hq	Magicbricks
yf	Citymobil
nj	FreshKarta
oe	Codashop
afw	Packeta
ahm	BRO
aig	K11
cg	Gemgala
ix	Celcoin
cy	РСА
uc	Tatneft
ahs	1and1
wq	Leboncoin1
afz	Klarna
fj	Potato Chat
abk	GMX
ada	TRUTH SOCIAL
agm	CMB
gy	MIYACHAT
th	WestStein
kl	Kolesa.kz
uz	OffGamers
ake	DIKIDI
wb	WeChat
ls	Careem
vj	Stormgain
tx	Bolt
gf	GoogleVoice
fp	Phound
aci	BPJS
adn	Zach Bryan
oq	Vlife
xm	Лэтуаль
ok	Ok.ru
ed	Gamer
tr	Paysend
qf	RedBook
alo	Profee
wh	TanTan
ado	SmartyPig
vc	Banqi
ns	Oldubil
vi	Viber
gn	A9A
ez	GoerliFaucet
rr	Wolt
cc	Quipp
ajp	AsiaMiles
sd	Dodopizza
nf	Netflix
afs	Privalia
em	ZéDelivery
alf	WEBULL
yq	Фокстрот
dn	Paxful
dx	Powerkredite
av	Avito
xu	RecargaPay
ahp	PizzaHut
oy	CashFly
mp	Winmasters
de	Karusel
aic	Ozan SuperApp
wc	Craigslist
gj	Carousell
ajr	Boku
agj	Marktplaats
ba	Expressmoney
st	Auchan
mv	Fruitz
he	Mewt
pu	Justdating
om	Corona
df	Happn
adm	FitCredit
zr	Papara
fw	99acres
ug	Fiqsy
jy	Sorare
aju	Daya Auto
vx	HeyBox
ii	CashKaro
vy	Meta
hd	MarketPapa
aff	C6 Bank
cp	Uklon
xk	DiDi
ib	Immowelt
yi	Yemeksepeti
nm	Thisshop
mi	Zupee
pg	NRJ Music Awards
ci	RedBus
zn	Biedronka
ui	RuTube
me	Line msg
jf	Likee
sp	HappyFresh
ie	Bet365""")

def buka_file_main():
    file_path = 'main.py'  # Ganti dengan path file main.py jika perlu
    if os.path.exists(file_path):
        # Bersihkan layar sebelum menjalankan perintah
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        
        # Jalankan file main.py
        subprocess.run(f'python {file_path}', shell=True)
    else:
        print(f"File {file_path} tidak ditemukan")

if __name__ == '__main__':
    print("Tekan Enter untuk kembali ke Menu")
    input()  # Menunggu sampai Enter ditekan
    buka_file_main()
