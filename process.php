<?php
    $a = escapeshellarg($_POST['a']);
    $b = escapeshellarg($_POST['b']);
    $c = escapeshellarg($_POST['c']);
    $command = escapeshellcmd("python3 calculate.py $a $b $c");
    $output = shell_exec($command);

    echo "<h1>Assignment 4:</h1>";
    echo "<h2>Python Script Result</h2>";
    echo "<div>$output</div>";
?>