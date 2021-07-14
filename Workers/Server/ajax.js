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
        }
    }
    catch (error) {
        console.log(error);
    }
}
