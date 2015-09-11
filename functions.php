<?php
  // Creates a connection to the database. Otherwise outputs an error.
  function connectToDB()
  {

    $servername="localhost";
    $un="pinkies";
    $pd="pinkies2";
    $db="pinkies2";
    $conn = new mysqli($servername, $un, $pd, $db);
    // Check connection
    if ($conn->connect_error)
    {
      echo "Connection failed: " . $conn->connect_error;
    }
    return $conn;
  }
?>
