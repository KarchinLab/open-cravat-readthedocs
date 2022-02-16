import os
import subprocess
import uuid
import sys

cmd='oc config md'
md = subprocess.check_output(cmd, shell=True)
md = str(md,'utf-8').strip()
print("Modules directory: "+md)

inputArgs = sys.argv
for i in inputArgs[1:]:
        print("Downloading "+i)
        cmd = "oc module info "+i+" | grep \'latest_version:\' | cut -f2 -d:"
        ver = subprocess.check_output(cmd, shell=True)
        ver = str(ver,'utf-8').strip()

        cmd = "oc module info "+i+" | grep \'type\:\' | cut -f2 -d:"
        typ = subprocess.check_output(cmd, shell=True)
        typ = str(typ,'utf-8').strip()
        if len(ver)>0:
                print('Version: '+ver)
                s = subprocess.check_output("mkdir -p "+md+"/"+typ+"s", shell=True)  #Make directory if it doesn't exist 
                s = subprocess.check_output("rm -rf "+md+"/"+typ+"s/"+i, shell=True)  #Remove module if it does exist 
                cmd_p1 = "./azcopy copy 'https://datasetopencravat.blob.core.windows.net/dataset/modules/"
                cmd_p2="?sv=2020-04-08&st=2021-03-11T23%3A50%3A01Z&se=2025-07-26T22%3A50%3A00Z&sr=c&sp=rl&sig=J9J9wnJOXsmEy7TFMq9wjcxjXDE%2B7KhGpCUL4elsC14%3D'"
                cmd2 =  cmd_p1+i+"/"+ver+cmd_p2+" '"+md+"/"+typ+"s' --recursive"
                s = subprocess.check_output(cmd2, shell=True) #Download data 
                cmd = "mv "+md+"/"+typ+"s/"+ver+" "+md+"/"+typ+"s/"+i
                s = subprocess.check_output(cmd, shell=True) #Rename folder 
