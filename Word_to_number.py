import sys
word = {
    "One" : "1",
    "two" : "2",
    "Three":"3",
    "Four":"4",
    "five":"5"
}

def convert(s):
    x=-1
    try:#try block

        number =''
        for digit in s:
            number+=word[digit]
        x=int(number)
        print('Conversion succeeded')
    except (KeyError,TypeError) as e:#catch block
        print(f"Coversion error : {e!r}",file=sys.stderr)#f string => f"{expr!r}"

    return x    

# not existing in the list will give key error
# when input itself is wrong , it would give type error
result = convert("Three Oneee Four".split())
sp = "Three One Four".split()
print(result)
