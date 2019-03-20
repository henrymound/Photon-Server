<?php
    if($_SERVER['REQUEST_METHOD'] == "POST" and isset($_POST['photonOn']))
    {
        exec("rgb.py");
    }
    function func()
    {
        // do stuff
    }
?>
