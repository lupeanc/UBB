# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Example:
# .\scriptL2Java.ps1 sequential 1 10
# .\scriptL2Java.ps1 parallel 2 10

# java exe
$java = "C:\Users\Clayton\.jdks\openjdk-25.0.1\bin\java.exe"

# Java class name
$exe = "Main"

# Implementation mode
$mode = $args[0]

# Number of threads
$p = [int]$args[1]

# Number of executions
$runs = [int]$args[2]

$sum = 0.0

for ($i = 0; $i -lt $runs; $i++) {
    Write-Host "Run" ($i + 1)

    # Execute Java and pass the selected variant and thread count.
	$time = (Measure-Command { & $java $exe $mode $p
    		}).TotalMilliseconds

    Write-Host "Time:" $time "ms"

    $sum += $time
}

$average = $sum / $runs

Write-Host ""
Write-Host "Mode:" $mode
Write-Host "Threads:" $p
Write-Host "Average execution time:" $average "ms"
