<?php
    if isset($_GET("data")){
        $data = $_GET("data");
        $file = fopen("log.txt", "a");
        fwrite($file, $data . "\n");
        fclose($file);
    }
?>
