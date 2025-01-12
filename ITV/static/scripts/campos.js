window.addEventListener("load", inicializar, false);

function inicializar() {
    clases();
    document.getElementById("id_rol").addEventListener("click", campos, false);
}

var clasecliente=document.getElementsByClassName("cliente");
var clasetrabajador=document.getElementsByClassName("trabajador");

function clases(){
    var listacliente=[document.getElementById("id_puesto")];
    var listatrabajador=[document.getElementById("id_fecha_nacimiento")];
    listacliente.forEach(id=>id.parentNode.setAttribute("class","cliente"));
    listatrabajador.forEach(id=>id.parentNode.setAttribute("class","trabajador"));
    [...clasecliente].forEach(id=>id.setAttribute("style","display:none"));
    [...clasetrabajador].forEach(id=>id.setAttribute("style","display:none"));
}

function ocultar(opcion){
    if (opcion=="2"){
        [...clasetrabajador].forEach(id=>id.setAttribute("style","display:none"));              
    } else if (opcion == "3") {        
        [...clasecliente].forEach(id=>id.setAttribute("style","display:none")); 
    }  else { 
        [...clasetrabajador].forEach(id=>id.setAttribute("style","display:none")); 
        [...clasecliente].forEach(id=>id.setAttribute("style","display:none"));        
    }
}

function mostrar(opcion){
    if (opcion=="2"){
        [...clasecliente].forEach(id=>id.setAttribute("style","display:block"));              
    }

    if (opcion == "3") {        
        [...clasetrabajador].forEach(id=>id.setAttribute("style","display:block")); 
    }
}

function campos(e){
    var rol = e.currentTarget.value;
    ocultar(rol);
    mostrar(rol);
}