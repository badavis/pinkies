<?php
// In this file we wil add a new user to the database.
include 'functions.php';
// We can not put in to the table if any of the following are empty.
// FundName, activity, fund, function, balance.
if(!empty($_POST["fundName"]) && !empty($_POST["activity"]) && !empty($_POST["fund"]) && !empty($_POST["function"]) && !empty($_POST["balance"]))
{
  $sql = "INSERT INTO ListOfFunds (Users, FundName, Activity, Fund, Function, Balance, BalanceAsOf, CostCenter, ProjectCode, Active) VALUES ( '";
  $sql .= $_POST["users"]. "', '".$_POST["fundName"]."', '".$_POST["activity"]."', '".$_POST["fund"]."', '".$_POST["function"]."', ".$_POST["balance"].", '".date("m/d/y")."', '".$_POST["costCenter"]. "', '".$_POST["projectCode"]."', ".$_POST["active"].")";

  echo $sql."<br>";
  $conn = connectToDB();
  if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
}

// Redirect to users.php
//header( 'Location: ./funds.php' ) ;
 ?>
