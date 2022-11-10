<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

if (isset($_POST['submit'])) {
    if (isset($_POST['code']) && isset($_POST['name'])) 
	{    
        $code = $_POST['code'];
        $name = $_POST['name'];
        
        $host = "localhost";
        $dbUsername = "scaner";
        $dbPassword = "scan";
        $dbName = "qr";
        $conn = new mysqli($host, $dbUsername, $dbPassword, $dbName);
        if ($conn->connect_error) {
            die('Could not connect to the database.');
        }
        else {
            $Select = "SELECT name FROM codes WHERE code = ? LIMIT 1";
            $Insert = "INSERT INTO codes(code, name) values(?, ?)";
            $stmt = $conn->prepare($Select);
            $stmt->bind_param("s", $code);
            $stmt->execute();
            $stmt->bind_result($resultCode);
            $stmt->store_result();
            $stmt->fetch();
            $rnum = $stmt->num_rows;
            if ($rnum == 0) {
                $stmt->close();
                $stmt = $conn->prepare($Insert);
                $stmt->bind_param("ss",$code, $name);
                if ($stmt->execute()) {
                    echo "New record inserted sucessfully.";
                }
                else {
                    echo $stmt->error;
                }
            }
            else {
                echo "This code is in database";
            }
            $stmt->close();
            $conn->close();
        }
    }
    else {
        echo "All field are required.";
        die();
    }
}
else {
    echo "Submit button is not set";
}
?>