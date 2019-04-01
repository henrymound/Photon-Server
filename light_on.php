<?php
    if($_SERVER['REQUEST_METHOD'] == "POST"){
      $red = $_REQUEST['red'];
      $green = $_REQUEST['green'];
      $blue = $_REQUEST['blue'];
      exec("sudo python3 rgb.py $red $green $blue");
    }
?>
