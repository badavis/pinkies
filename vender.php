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
    loadVender($_GET['type'], $_GET[$_GET['type']]);
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
  // Load the given vendors information in to a bunch of php variables.
  function loadVender($type, $value)
  {
    $conn = connectTODB();
    $sql = "SELECT 1 FROM ListOfVendors WHERE ".$_GET['type']."=".$_GET[$_GET['type']];
    $result = $conn->query($sql);
    // Check if we got any results.
    if ($result->num_rows > 0)
    {
      // Copy over all the values in to php variables.
      // i_ means int and s_ means string (varchar).
      $row = $result->fetch_assoc();
      $i_VID = $row["VID"];
      $s_VendorName = $row["VendorName"];
      $s_Address = $row["Address"];
      $s_City = $row["City"];
      $s_State = $row["State"];
      $s_Country = $row["Country"];
      $s_Zip = $row["Zip"];
      $s_POC = $row["POC"];
      $s_Phone = $row["Phone"];
      $s_Fax = $row["Fax"];
      $s_Website = $row["Website"];
      $s_UCRAccount = $row["UCRAccount"];
    }
    else
    {
      echo "0 results for ".$_GET['type']." with value of ".$_GET[$_GET['type']];
    }
    $conn->close();
  }

  function printAllVendors()
  {
    $conn = connectTODB();
    $sql = "SELECT * FROM ListOfVendors";
    $result = $conn->query($sql);
    $result = $conn->query($sql);

    if ($result->num_rows > 0)
    {
      // output data of each row
      while($row = $result->fetch_assoc())
      {
          echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
      }
    }
    else
    {
      echo "0 results in ListOfVendors";
    }
    $conn->close();
  }
?>

<!-- Actual page  -->
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

      <form action="" method="post">
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
      <h1> Editing <?php echo $s_VendorName ; ?> </h1>

      <form action="" method="post">
        Vender ID:
        <input type="text" name="vid" value="<?php echo $i_VID ; ?>" readonly>
        <br>
        Vender Name:
        <input type="text" name="venderName" value="<?php echo $s_VendorName ; ?>">
        <br>
        Address:
        <input type="text" name="address" value="<?php echo $s_Address ; ?>">
        <br>
        City:
        <input type="text" name="city" value="<?php echo $s_City ; ?>">
        <br>
        State:
        <input type="text" name="state" value="<?php echo $s_State ; ?>">
        <br>
        Country:
        <input type="text" name="country" value="<?php echo $s_Country ; ?>">
        <br>
        Postal Code:
        <input type="text" name="zip" value="<?php echo $s_Zip ; ?>">
        <br>
        UCR Account ID:
        <input type="text" name="UCRAccID" value="<?php echo $s_UCRAccount ; ?>">
        <br>
        Contact:
        <input type="text" name="contact" value="<?php echo $s_POC ; ?>">
        <br>
        Phone:
        <input type="text" name="phone" value="<?php echo $s_Phone ; ?>">
        <br>
        Fax:
        <input type="text" name="fax" value="<?php echo $s_Fax ; ?>">
        <br>
        Website:
        <input type="text" name="website" value="<?php echo $s_Website ; ?>">

        <br><br>
        <input type="submit" value="Update">
      </form>

    <!-- List a vendor -->
    <?php else : ?>
      <h1> List Of All vendors </h1>
    <?php endif;?>
  </body>
</html>
