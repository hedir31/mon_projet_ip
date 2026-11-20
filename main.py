
from client_api import clientapi

def main():
    print ("=== Application d'information d'adresse IP ===")
    cl = clientapi()
    adr = cl.recup_ip()

    if adr and adr.est_valide():
        adr.affichage()
    else:
        print("Impossible de recuperer une addresse IP valide ")
if __name__ == "__main__":
    main()