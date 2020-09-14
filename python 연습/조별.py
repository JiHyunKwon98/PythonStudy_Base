import turtle as t

def fibo(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
def fibo_tree(length, n):
    if n > 0:
        t.forward(length)
        t.right(30)
        fibo_tree(length*3/4, n-1)
        t.left(60)
        fibo_tree(length*3/4, n-2)
        t.right(30)
        t.backward(length)

t.setup(500, 500)
s = t.Screen()
t.left(90)
t.color("green")
t.penup()
t.goto(0, -200)
t.pendown()
t.speed(0)

n = t.numinput("입력", "F(n), n : ", 6, 1, 12)
fn = fibo(n)
fibo_tree(100, n)
t.penup()
t.goto(-230, 230)
t.write("F(%d) = %d, 나뭇가지 : %d"%(n, fn. fn))

