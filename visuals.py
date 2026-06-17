import os
import subprocess

print("\033c\033[47;31m")
print("give me a file to check ...")

fname=input().strip()

if not os.path.isfile(fname):
    print("file not found")
    exit(1)

base=os.path.basename(fname)
outdir=base + ".code"

os.makedirs(outdir,exist_ok=True)

subprocess.run(
    ["objdump","--disassembler-options=intel","-D",fname],
    stdout=open("/temp/out.txt","w")
)

with open("/temp/out.txt") as f:
    lines=f.readlines()

current=open(os.path.join(outdir,"start.asm"),"w")

for line in lines:
    s=line.strip()

    if not s:
        continue

    if "<" in s and ">:" in s:
        p1=s.find("<")
        p2=s.find(">:")

        name=s[p1+1:p2]

        if "+" in name:
            continue

        current.close()

        print("-"*50)
        print(name)

        current=open(
            os.path.join(outdir,name+".asm"),
            "w"
        )

    current.write(line)

current.close()