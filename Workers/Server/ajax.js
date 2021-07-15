function get_info() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4)  {
            if (this.status == 200) {
                parse(this.responseText);
                get_info();
            }
            else{
                setTimeout("get_info()", 500)
            }
        }

    };
    xmlhttp.open("GET", "/info" , true);
    //setTimeout(() => {xmlhttp.send();}, 1000);

    xmlhttp.send();
}

function parse(data_){
    //console.log(data_)
    try {
        if (data_ != "No new data"){
            var data = JSON.parse(data_);
            document.getElementById("rpm").innerHTML= data["rpm"];
            document.getElementById("water_temp").innerHTML= data["water_temp"];
            document.getElementById("gear").innerHTML= data["gear"];
            document.getElementById("gear_cut").innerHTML= data["gear_cut"];
            document.getElementById("TPS").innerHTML= data["TPS"];
            document.getElementById("oil_temp").innerHTML= data["oil_temp"];
            document.getElementById("voltage").innerHTML= data["voltage"];
            document.getElementById("MAP").innerHTML= data["MAP"];
            document.getElementById("intake_temp").innerHTML= data["intake_temp"];
            document.getElementById("lambda").innerHTML= data["lambda"];
            document.getElementById("ecu_temp").innerHTML= data["ecu_temp"];
            document.getElementById("oil_press").innerHTML= data["oil_press"];
            document.getElementById("rpi_temp").innerHTML= data["rpi_temp"];
            document.getElementById("fuel_press").innerHTML= data["fuel_press"];
        }
    }
    catch (error) {
        console.log(error);
    }
}
