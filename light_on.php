<?php
    if($_SERVER['REQUEST_METHOD'] == "GET"){
      $red = $_REQUEST['red'];
      $green = $_REQUEST['green'];
      $blue = $_REQUEST['blue'];
      $white = $_REQUEST['white'];
      exec("sudo python3 rgb.py $red $green $blue $white");
    }
?>
