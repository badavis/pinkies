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
  function getUserValue($key)
  {
    $conn = connectToDB();
    $sql = "SELECT * FROM Users WHERE ".$_GET['type']."=".$_GET[$_GET['type']];
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
  function printAllUsers()
  {
    $conn = connectToDB();
    $sql = "SELECT * FROM Users";
    $result = $conn->query($sql);
    echo "<table>";
    echo "<tr><th>Username</th><th>Name</th><th>Phone #</th><th>Access Lvl</th></tr>";

    if ($result->num_rows > 0)
    {
      // Output data of each row
      while($row = $result->fetch_assoc())
      {
          echo "<tr><td><a href=\".\\users.php?type=UID&UID=".$row["UID"]."\">".$row["UserID"]."</a></td><td>".$row["Name"]."</td><td>".$row["Phone"]."</td><td>";
          if($row["Active"])
          {
            echo $row["Access"];
          }
          else
          {
            echo "Not Active";
          }
          echo "</td></tr>";
      }
    }
    else
    {
      echo "0 results in Users";
    }
    $conn->close();
  }
?>
<!-- Actual page -->
<html>
  <head>
    <?php if($mode == 2) : ?>
      <title> Add New User </title>
    <?php elseif($mode == 1) : ?>
      <title> Editing <?php echo getUserValue("Name")?> </title>
    <?php else : ?>
      <title> List Of All Users </title>
    <?php endif;?>
  </head>
  <body>
    <?php if($mode == 2) : ?>
      <!-- Add a new user. -->
      <h1> Add a new User </h1>
      <a href="./users.php"> List of all users </a>
      <form action="addUser.php" method="POST">
        Username: <input type="text" name="username" /> <br>
        Name: <input type="text" name="name" /> <br>
        Phone: <input type="text" name="phone" /> <br>
        Access Level:
        <select name="Access">
          <option value="Admin">Admin</option>
          <option value="User" default>User</option>
          <option value="Deactive">Deactive</option>
        </select> <br>
        <input type="submit" value="Submit">
      </form>
    <?php elseif($mode == 1) : ?>
      <!-- Edit a user. -->
      <h1> Editting <?php echo getUserValue("Name")?> </h1>
      <a href="./users.php"> List of all users </a>
      <a href="./users.php?add"> Add a new User </a>
      <form action="updateUser.php" method="POST">
        UID: <input type="text" name="uid" value="<?php echo getUserValue("UID")?>" readonly/> <br>
        Username: <input type="text" name="username" value="<?php echo getUserValue("UserID")?>"/> <br>
        Name: <input type="text" name="name" value="<?php echo getUserValue("Name")?>"/> <br>
        Phone: <input type="text" name="phone" value="<?php echo getUserValue("Phone")?>"/> <br>
        Access Level:
        <select name="Access">
          <option value="Admin">Admin</option>
          <option value="User" default>User</option>
          <option value="Deactive">Deactive</option>
        </select> <br>
        <input type="submit" value="Submit">
      </form>
    <?php else : ?>
      <!-- List of all users page. -->
      <h1> List Of All Users </h1>
      <a href="./users.php?add"> Add a new User </a>
      <?php printAllUsers(); ?>
    <?php endif;?>
  </body>
</html>
