<?php
include 'functions.php';
// In this file we will update the values in the database.
if(!empty($_POST["fid"]))
{
  $fid = $_POST['fid'];
  updateValue("FundName", $_POST["fundName"], $fid);
  updateValue("Activity", $_POST["activity"], $fid);
  updateValue("Fund", $_POST["fund"], $fid);
  updateValue("Function", $_POST["function"], $fid);
  updateValue("CostCenter", $_POST["costCenter"], $fid);
  updateValue("ProjectCode", $_POST["projectCode"], $fid);
  updateValue("Balance", $_POST["balance"], $fid);
  updateValue("Users", $_POST["users"], $fid);
  updateValue("Active", $_POST["active"], $fid);

  // Update the date on the fund, because the balance has been updated.
  updateValue("BalanceAsOf", date("m/d/y"), $fid);
}


// Redirect to funds.php
header( 'Location: ./funds.php' ) ;

// Updates a single value.
function updateValue($valueName, $newValue, $valueID)
{
  // Prevents writting an empty value to the table.
  if(empty($valueName) OR empty($newValue) OR empty($valueID))
    return;

  $conn = connectTODB();
  $sql = "UPDATE ListOfFunds SET ".$valueName."='".$newValue."' WHERE FID=".$valueID;
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
