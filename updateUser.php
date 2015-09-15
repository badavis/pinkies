<?php
include 'functions.php';
// In this file we will update the values in the database.
if(!empty($_POST["uid"]))
{
  $uid = $_POST['uid'];
  updateValue("Name", $_POST["name"], $uid);
  updateValue("UserID", $_POST["username"], $uid);
  updateValue("Access", $_POST["Access"], $uid);
  updateValue("Phone", $_POST["Phone"], $uid);
  if($_POST["Access"] == "Deactive")
  {
    updateValue("Active", "0", $uid);
  }
  else
  {
    updateValue("Active", "1", $uid);
  }
}


// Redirect to users.php
header( 'Location: ./users.php' ) ;

// Updates a single value.
function updateValue($valueName, $newValue, $valueID)
{
  // Prevents writting an empty value to the table.
  if(empty($valueName) OR empty($newValue) OR empty($valueID))
    return;

  $conn = connectTODB();
  $sql = "UPDATE Users SET ".$valueName."='".$newValue."' WHERE UID=".$valueID;
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
