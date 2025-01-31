import sys

# Assignment 4 - Cristobal Lara
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]

print("<h2>Original Values:</h2>")
print("<ul>")
print(f"<li>a: {a}</li>")
print(f"<li>b: {b}</li>")
print(f"<li>c: {c}</li>")
print("</ul>")
print("<br>")

def inputs_are_numeric():
    try:
        val_a = float(a)
        val_b = float(b)
        val_c = float(c)
        return val_a, val_b, val_c
    except ValueError:
        return None, None, None
val_a, val_b, val_c = inputs_are_numeric()
if val_a == None or val_b == None or val_c == None:
    print("<h2>Error: Just valid numbers allowed as input</h2>")
elif val_a < 1:
    print(f"<h2>Error: The input {a} is too small</h2>")
elif val_c < 0:
    print(f"<h2>Error: The value of c: {c} must be positive</h2>")
else:
    if val_b == 0:
        print(f"<h3>The value of b: {b} will not affect the result</h3>")
    #It's not necessary to validate val_c >= 0, because in this point that is True
    print("<h2>Operations applied:</h2>")
    result = val_c**3
    print(f"<h3>base = c**3 = {result}</h3>")
    if result > 1000:
        result = (result**0.5) * 10
        print(f"<h3>result = (base**0.5) * 10 = {result}</h3>")
    else:
        result = (result**0.5) / val_a
        print(f"<h3>result = (base**0.5) / a = {result}</h3>")
    result += val_b
    print(f"<h3>result + b = {result}</h3>")
    print(f"<h2>Final Result is: {result}</h2>")