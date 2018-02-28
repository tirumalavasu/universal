import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for path, subdirs, files in os.walk(os.getcwd()):
    for f in files:
        searchfile = open(f, "r")
        for num, line in enumerate(searchfile, 1):
            if f != "main.py":
                if "password" in line: 
                    print(os.path.join(path, f, ' has ', line, ' at line:', str(num)))  
                elif "pwd" in line: 
                    print(os.path.join(path, f, ' has ', line, ' at line:', str(num)))  
        searchfile.close()

