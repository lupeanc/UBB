###### **PPD - MPI SET UP**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**



1. Solution explorer -> Right click solution -> Properties:
- AT THE TOP - SET: All config - x64

2. C/C++ -> Additional Include Directories -> ADD:
C:\\Program Files (x86)\\Microsoft SDKs\\MPI\\Include

3. Linker -> General -> Additional Library Directories -> ADD:
C:\\Program Files (x86)\\Microsoft SDKs\\MPI\\Lib\\x64

4. Linker -> Input -> Additional Dependencies -> ADD:
msmpi.lib

5. Rebuild project - DONE



OPTIONAL - Run with:

mpiexec -n 2 "C:\\path\\to\\your\\project\\x64\\Debug\\YourProgram.exe"

