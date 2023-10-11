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
{yellow}ID	Name	Countries	Available Operators{white}
0	Russia	russia	aiva,any,beeline,center2m,danycom,ezmobile,gazprombank_mobile,lycamobile,matrix,mcn,megafon,motiv,mts,mtt,mtt_virtual,rostelecom,sber,simsim,tele2,tinkoff,ttk,vtb_mobile,winmobile,yota
1	Ukraine	ukraine	3mob,any,intertelecom,kyivstar,life,lycamobile,mts,utel,vodafone
2	Kazakhstan	kazakhstan	activ,altel,any,beeline,forte_mobile,kcell,tele2
3	China	china	any,chinamobile,china_unicom,unicom
4	Philippines	philippines	any,globe_telecom,smart,tm
5	Myanmar	myanmar	any,mpt,mytel,ooredoo,telenor
6	Indonesia	indonesia	any,axis,indosat,smartfren,telkomsel,three
7	Malaysia	malaysia	any,celcom,digi,hotlink,tune_talk,u_mobile,xox,yes
8	Kenya	kenya	airtel,any,econet,orange,safaricom,telkom
9	Tanzania	tanzania	airtel,any,halotel,tigo,ttcl,vodacom
10	Vietnam	vietnam	any,itelecom,mobifone,vietnamobile,viettel,vinaphone,wintel
11	Kyrgyzstan	kyrgyzstan	any,beeline,megacom,o!
12	Usa	usa	any,cellular,tmobile
13	Israel	israel	019mobile,any,golan_telecom,home_cellular,hot_mobile,jawwal,ooredoo,orange,pelephone,rami_levy
14	Hongkong	hongkong	any,chinamobile,csl_mobile,imc,smartone,three,unicom
15	Poland	poland	a2_mobile,aero2,any,e_telko,heyah,klucz,lycamobile,netia,nju,orange,play,plus,tmobile
16	England	england	any,cmlink,ee,ezmobile,giffgaff,lebara,lycamobile,o2,orange,talk_telecom,teleena,three,tmobile,vectone,vodafone
17	Madagascar	madagascar	any
18	Dcongo	dcongo	africel,airtel,any,orange,vodacom
19	Nigeria	nigeria	airtel,any,etisalat,glomobile,mtn
20	Macao	macao	3macao,any
21	Egypt	egypt	any,etisalat,orange,vodafone
22	India	india	any
23	Ireland	ireland	48mobile,any,cablenet,lycamobile,tesco
24	Cambodia	cambodia	any,metfone
25	Laos	laos	any,etl,telekom,tplus,unitel
26	Haiti	haiti	any,natcom
27	Ivory	ivory	any,moov,mtn,orange
28	Gambia	gambia	africel,any,comium,gamcel,qcell
29	Serbia	serbia	a1,any,mobtel,mts,vip
30	Yemen	yemen	any,mtn,sabafon,yemen_mobile
31	Southafrica	southafrica	any,cell_c,lycamobile,mtn,telkom,vodacom
32	Romania	romania	any,benefito_mobile,digi,lycamobile,my_avon,orange,runex_telecom,telekom,vodafone
33	Colombia	colombia	any,claro,movistar,tigo,virgin,wom
34	Estonia	estonia	any,elisa,goodline,super,tele2,topconnect
35	Azerbaijan	azerbaijan	any,azerfon,humans
36	Canada	canada	any,cellular,chatrmobile,fido,lucky,rogers,telus
37	Morocco	morocco	any,iam,inwi,itissalat,orange
38	Ghana	ghana	airtel,any,glomobile,millicom,mtn,vodafone
39	Argentina	argentina	any,claro,movistar,personal,tuenti
40	Uzbekistan	uzbekistan	any,beeline,humans,mobiuz,mts,ucell,uzmobile
41	Cameroon	cameroon	any,mtn,nexttel,orange
42	Chad	chad	airtel,any,salam,tigo
43	Germany	germany	any,fonic,lebara,lycamobile,o2,ortel_mobile,telekom,vodafone
44	Lithuania	lithuania	any,bite,tele2,telia
45	Croatia	croatia	a1,any,tele2,telemach,tmobile,tomato
46	Sweden	sweden	any,comviq,lycamobile,tele2,telenor,telia,three,vectone,vodafone
47	Iraq	iraq	any,asiacell,korek,zain
48	Netherlands	netherlands	any,kpn,lebara,lycamobile,l_mobi,tmobile,vodafone
49	Latvia	latvia	any,bite,lmt,tele2,xomobile
50	Austria	austria	a1,any,eety,hot_mobile,lidl,lycamobile,orange,telering,three,tmobile,yesss
51	Belarus	belarus	any,best,life,mdc,mts
52	Thailand	thailand	ais,any,dtac,truemove
53	Saudiarabia	saudiarabia	any
54	Mexico	mexico	any,telcel
55	Taiwan	taiwan	any,chunghwa,fareast
56	Spain	spain	altecom,any,euskaltel,lebara,llamaya,lycamobile,movistar,orange,tmobile,vodafone,yoigo,you_mobile
57	Iran	iran	any,aptel,azartel,hamrah_e_aval,irancell,mtn,rightel,samantel,shatel,taliya,tci
58	Algeria	algeria	any,djezzy,mobilis,ooredoo
59	Slovenia	slovenia	a1,any,telekom,telemach
60	Bangladesh	bangladesh	any
61	Senegal	senegal	any,expresso,free,orange
62	Turkey	turkey	any,turkcell,turk_telekom,vodafone
63	Czech	czech	any,kaktus,o2,tmobile,vodafone
64	Srilanka	srilanka	airtel,any,dialog,etisalat,hutch,sltmobitel
65	Peru	peru	any,movistar
66	Pakistan	pakistan	any,jazz,ptcl,sco,telenor,ufone,zong
67	Newzealand	newzealand	2degree,any,one_nz,skinny,vodafone,warehouse
68	Guinea	guinea	any,cellcom,mtn,orange,sotelgui,telecel
69	Mali	mali	any,malitel,orange,telecel
70	Venezuela	venezuela	any
71	Ethiopia	ethiopia	any,mtn
72	Mongolia	mongolia	any,beeline
73	Brazil	brazil	algartelecom,any,claro,correios_celular,nlt,oi,tim,vivo
74	Afghanistan	afghanistan	any,salaam
75	Uganda	uganda	airtel,any,k2_telecom,lycamobile,mtn,orange,smart,smile,uganda_telecom
76	Angola	angola	africel,any,unitel
77	Cyprus	cyprus	any,cablenet,cyta,epic,lemontel,primetel,vectone
78	France	france	any,bouygues,free,lebara,lycamobile,orange,sfr,syma_mobile,vectone
79	Papua	papua	any
80	Mozambique	mozambique	any
81	Nepal	nepal	any
82	Belgium	belgium	any,bandwidth,base,infrabel,lycamobile,nethys,orange,proximus,vectone
83	Bulgaria	bulgaria	a1,any,telenor,vivacom,yettel
84	Hungary	hungary	any,tmobile,vodafone,yettel
85	Moldova	moldova	any,idc,moldcell,orange,unite
86	Italy	italy	any,digi,ho,kena_mobile,lycamobile,optima,tim,vodafone,wind
87	Paraguay	paraguay	any,claro,personal
88	Honduras	honduras	any,claro
89	Tunisia	tunisia	any,ooredoo,orange,tunicell
90	Nicaragua	nicaragua	any,movistar
91	Timorleste	timorleste	any,telemor,telkomcel,timor_telecom
92	Bolivia	bolivia	any
93	Costarica	costarica	any
94	Guatemala	guatemala	any,claro,movistar,tigo
95	Uae	uae	any
96	Zimbabwe	zimbabwe	any,econet
97	Puertorico	puertorico	any
98	Sudan	sudan	any,mtn,sudani_one,zain
99	Togo	togo	any
100	Kuwait	kuwait	any
101	Salvador	salvador	any,claro,digi,movistar,red,tigo
102	Libyan	libyan	any
103	Jamaica	jamaica	any,digi
104	Trinidad	trinidad	any
105	Ecuador	ecuador	any,claro,cnt_mobile,movistar,tuenti
106	Swaziland	swaziland	any
107	Oman	oman	any
108	Bosnia	bosnia	a1,any,hej
109	Dominican	dominican	altice,any,claro,viva
110	Syrian	syrian	any
111	Qatar	qatar	any
112	Panama	panama	any
113	Cuba	cuba	any,cubacel
114	Mauritania	mauritania	any,chinguitel,mattel,mauritel
115	Sierraleone	sierraleone	africel,airtel,any,qcell
116	Jordan	jordan	any,orange,umniah,xpress,zain
117	Portugal	portugal	any,lebara,lycamobile,nos,vodafone
118	Barbados	barbados	any
119	Burundi	burundi	africel,any,econet,lacell,telecel,viettel
120	Benin	benin	any
121	Brunei	brunei	any
122	Bahamas	bahamas	any
123	Botswana	botswana	any,be_mobile,mascom,orange
124	Belize	belize	any
125	Caf	caf	any
126	Dominica	dominica	any
127	Grenada	grenada	any
128	Georgia	georgia	any,beeline,geocell,hamrah_e_aval,magticom
129	Greece	greece	any,cosmote,ose,q_telecom,vodafone
130	Guineabissau	guineabissau	any
131	Guyana	guyana	any
132	Iceland	iceland	any
133	Comoros	comoros	any
134	Saintkitts	saintkitts	any
135	Liberia	liberia	any,cellcom,comium,libercell,libtelco,lonestar
136	Lesotho	lesotho	any
137	Malawi	malawi	any
138	Namibia	namibia	any
139	Niger	niger	any
140	Rwanda	rwanda	airtel,any,mtn
141	Slovakia	slovakia	any,o2
142	Suriname	suriname	any
143	Tajikistan	tajikistan	any,indigo
144	Monaco	monaco	any
145	Bahrain	bahrain	any
146	Reunion	reunion	any
147	Zambia	zambia	airtel,any,mtn,zamtel
148	Armenia	armenia	any,team,viva,vivo
149	Somalia	somalia	any
150	Congo	congo	airtel,any
151	Chile	chile	any,claro,entel,movistar,wom
152	Burkinafaso	burkinafaso	airtel,any,onatel,telecel
153	Lebanon	lebanon	alfa,any,ogero,touch
154	Gabon	gabon	any
155	Albania	albania	any,telekom,vodafone
156	Uruguay	uruguay	any,claro
157	Mauritius	mauritius	any
158	Bhutan	bhutan	any
159	Maldives	maldives	any
160	Guadeloupe	guadeloupe	any
161	Turkmenistan	turkmenistan	any
162	Frenchguiana	frenchguiana	any
163	Finland	finland	any,dna,elisa,telia
164	Saintlucia	saintlucia	any
165	Luxembourg	luxembourg	any,tango,tiptop
166	Saintvincentgrenadines	saintvincentgrenadines	any
167	Equatorialguinea	equatorialguinea	any
168	Djibouti	djibouti	any
169	Antiguabarbuda	antiguabarbuda	any
170	Caymanislands	caymanislands	any
171	Montenegro	montenegro	any
172	Denmark	denmark	any,lebara,lycamobile
173	Switzerland	switzerland	any
174	Norway	norway	any,lycamobile,my_call,telia
175	Australia	australia	any,optus,telstra,vodafone
176	Eritrea	eritrea	any
177	Southsudan	southsudan	any,mtn,zain
178	Saotomeandprincipe	saotomeandprincipe	any
179	Aruba	aruba	any
180	Montserrat	montserrat	any
181	Anguilla	anguilla	any
183	Northmacedonia	northmacedonia	a1,any,lycamobile,telekom,vip
184	Seychelles	seychelles	any
185	Newcaledonia	newcaledonia	any
186	Capeverde	capeverde	any
187	Usaphysical	usaphysical	any,at_t,lycamobile,moabits,tmobile
189	Fiji	fiji	any
196	Singapore	singapore	any,maxx,simba,singtel,starhub
201	Gibraltar	gibraltar	any,gibtele
""")

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

