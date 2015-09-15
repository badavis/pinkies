<!DOCTYPE HTML>
<?php
  include 'functions.php';

  // Check if any GET parameters are set. If they are, we need to get those
  // results, other wise we need to set up the page for an addition to the database.
  if(isset($_GET['type'], $_GET[$_GET['type']]))
  {
    // There was something set we need to check what it was and do a search based off of that.
    // This must match the search param otherwise it won't work...
    $mode = 1;
  }
  else if(isset($_GET['add']))
  {
    // We are doing an addition to the database.
    $mode = 2;
  }
  else
  {
    // Nothing was set and we need to load up the page to list all the users.
    $mode = 3;
  }

  // Gets a user's value.
  function getFundValue($key)
  {
    $conn = connectToDB();
    $sql = "SELECT * FROM ListofFunds WHERE ".$_GET['type']."=".$_GET[$_GET['type']];
    $result = $conn->query($sql);
    // Check if we got any results.
    if ($result->num_rows > 0)
    {
      // Copy over all the values in to php variables.
      // i_ means int and s_ means string (varchar).
      $row = $result->fetch_assoc();
      return$row[$key];
    }
    else
    {
      echo "0 results for ".$_GET['type']." with value of ".$_GET[$_GET['type']];
    }
    $conn->close();
  }

  // Creates a table and prints all the users to the table.
  function printAllFunds()
  {
    $conn = connectToDB();
    $sql = "SELECT * FROM ListOfFunds";
    $result = $conn->query($sql);
    echo "<table>";
    echo "<tr><th>Users</th><th>Fund Name</th><th>Activity</th><th>Fund</th><th>Function</th><th>Cost Center</th> <th>Project Code</th> <th>Balance</th> <th>As of</th> <th> Active </th></tr>";

    if ($result->num_rows > 0)
    {
      // Output data of each row
      while($row = $result->fetch_assoc())
      {
          echo "<tr><td><a href=\".\\funds.php?type=FID&FID=".$row["FID"]."\">".$row["Users"]."</a></td><td>".$row["FundName"]."</td><td>".$row["Function"]."</td>";
          echo "<td>".$row["Fund"]."</td>";
          echo "<td>".$row["Function"]."</td>";
          echo "<td>".$row["CostCenter"]."</td>";
          echo "<td>".$row["ProjectCode"]."</td>";
          echo "<td>".$row["Balance"]."</td>";
          echo "<td>".$row["BalanceAsOf"]."</td>";
          if($row["Active"] == 1)
          {
            echo "<td>"."Yes"."</td>";
          }
          else
          {
            echo "<td>"."No"."</td>";
          }
      }
    }
    else
    {
      echo "0 results in Funds";
    }
    $conn->close();
  }
?>
<!-- Actual page -->
<html>
  <head>
    <?php if($mode == 2) : ?>
      <title> Add New Fund </title>
    <?php elseif($mode == 1) : ?>
      <title> Editing </title>
    <?php else : ?>
      <title> List Of All Funds </title>
    <?php endif;?>
  </head>
  <body>
    <?php if($mode == 2) : ?>
      <!-- Add a new Fund. -->
      <h1> Add a new Fund </h1>
      <a href="./funds.php"> List of all funds </a>
      <form action="addFund.php" method="POST">

      </form>
    <?php elseif($mode == 1) : ?>
      <!-- Edit a user. -->
      <h1> Editting <?php echo getFundValue("FundName")?> </h1>
      <a href="./funds.php"> List of all funds </a>
      <a href="./funds.php?add"> Add a new Fund </a>
      <form action="updateFund.php" method="POST">

      </form>
    <?php else : ?>
      <!-- List of all users page. -->
      <h1> List Of All Funds </h1>
      <a href="./funds.php?add"> Add a new Fund </a>
      <?php printAllFunds(); ?>
    <?php endif;?>
  </body>
</html>
