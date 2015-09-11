<?php
  $servername="localhost";
  $username="pinkies2";
  $password="pinkies2";
  $database="pinkies";

  // Creates a connection to the database.
  function connectTODB()
  {
    return new mysqli($servername, $username, $password, $database);
  }
?>
