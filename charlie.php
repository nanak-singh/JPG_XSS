<?php
// Execute the ifconfig command
echo "<pre>";
echo "Network Configuration:\n";
echo shell_exec("ifconfig");

// Execute the pwd command
echo "\nCurrent Directory:\n";
echo shell_exec("pwd");
echo "</pre>";
?>
