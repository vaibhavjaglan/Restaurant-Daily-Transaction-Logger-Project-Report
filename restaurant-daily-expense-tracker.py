import matplotlib.pyplot as p
i = input
f = float
n = int
z = 0
o = 1
l = 12
def w(v):
    print(v)
d = {}
t = []
m = {}
k = 'ON'
m[k] = z
k = 'OFF'
m[k] = z
c = o
while c == o:
    x = "\n"
    y = "Enter Dish Name: "
    q = x + y
    a = i(q)
    x = "Enter Transaction Amount: "
    b = i(x)
    v = f(b)
    x = "Order Type (ON/OFF): "
    b = i(x)
    k = b.upper()
    x = "Enter Hour (0-11): "
    b = i(x)
    h = n(b)
    if a in d:
        x = d[a]
        y = x + o
        d[a] = y
    else:
        d[a] = o
    if k in m:
        x = m[k]
        y = x + o
        m[k] = y
    else:
        m[k] = o
    x = (v, h)
    t.append(x)
    x = "Add another transaction? (y/n): "
    b = i(x)
    k = b.lower()
    y = 'n'
    if k == y:
        c = z
    else:
        c = o
b = []
b.append(z)
b.append(z)
b.append(z)
for x in t:
    v = x[z]
    h = x[o]
    y = z
    if h >= y:
        if h < l:
            y = 4
            j = h // y
            q = b[j]
            if v > q:
                b[j] = v
            else:
                b[j] = q
s = z
for x in t:
    v = x[z]
    s = s + v
x = "\n--- DAILY REPORT ---"
w(x)
x = "Total Revenue: "
y = str(s)
q = x + y
w(q)
x = "Dish Orders: "
y = str(d)
q = x + y
w(q)
x = "Order Modes: "
y = str(m)
q = x + y
w(q)
x = ['0-4 Hours', '4-8 Hours', '8-12 Hours']
y = 'green'
p.bar(x, b, color=y)
x = 'Time Block'
p.xlabel(x)
x = 'Highest Transaction'
p.ylabel(x)
x = 'Max Transaction per 4-Hour Block'
p.title(x)
p.show()
