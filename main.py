import os
import subprocess
import sys
while True:
    x = input(os.getcwd()+" >>>")
    if x=="Python" or x=="python":
        while True:
            x1 = input("Python shell >>>")
            if x1=="exit":
                break
            try:
                y = eval(x1)                                                                                    
                if y: print(y)
            except:
                try:
                    exec(x1)
                except Exception as e:
                    print("error:", e)
    elif x=="exit":
        sys.exit()
    else:
        x=bytes(x,'utf-8')
        if x[:2].decode("utf-8")=="cd":
            os.chdir(x[3:].decode("utf-8"))
        else:
            p = subprocess.Popen(x[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(str(line.decode('utf-8')))
