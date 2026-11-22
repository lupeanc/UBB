# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Example:
# .\script.ps1 (FOR SEQ)
# .\script.ps1 4 2

# java exe
$java = "C:\Users\Clayton\.jdks\openjdk-25.0.1\bin\java.exe"

# Java class name
if ($args.Count -eq 0) {
	$exe = "Main"
} else {
	$exe = "MainParallel"
}

# Number of threads
$p = [int]$args[0]

# Number of readers
$p_r = [int]$args[1]

# Number of executions
$runs = 10

$sumInternal = 0.0
$sumExternal = 0.0

for ($i = 0; $i -lt $runs; $i++) {

    Write-Host "Run" ($i + 1)

    $timeExternal = (Measure-Command {
        if ($exe -eq "Main") {
            $timeInternal = & $java $exe
        }
        else {
            $timeInternal = & $java $exe $p $p_r
        }
    }).TotalMilliseconds

    $sumInternal += $timeInternal

    $sumExternal += $timeExternal
}

$averageInternal = $sumInternal / $runs
$averageExternal = $sumExternal / $runs

Write-Host ""
Write-Host "Number of threads:" $p
Write-Host "Number of readers:" $p_r
Write-Host "Average execution time INTERNAL:" $averageInternal "ms"
Write-Host "Average execution time EXTERNAL:" $averageExternal "ms"
