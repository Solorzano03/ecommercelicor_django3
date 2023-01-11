function mostrar() {
    var x = document.getElementById("inputPassword1");
    var y = document.getElementById("inputPassword2");

    if (x.type==="password" || y.type==="password" ){
        x.type ="text";
        y.type ="text";
    } else {
        x.type ="password";
        y.type ="password";
    }
}