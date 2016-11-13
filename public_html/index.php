<?php

include "db.php";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT date, temperature, humidity FROM main ORDER BY date DESC LIMIT 1";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
		echo "<head><link rel=stylesheet type=text/css href=pythermo.css><meta http-equiv=refresh content=300></head>\r\n";
		echo "<body>\r\n";
        echo "<div class=pythermo-css> Date/Time: ". $row["date"]. "<br> Temperature: " . $row["temperature"]." &#8451;<br> Humidity: " . $row["humidity"]."% </div>\r\n";
    }
} else {
    echo "0 results";
}

echo "<table width=70% align=center style=font-family:arial font-size=30;>\r\n";
echo "<tr><th align=left>Data History</th></tr>";
echo "<tr align=left>\r\n";
echo "<th>Date/Time</th>\r\n";
echo "<th>Temperature</th>\r\n";
echo "<th>Humidity</th>\r\n";
echo "</tr>\r\n";
$sql = "SELECT date, temperature, humidity FROM main ORDER BY date DESC LIMIT 12";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
	echo "<tr>\r\n";
	echo "<td>".$row["date"]."</td>\r\n";
	echo "<td>".$row["temperature"]." &#8451;</td>\r\n";
	echo "<td>".$row["humidity"]."%</td>\r\n";
	echo "</tr>\r\n";
    }
} else {
    echo "0 results";
}
	echo "</table>\r\n";
	echo "</body>";

$conn->close();
?>
