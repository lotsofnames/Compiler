import sys
def g64(x,z,h,f,X,Z,file):
    z=float(z)
    h=float(h)
    f=float(f)
    X=float(X)
    x=float(x)
    Z=float(Z)
    XX=float(X)
    while 1:
        if (x+h)>X:

            file.write(f"G00 X{X} Z{Z}\n")
            file.write(f"G01 X{X} Z{z} F{f}\n")
            file.write(f"G00 X{XX} Z{Z}\n")
            break
        file.write(f"G00 X{X-h} Z{Z}\n")
        X=X-h
        file.write(f"G01 X{X} Z{z} F{f}\n")
        file.write(f"G00 X{X+2} Z{Z}\n")

    print(x,z,h,f,X,Z)


lines = []
with open("CNC.txt", 'r') as file:
    for line in file:
        lines.append(line)

with (open("compliedCNC.txt", 'w') as file):

    for line in lines:
        ok=0
        file.write(line)
        if "G01"in line or "G00" in line or "G0" in line or "G1" in line:

            XS=line.split(" ")
            for xs in XS:
                if xs.lower().startswith("x"):
                    X=xs.lower().replace("x","")
                if xs.lower().startswith("z"):
                    Z=xs.lower().replace("z","")


        elif "G64" in line:

            l=line.lower().split(" ")

            for line in l:
                if line.startswith("x"):
                    ok=ok+1
                    
                    x=line.replace("x","")
                elif line.startswith("z"):
                    ok=ok+1
                    
                    z=line.replace("z","")
                elif line.startswith("h"):
                    ok=ok+1
                    
                    h=line.replace("h","")
                elif line.startswith("f"):
                    ok=ok+1
                    
                    f=line.replace("\n","").replace("f","")
                else:
                    ok=ok+0

            
            if ok<4 or ok>5 and Z!=None and X!=None:
                sys.exit("ok error")
            g64(x,z,h,f,X,Z,file)
