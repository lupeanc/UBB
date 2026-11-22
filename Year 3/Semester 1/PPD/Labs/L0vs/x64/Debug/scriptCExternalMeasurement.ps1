#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\scriptCExternalMeasurement.ps1 L0vs.exe 10
# file name
$exe = $args[0]

# number of runs
$runs = $args[1]

$sum = 0

# for every run, measure the process performance
for ($i = 0; $i -lt $runs; $i++) {
    Write-Host "Run" ($i + 1)

# measure how long a cmd takes to execute
# take its TotalMilliseconds attribute and put it in our var: time
    $time = (Measure-Command {
        & ".\$exe"
    }).TotalMilliseconds

    Write-Host "Time:" $time "ms"

    $sum += $time
}

$average = $sum / $runs

Write-Host ""
Write-Host "Average execution time:" $average "ms"