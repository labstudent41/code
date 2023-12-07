<?php

//          mysqli(hostname, username, password, database)
$conn = new mysqli("localhost", "master", "", "sycs19");
if ($conn->connect_error)
	die("Connection Failed!" . $conn->connect_error);
else
	echo "Connected!<br>";

// To run mysql commands
// conn->query("SQL QUERY...");

$result = $conn->query("SELECT * FROM employee");
while ($row = mysqli_fetch_array($result)) {
	echo print_r($row) . "<br>";
}
?>
