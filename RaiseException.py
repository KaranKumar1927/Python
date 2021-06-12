import sys

def finMultiple(x):
    if x<0:
        raise ValueError("Cannot read the value less that zero "f"for the given number {x}")

def getnumber():
    
    try:
        finMultiple(10)
        finMultiple(-1)
        print("number is okay")
    except ValueError as e:
        print(e,file=sys.stderr)  

getnumber()              