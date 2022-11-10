<?php
/* Attempt MySQL server connection. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
$link = mysqli_connect("localhost", "root", "root", "qr");
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
 
// Escape user inputs for security
$code = mysqli_real_escape_string($link, $_REQUEST['code']);
$name = mysqli_real_escape_string($link, $_REQUEST['name']);
 
// Attempt insert query execution
$sql = "INSERT INTO codes (code, name) VALUES ('$code', '$name')";
if(mysqli_query($link, $sql)){
    echo "Records added successfully.";
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 
// Close connection
mysqli_close($link);
?>