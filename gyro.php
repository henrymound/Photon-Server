<?php
    if($_SERVER['REQUEST_METHOD'] == "GET"){
      exec("sudo python3 gyro.py");
    }
?>
