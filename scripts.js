
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
    }
    var newObject = document.createElement('span');
    newObject.innerHTML = "<input type=\"text\" name=\"qty" +  "\"><input type=\"text\" name=\"stock" +  "\"><input type=\"text\" name=\"desc" + "\"><input type=\"text\" name=\"price" +  "\"><input type=\"text\" name=\"total\"" +  "disabled=\"true\"><br>";
    document.getElementById('objects_').appendChild(newObject);
  }

  function button_check(button, count){
    //console.log(count);
    if (count >= 10){
      button.innerHTML = "Max Funds";
      button.disabled = true;
    }
    else{
      button.innerHTML = "Add Fund";
      button.disabled = false;
    }

  }

  function add_fund(id) {

    button_check(document.getElementById("add_fund_"), document.getElementById('funds_tbl').rows.length);
    var table = document.getElementById('funds_tbl');
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    cell1.innerHTML = "<select name = \"fname\"><option value=\"Test\">Test</option></select>";
    cell2.innerHTML = "<input type=\"text\" name=\"balance\" disabled>";
    cell3.innerHTML = "<input type=\"text\" name=\"percentage\">";
    cell4.innerHTML = "<input type=\"text\" name=\"amount[]\">";
    cell5.innerHTML = "<input type=\"button\" class=\"remove_fund_\" value=\"Remove Fund\" onclick=\"remove_fund(this)\">";
  }

  function remove_fund(id) {
    // -2 because the positioning of the "Remove Fund" button is different relative to the "Add Fund" button
    // and will return a row count 2 higher than the actual number of rows in the funds_tbl
    button_check(document.getElementById("add_fund_"), document.getElementById('funds_tbl').rows.length - 2 );
    var i = id.parentNode.parentNode.rowIndex;
    document.getElementById('funds_tbl').deleteRow(i);
  }


  //this function checks to make sure an amount has been entered for each fund
  //if all amount fields have been filled in, return true
  //if there is an empty amount field, return false
  function validateFunds() {
    var amountValue = document.forms["pinkieForm"].elements['amount[]'];
    //at this point amountValue may be an array if another fund was added
    //we need to check to see if it's an array. If it is we need to check
    //for input in all array fields
    if (amountValue.length > 1){      // We use this if statement to check if amountValue is an array. If it's not an array length will be undefined
      for ( var i = 0; i < amountValue.length; i++){
        if (amountValue[i].value == null || amountValue[i].value == ""){
          //fail
          alert("All amount fields must be filled out");
          return false;
        }
      }
      return true;
    }

    //amountValue is not an array if function reaches this point, so we
    //handle it as a string
    if(amountValue.value == null || amountValue.value == "") {
      //fail
      alert("Amount must be filled out");
      return false;
    }
    //pass
    return true;
  }

  function validateObjects(){
    var form = document.forms["pinkieForm"];
    var qty = form.elements['qty'];
    var desc = form.elements['desc'];
    var prcEach = form.elements['price'];
    for ( var i = 0; i < qty.length; i++){
      var curRow = i + 1;
      if (qty[i].value != null     && qty[i].value != ""  ||
          desc[i].value != null    && desc[i].value != "" ||
          prcEach[i].value != null && prcEach[i].value != ""){

        if (qty[i].value == null || qty[i].value == ""){
          //fail
          alert("Please Enter a QTY for Purchase Item " + curRow);
          return false;
        }
        else if (desc[i].value == null || desc[i].value == ""){
          //fail
          alert("Please Enter a Description for Purchase Item " + curRow);
          return false;
        }
        else if (prcEach[i].value == null || prcEach[i].value == ""){
          //fail
          alert("Please Enter a 'Price Each' for Purchase Item " + curRow);
          return false;
        }
        else{
          //this row passes, move to next row
          continue;
        }
      }
    }
    //all rows pass, return true
    return true;
  }

  //this function does all necessary checks to make sure the form is ready to
  //submit to the server for preprocessing.
  //return true if all tests pass
  //return false if a test fails
  function validateForm() {
    if(!validateObjects()){return false};
    if(!validateFunds()){return false};
    return true;

  }

  //this fuction overrides the default actions of the form submit button
  //the form is submitted upon validation completion.
  $("#submitButton").click(function(button){
      //prevent form from being submitted until validation is passed
      button.preventDefault();
      //do form validation
      var result = validateForm();
      if (!result) {return false;}
      //fill empty text input fields so the server can process the form correctly
      $('#pinkieForm').find('input[type=text]').each(function(e){
        if($(this).val()=="") $(this).val("empty");
      })
      //submit form
      $('#pinkieForm').submit();

  });

  function updateTotal () {
    var total = parseFloat($('input[name="sub-total"]').val()) + parseFloat($('input[name="tax"]').val());
    $('input[name="total-price"]').val(total);
  }

  function updateTax () {
    var totalTax = parseFloat($('input[name="sub-total"]').val()) * 0.08;
    $('input[name="tax"]').val(totalTax);
    updateTotal();
  }

  function updateSubTotal () {
    var totalArray = $('input[name="total"]').get();
    var subTot = 0;
    for ( var i = 0; i < totalArray.length; i++){
      if ( totalArray[i].value != ""){
        subTot = subTot + parseFloat(totalArray[i].value);
      }
    }

    $('input[name="sub-total"]').val(subTot);
    updateTax();
  }

  $('.objects').on('keyup', 'input[name="price"]',function(){ //delegating to closest static element, which is the 'objects' div
    var priceArray = $('input[name="price"]').get();
    var totalArray = $('input[name="total"]').get();
    var qtyArray = $('input[name="qty"]').get();
    for ( var i = 0; i < priceArray.length; i++){
      if (qtyArray[i].value <= 1){
        totalArray[i].value = priceArray[i].value;
      }
      else{
        totalArray[i].value = priceArray[i].value * qtyArray[i].value;
      }

      if ( priceArray[i].value != "" && qtyArray[i].value < 1 ){
        qtyArray[i].value = 1;
      }
      else if ( priceArray[i].value == "") {
        qtyArray[i].value = "";
      }
    }
    updateSubTotal();
  });

  $('input[name="qty"]').keyup(function(){
    var priceArray = $('input[name="price"]').get();
    var totalArray = $('input[name="total"]').get();
    var qtyArray = $('input[name="qty"]').get();
    for ( var i = 0; i < priceArray.length; i++){
      if (qtyArray[i].value >= 1){
        totalArray[i].value = priceArray[i].value * qtyArray[i].value;
      }
    }
    updateSubTotal();
  });
