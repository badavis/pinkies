<?php
// In this file we wil add a new vender to the database.
include 'functions.php';
// We can not put in to the table if any of the following are empty.
// Vendername, Address, city, state, country, zip, phone
if(!empty($_POST["venderName"]) && !empty($_POST["address"]) && !empty($_POST["city"]) && !empty($_POST["state"]) && !empty($_POST["country"]) && !empty($_POST["zip"]) && !empty($_POST["phone"]))
{
  $sql = "INSERT INTO ListOfVendors (VendorName, Address, City, State, Country, Zip, POC, Phone, Fax, Website, UCRAccount)";
  $sql .= " VALUES ('".$_POST["venderName"]."', '".$_POST["address"]."', '".$_POST["city"]."', '".$_POST["state"]."', '".$_POST["country"]."', '".$_POST["zip"]."', '".$_POST["contact"]."', '";
  $sql .= $_POST["phone"]."', '".$_POST["fax"]."', '".$_POST["website"]."', '".$_POST["UCRAccID"]."')";


  $conn = connectToDB();
  if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
}

// Redirect to vender.php
header( 'Location: ./vender.php' ) ;
 ?>
