#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass 
#.\scriptCInternalMeasurement.ps1 L0vs.exe 10
# file name
$exe = $args[0]

# number of runs
$runs = $args[1]

$sum = 0

# for every run, get the outputted time (measured internally) and put it in our var: time
for ($i = 0; $i -lt $runs; $i++) {
    Write-Host "Run" ($i + 1)

    $time = & ".\$exe"

    Write-Host "Time:" $time "ms"

# convert to numeric value first :))
    $sum += [double]$time
}

$average = $sum / $runs

Write-Host ""
Write-Host "Average execution time:" $average "ms"