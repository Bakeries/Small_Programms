def makeNum(num):
    global left
    global right
    try:
        if (right==''):
            right=num
            return right
        elif (right!=''):
            left=num
            return left
    finally:
        if ((left!='') and (right!='')):
            Calc()
def Calc():
    global left
    global right
    global func
    l=int(left)
    r=int(right)
    if (func=='-'):
        print(l - r)
    elif (func=='+'):
        print(l + r)
    else:
        print(l * r)
    left=''
    right=''
    func=''
def zero(x):
    x='0'
    makeNum(x)
def one(x):
    x='1'
    makeNum(x)
def two(x):
    x='2'
    makeNum(x)
def three(x):
    x='3'
    makeNum(x)
def four(x):
    x='4'
    makeNum(x)
def five(x):
    x='5'
    makeNum(x)
def six(x):
    x='6'
    makeNum(x)
def seven(x):
    x='7'
    makeNum(x)
def eight(x):
    x='8'
    makeNum(x)
def nine(x):
    x='9'
    makeNum(x)
def minus(x):
    global func
    x='-'
    func=x
    return func
def plus(x):
    global func
    x='+'
    func=x
    return func
def times(x):
    global func
    x='*'
    func=x
    return func
x=''
left=''
right=''
func=''
eight(minus(five(x)))
zero(plus(one(x)))
eight(times(nine(x)))
two(minus(nine(x)))
