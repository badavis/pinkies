<?php
include 'functions.php';
// In this file we will update the values in the database.
if(!empty($_POST["vid"]))
{
  $vid = $_POST['vid'];
  updateValue("VendorName", $_POST["venderName"], $vid);
  updateValue("Address", $_POST["address"], $vid);
  updateValue("City", $_POST["city"], $vid);
  updateValue("State", $_POST["state"], $vid);
  updateValue("Country", $_POST["country"], $vid);
  updateValue("Zip", $_POST["zip"], $vid);
  updateValue("UCRAccount", $_POST["UCRAccID"], $vid);
  updateValue("POC", $_POST["contact"], $vid);
  updateValue("Phone", $_POST["phone"], $vid);
  updateValue("Fax", $_POST["fax"], $vid);
  updateValue("Website", $_POST["website"], $vid);
}


// Redirect to venders.php
header( 'Location: ./vender.php' ) ;

// Updates a single value.
function updateValue($valueName, $newValue, $valueID)
{
  // Prevents writting an empty value to the table.
  if(empty($valueName) OR empty($newValue) OR empty($valueID))
    return;

  $conn = connectTODB();
  $sql = "UPDATE ListOfVendors SET ".$valueName."='".$newValue."' WHERE VID=".$valueID;
  if ($conn->query($sql) === TRUE)
  {
    echo $valueName."updated successfully";
  }
  else
  {
    echo "Error updating record: " . $conn->error . "<br>";
  }

  $conn->close();
}

?>
