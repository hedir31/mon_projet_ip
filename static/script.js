document.addEventListener("DOMContentloaded", function(){
    const from = document.getElementById("from-ip");
    const champips = document.getElementById("champ-ips");
    const btnv = document.getElementById("btn-v");
    const etatch = document.getElementById("etat-ch");
    if (!form){
        return  ;
    }
    
    form.addEventListener("submit", function(){
        const val = champips.value.trim();
        btnv.disabled = true;
        if(val == ""){
            etatch.textContent = "Recherche de votre adresse IP en cours...";
        } else {
            etatch.textContent = " Verification des adresses IP en cours ...";
        }
    }   );
});