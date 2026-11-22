
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Example:
# .\scriptL2CppExternal.ps1 L2Cpp.exe sequential 1 10 10 3

# file name
$exe = $args[0]

# Implementation mode
$mode = $args[1]

# Number of threads
$p = [int]$args[2]

# n
$n = [int]$args[3]

# m
$m = [int]$args[4]

# k
$k = [int]$args[5]

# Number of executions
$runs = 10

$sum = 0.0

for ($i = 0; $i -lt $runs; $i++) {
    Write-Host "Run" ($i + 1)

	$time = (Measure-Command { & ".\$exe" $mode $n $m $k $p
    		}).TotalMilliseconds

    Write-Host "Time:" $time "ms"

    $sum += $time
}

$average = $sum / $runs

Write-Host ""
Write-Host "Mode: " $mode
Write-Host "Threads:" $p
Write-Host "Average execution time:" $average "ms"

