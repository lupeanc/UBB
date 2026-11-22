
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# Example:
# .\scriptMatrixGenerator.ps1 10 10 3

# Java executable
$java = "C:\Users\Clayton\.jdks\openjdk-25.0.1\bin\java.exe"

# Java class name
$exe = "Main"

# Number of rows
$n = [int]$args[0]

# Number of cols
$m = [int]$args[1]

# Number of rows/cols in C matrix
$k = [int]$args[2]

$output = & $java $exe $n $m $k

Write-Host ""
Write-Host $output
