<?php
    if($_SERVER['REQUEST_METHOD'] == "GET"){
      $red = $_REQUEST['red'];
      $green = $_REQUEST['green'];
      $blue = $_REQUEST['blue'];
      exec("sudo python3 candle.py $red $green $blue");
    }
?>
