<?php

$filename = "file.txt";
$file = fopen($filename, "r");

if (!$file) {
	echo "Failed to open file.";
	exit();
}

$filesize = filesize($filename);
$filetext = fread($file, $filesize);
echo "$filetext";

echo "<br>Finished!";
?>
