//$(document).ready(function(){
//Script for getting and displaying date at top of pinkie
  var d = new Date();
  document.getElementById("date").innerHTML += " " + d.toDateString();


//Script for keeping track of current number of object inputs.
//if number of object inputs divided by 5 exceeds 50, disables 'add item' button

  function add_line(id) {
    var count = document.getElementById('objects_').getElementsByTagName('input').length / 5;
    if (count >= 50) {
      var button = document.getElementById('add_line');
      button.innerHTML='Max Objects';
      button.disabled = true;
    }console.log(count);
    document.getElementById('objects_').innerHTML+="<span><input type=\"text\" name=\"qty" + count + "\"><input type=\"text\" name=\"stock" + count + "\"><input type=\"text\" name=\"desc" + count + "\"><input type=\"text\" name=\"price" + count + "\"><input type=\"text\" name=\"total" + count + "\"><br></span>";
  }

  function add_fund(id) {
    //count is the number of table rows in the funds table
    //count is needed to append a number to each new row(fund) added
    var count = document.getElementById('funds_tbl').rows.length;
    if (count >= 10){
      var button = document.getElementById('add_fund');
      button.innerHTML = "Max Funds";
      button.disabled = true;
    }

    var table = document.getElementById('funds_tbl');
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    cell1.innerHTML = "<select></select>"
    cell2.innerHTML = "<input type=\"text\" name=\"balance\" disabled>"
    cell3.innerHTML = "<input type=\"text\" name=\"percentage\">"
    cell4.innerHTML = "<input type=\"text\" name=\"amount\">"
    cell5.innerHTML = "<input type=\"button\" class=\"remove_fund_\" value=\"Remove Fund\" onclick=\"remove_fund(this)\">"
  }

  function remove_fund(id) {
    var i = id.parentNode.parentNode.rowIndex;
    document.getElementById('funds_tbl').deleteRow(i);
  }

  function submit(id){

  }
