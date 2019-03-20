<?php
    if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['photonOn']))
    {
        exec("sudo python3 rgb.py");
    }
    function func()
    {
        // do stuff
    }
?>
