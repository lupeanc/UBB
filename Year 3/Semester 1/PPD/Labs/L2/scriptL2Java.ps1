# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Example:
# .\scriptL1Java.ps1 sequential 1 10
# .\scriptL1Java.ps1 parallel 2 10

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
    $time = & $java $exe $mode $p
    Write-Host "Time:" $time "ms"

    $sum += $time
}

$average = $sum / $runs

Write-Host ""
Write-Host "Mode:" $mode
Write-Host "Threads:" $p
Write-Host "Average execution time:" $average "ms"
