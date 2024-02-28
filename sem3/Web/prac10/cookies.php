<?php

setcookie("user", "vikas");

if (!isset($_COOKIE["user"]))
	echo "Cookie is not found<br>";
else
	echo "<br>Cookie value : " . $_COOKIE["user"];

echo print_r($_COOKIE);

?>
