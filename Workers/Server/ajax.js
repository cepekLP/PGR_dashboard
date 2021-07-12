function get_info() {
        var xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                parse(this.responseText);
            }
        };
        xmlhttp.open("GET", "/info" , true);
        xmlhttp.send();
        setTimeout("get_info()", 1000);
}

function parse(data_){
    console.log(data_)
    if (data_ != "No new data"){
        var data = JSON.parse(data_);
        document.getElementById("rpm").innerHTML= data["rpm"];
    }
}
