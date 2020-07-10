#DETECTOR PROXY BASADO EN EVIL-SOFIA
import requests
import json

def banner():
  print("""

██╗██████╗  ██████╗ ███████╗ ██████╗ 
██║██╔══██╗██╔════╝ ██╔════╝██╔═══██╗
██║██████╔╝██║  ███╗█████╗  ██║   ██║
██║██╔═══╝ ██║   ██║██╔══╝  ██║   ██║
██║██║     ╚██████╔╝███████╗╚██████╔╝
╚═╝╚═╝      ╚═════╝ ╚══════╝ ╚═════╝ 
                              @BARROSOE 

  """)
banner()

geoapi = 'http://ipinfo.io/'
print("")
resp = input("IP>> ")

geoapi = 'http://ipinfo.io/{}'.format(resp)
onde = requests.get("https://ip.teoh.io/api/vpn/"+resp)
salav = requests.get(geoapi)
skri = onde.json()

esono = skri['vpn_or_proxy']

if esono=="no":
  pass
elif esono=="yes":
  print("\n{} => VPN / PROXY".format(resp))
else:
  print("ERROR")
comoja = salav.json()

ciudad = comoja['city']

estado = comoja['region']

pais = comoja['country']

corde = comoja['loc']

postal = comoja['postal']

zhora = comoja['timezone']

print("\nCity - "+ ciudad)
print("\nState - " + estado)
print("\nCountry - " + pais)
print("\nLocation - " + corde)
print("\nZip - " + postal)
print("\nTimezone - " + zhora)
