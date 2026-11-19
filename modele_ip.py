import ipaddress

class adresseip:
    def __init__(self,ip="",version="",pays="",ville="",fournisseur=""):
        self.ip = ip
        self.version = version
        self.pays = pays
        self.ville = ville
        self.fournisseur = fournisseur
    def est_valide(self):
        try:
            ipaddress.ip_address(self.ip)
            return True
        except ValueError:
            return False
    def affichage(self):
        print("/n--- Information de l'adresse IP ---")
        print("Adresse IP :",self.ip if self.ip else "Non disponible!")
        print("Version :", self.version if self.version else "Non disponible!")
        print("Pays:",self.pays  if self.pays  else "Non disponible!")
        print("Ville :",self.ville if self.ville else "Non disponible!")
        print("Fournisseur :",self.fournisseur if self.fournisseur else "Non disponible!")
