<?php
// In this file we wil add a new user to the database.
include 'functions.php';
// We can not put in to the table if any of the following are empty.
// Username, name, phone, access.
if(!empty($_POST["username"]) && !empty($_POST["name"]) && !empty($_POST["phone"]) && !empty($_POST["Access"]))
{
  $sql = "INSERT INTO Users (Access, UserID, Name, Phone, Active) VALUES ( '";
  $sql .= $_POST["Access"]."', '".$_POST["username"]."', '".$_POST["name"]."', '".$_POST["phone"]."', 1)";

  $conn = connectToDB();
  if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
}

// Redirect to users.php
header( 'Location: ./users.php' ) ;
 ?>
