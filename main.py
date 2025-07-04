import sys


def g64(x, z, h, f, X, Z, file):
    z = float(z)
    h = float(h)
    f = float(f)
    X = float(X)
    x = float(x)
    Z = float(Z)
    XX = float(X)
    while 1:
        if (x + h) > X:

            file.write(f"G00 X{X} Z{Z}\n")
            file.write(f"G01 X{X} Z{z} F{f}\n")
            file.write(f"G00 X{XX} Z{Z}\n")
            break
        file.write(f"G00 X{X-h} Z{Z}\n")
        X = X - h
        file.write(f"G01 X{X} Z{z} F{f}\n")
        file.write(f"G00 X{X+2} Z{Z}\n")


lines = []
with open("CNC.txt", "r") as file:
    for line in file:
        lines.append(line)

with open("compliedCNC.txt", "w") as file:
    file.write("G54\n")

    for line in lines:
        k = []
        ok = 0
        for li in line:
            if li.isnumeric():
                continue
            elif li == " " or li == "\n " or li == "\n":
                continue
            elif li == "." or li == "-" or li == "+" or li == "*" or li == "/":
                continue
            else:
                k.append(f" {li}")
        for o in k:
            line = line.replace(o.strip(), o)
        line = line.strip()
        while 1:
            if "  " in line:
                line = line.replace("  ", " ").strip()
            else:
                break

        if "m03" in line.lower().strip() or "m3" in line.lower().strip():
            M3 = line.strip().lower().split(" ")

            for i in M3:

                if i.startswith("s"):
                    file.write(f"{i.title()} ")
                elif i.startswith("m"):
                    file.write(f"{i.replace('0', '').title()} ")
                else:
                    continue
            file.write("\n")
        elif "G01" in line or "G00" in line or "G0" in line or "G1" in line:
            file.write(f"{line}\n")

            XS = line.split(" ")
            for xs in XS:
                if xs.lower().startswith("x"):
                    X = xs.lower().replace("x", "")
                if xs.lower().startswith("z"):
                    Z = xs.lower().replace("z", "")

        elif "G64" in line:

            l = line.lower().split(" ")

            for line in l:
                if line.startswith("x"):
                    ok = ok + 1

                    x = line.replace("x", "")
                elif line.startswith("z"):
                    ok = ok + 1

                    z = line.replace("z", "")
                elif line.startswith("h"):
                    ok = ok + 1

                    h = line.replace("h", "")
                elif line.startswith("f"):
                    ok = ok + 1

                    f = line.replace("\n", "").replace("f", "")
                else:
                    ok = ok + 0

            if ok < 4 or ok > 5 and Z != None and X != None:
                sys.exit("ok error")
            g64(x, z, h, f, X, Z, file)
            X = x
            Z = z
        else:
            file.write(f"{line}\n")
