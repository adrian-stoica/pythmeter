<?php

include "db.php";

//Define data variable
$temperature = $_GET['temperature'];
$humidity = $_GET['humidity'];

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if (isset($_GET['key'])){
    $sql = "INSERT INTO main (temperature, humidity)
    VALUES ($temperature, $humidity)";
} else {
    echo "error";
}
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();

?> 
