import sys
import os
import subprocess
import time

sourceDir = "/w/moller12gev-sciwork18/snich/remoll"
config = "beamrastertest"
generator = "moller"

runrange= range(int(sys.argv[1]),int(sys.argv[2]))

outDir="/volatile/halla/moller12gev/snich/sim_out/"+config
jobs=outDir+"/jobs"

if not os.path.exists(outDir):
  os.system("mkdir "+outDir)
if not os.path.exists(jobs):
  os.system("mkdir "+jobs)


for i in runrange:
  outfile=outDir+"/test_"+generator+"_"+str(i)+".root"
  jsubf=open(jobs+"/test_"+str(i)+".sh", "w")
  jsubf.write("#!/bin/bash\n")
  jsubf.write("#SBATCH --account=halla\n")
  jsubf.write("#SBATCH --partition=production\n")
  jsubf.write("#SBATCH --job-name=AirWindow_"+str(i)+"\n")
  jsubf.write("#SBATCH --time=25:00:00\n")
  jsubf.write("#SBATCH --nodes=1\n")
  jsubf.write("#SBATCH --ntasks=1\n")
  jsubf.write("#SBATCH --cpus-per-task=1\n")
  jsubf.write("#SBATCH --mem=2G\n")
  jsubf.write("tcsh -c \"source /apps/root/6.18.00/setroot_CUE\"\n")
  jsubf.write("cd "+sourceDir+"\n")
  jsubf.write("echo \"Current working directory is `pwd`\"\n")	
  jsubf.write("./build/remoll -o "+outfile+" macros/beamraster.mac\n")
  print("sbatch "+jobs+"/test_"+str(i)+".sh") 
