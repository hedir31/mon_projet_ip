from flask import Flask , render_template , request
from client_api import clientapi

app = Flask(__name__)
cl = clientapi()
@app.route("/", methods = ["GET" , "POST"])
def index():
    res = []
    err = []
    ent = ""
    if request.method == "POST":
        ent = request.form.get("ips", "").strip()
        if ent :
            liste_ip = [
                item.strip()
                for item in ent.replace(";",",").split(",")
                if item.strip()
            ]
            for ip_cible in liste_ip:
                adr = cl.recup_ip_specifique(ip_cible)
                if adr and adr.est_valide():
                    res.append(adr)
                else:
                    err.append("impossible de recuperer une IP  valide pour :{ip_cible}.")
        else:
            adr = cl.recup_ip()
            if adr and adr.est_valide():
                res.append(adr)
            else:
                err.append("impossible de recuperer votre addresse IP ")
    else:
        adr = cl.recup_ip()
        if adr and adr.est_valide():
            res.append(adr)
    return render_template(
        "index.html",
        res=res,
        err=err,
        ent=ent,
    )

if __name__ == "__main__":
        app.run(host="127.0.0.1",port = 5000 , debug = True)