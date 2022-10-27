
    var obj = {
        "Electrician":['Improper Electrical Wiring','Installing electrical apparatus','Repair and replace equipments'],
        "Plumber" : ["Improper Drainage","Leakage issues","Repair water supply lines",],
        "Carpenter": ["assa"]
    }
    window.onload = function() {
  var wTypeSel = document.getElementById("wtype");
  var complaintSel = document.getElementById("complaint");
  for (var x in obj) {
    wTypeSel.options[wTypeSel.options.length] = new Option(x, x);
  }
  wTypeSel.onchange = function() {
    complaintSel.length=1;
    for (var y in obj[this.value]) {
        let ans = obj[this.value][y]
        complaintSel.options[complaintSel.options.length] = new Option(ans, ans);
    }
  }
}
