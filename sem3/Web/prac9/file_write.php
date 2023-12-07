<?php

$filename = "file.txt";
$file = fopen($filename, "w");

if (!$file) {
	echo "Failed to open file.";
	exit();
}

fwrite($file, "Here is some text");
fclose($file);

echo "<br>Finished!";
?>
