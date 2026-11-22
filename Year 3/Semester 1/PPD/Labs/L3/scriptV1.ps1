
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Example:
# .\scriptL3MPI.ps1 MPI_Program.exe 4

# Executable file name
$exe = $args[0]

# Number of MPI processes
$p = [int]$args[1]

# Number of executions
$runs = 10

$sum = 0.0

for ($i = 0; $i -lt $runs; $i++) {

    Write-Host "Run" ($i + 1)

    $time = (Measure-Command {
        mpiexec -n $p ".\$exe"
    }).TotalMilliseconds

    Write-Host "Time:" $time "ms"

    $sum += $time
}

$average = $sum / $runs

Write-Host ""
Write-Host "Implementation: MPI"
Write-Host "Number of processes:" $p
Write-Host "Average execution time:" $average "ms"
