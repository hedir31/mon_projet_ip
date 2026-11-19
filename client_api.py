import ipaddress
import requests
from modele_ip import adresseip


class clientapi:
    def __init__(self,url="https://ipinfo.io/json"):
        self.url=url
    def recup_ip(self):
        try:
            rep=requests.get(self.url,Timeout=5)
            if rep.status_code !=  200:
                print("Erreur HTTP :",rep.status_code)
                return None
            dnnee=rep.json()
            ip = dnnee.get("ip","")
            pays = dnnee.get("country","")
            ville = dnnee.get("city","")
            fournisseur = dnnee.get("org","")

            version = ""
            if ip:
                try:
                    addr = ipaddress.ip_address(ip)
                    version ="IPV4" if addr.version == 4 else "IPV6"
                except ValueError:
                    version = ""
            return adresseip(
                ip="ip",
                version="version", 
                pays="pays", 
                ville="ville", 
                fournisseur="fournisseur",
                
            )
        except requests.RequestException as Erreur:
            print("Erreur de connexion :", Erreur)
            return None