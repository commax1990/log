// fetch('http://127.0.0.1:8000/api/apidashborad/?format=json')

var xhr = new XMLHttpRequest();

xhr.open('GET', 'http://127.0.0.1:8000/api/apidashborad/?format=json', true);

xhr.send();

xhr.onreadystatechange = function () {

    if (this.status == 200 & this.responseText != "") {

        massif = JSON.parse(this.responseText);
        var txt = " ";
        txt += "<table border='1'>";
        var kol = true;
        for (var el in massif) {
            var myObj = massif[el];
            if (kol == true) {
                txt += "<thead><tr>";
                for (c in myObj) {
                    txt += "<th>" + c + "</th>";
                }
                txt += "</tr></thead>";
            }
            kol = false;
            txt += "<tbody><tr>";
            for (x in myObj) {
                txt += "<td>" + myObj[x] + "</td>";
            }
            txt += "</tr></tbody>";
        }
        txt += "</table>"
        document.getElementById("table_id").innerHTML = txt;

    }


}
