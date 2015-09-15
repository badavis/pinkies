<!DOCTYPE html>
<?php
  include 'functions.php';

  // Check if any GET parameters are set. If they are, we need to get those
  // results, other wise we need to set up the page for an addition to the database.
  if(isset($_GET['type'], $_GET[$_GET['type']]))
  {
    // There was something set we need to check what it was and do a search based off of that.
    // This must match the search param otherwise it won't work...
    $newAdd = FALSE;
    $listVendors = FALSE;
  }
  else if(isset($_GET['add']))
  {
    $newAdd = TRUE;
    $listVendors = FALSE;
  }
  else
  {
    // Nothing was set and we need to load up the page to list all the venders
    $listVendors = TRUE;
    $newAdd = FALSE;
  }

  // Functions
  // Load the given vendor's information.
  function loadVenderValue($key)
  {
    $conn = connectToDB();
    $sql = "SELECT * FROM ListOfVendors WHERE ".$_GET['type']."=".$_GET[$_GET['type']];
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

  // Function to print all the venders.
  function printAllVendors()
  {
    $conn = connectToDB();
    $sql = "SELECT * FROM ListOfVendors";
    $result = $conn->query($sql);
    echo "<table>";
    echo "<tr><th>Vendor Name</th></tr>";

    if ($result->num_rows > 0)
    {
      // Output data of each row
      while($row = $result->fetch_assoc())
      {
          echo "<tr><td><a href=\".\\vender.php?type=VID&VID=".$row["VID"]."\">".$row["VendorName"]."</a></td></tr>";
      }
    }
    else
    {
      echo "0 results in ListOfVendors";
    }
    $conn->close();
  }
?>

<!-- Actual page -->
<html>
  <head>
    <?php if($newAdd AND !$listVendors) : ?>
      <title> Add New Vender </title>
    <?php elseif(!$newAdd AND !$listVendors) : ?>
      <title> Editing <?php echo $s_VendorName ; ?></title>
    <?php else : ?>
      <title> List Of All vendors </title>
    <?php endif;?>
  </head>
  <body>
    <!-- Add new Vendor Mode-->
    <?php if($newAdd AND !$listVendors) : ?>
      <h1> Add New Vender </h1>
      <a href="./vender.php">List vendors </a>
      <form action="./addVendor.php" method="post">
        Vender Name:
        <input type="text" name="venderName">
        <br>
        Address:
        <input type="text" name="address" >
        <br>
        City:
        <input type="text" name="city" >
        <br>
        State:
        <input type="text" name="state" >
        <br>
        Country:
        <input type="text" name="country" >
        <br>
        Postal Code:
        <input type="text" name="zip" >
        <br>
        UCR Account ID:
        <input type="text" name="UCRAccID" >
        <br>
        Contact:
        <input type="text" name="contact" >
        <br>
        Phone:
        <input type="text" name="phone" >
        <br>
        Fax:
        <input type="text" name="fax" >
        <br>
        Website:
        <input type="text" name="website" >

        <br><br>
        <input type="submit" value="Add">
      </form>

    <!-- Edit a vendor -->
    <?php elseif(!$newAdd AND !$listVendors) : ?>
      <h1> Editing <?php echo loadVenderValue("VendorName") ; ?> </h1>
      <a href="./vender.php?add">Add a vendor </a>
      <a href="./vender.php">List vendors </a>
      <form action="updateVendor.php" method="post">
        Vender ID:
        <input type="text" name="vid" value="<?php echo loadVenderValue("VID") ; ?>" readonly>
        <br>
        Vender Name:
        <input type="text" name="venderName" value="<?php echo loadVenderValue("VendorName") ; ?>">
        <br>
        Address:
        <input type="text" name="address" value="<?php echo loadVenderValue("Address") ; ?>">
        <br>
        City:
        <input type="text" name="city" value="<?php echo loadVenderValue("City") ; ?>">
        <br>
        State:
        <input type="text" name="state" value="<?php echo loadVenderValue("State") ; ?>">
        <br>
        Country:
        <input type="text" name="country" value="<?php echo loadVenderValue("Country") ; ?>">
        <br>
        Postal Code:
        <input type="text" name="zip" value="<?php echo loadVenderValue("Zip") ; ?>">
        <br>
        UCR Account ID:
        <input type="text" name="UCRAccID" value="<?php echo loadVenderValue("UCRAccount") ; ?>">
        <br>
        Contact:
        <input type="text" name="contact" value="<?php echo loadVenderValue("POC") ; ?>">
        <br>
        Phone:
        <input type="text" name="phone" value="<?php echo loadVenderValue("Phone") ; ?>">
        <br>
        Fax:
        <input type="text" name="fax" value="<?php echo loadVenderValue("Fax") ; ?>">
        <br>
        Website:
        <input type="text" name="website" value="<?php echo loadVenderValue("Website") ; ?>">

        <br><br>
        <input type="submit" value="Update">
      </form>

    <!-- List a vendor -->
    <?php else : ?>
      <h1> List Of All vendors </h1>
      <a href="./vender.php?add">Add a vendor </a>
      <?php printAllVendors(); ?>
    <?php endif;?>
  </body>
</html>
