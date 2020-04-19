#!/bin/python

class Expr:
    pass


class Plus(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "+" + str(self.right) + ")"

    def eval(self, env):
        return self.left.eval(env) + self.right.eval(env)


class Minus(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "-" + str(self.right) + ")"

    def eval(self, env):
        return self.left.eval(env) - self.right.eval(env)


class Times(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" +  str(self.left) + "*" + str(self.right) + ")"

    def eval(self, env):
        return self.left.eval(env) * self.right.eval(env)


class Divided(Expr):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + str(self.left) + "/" + str(self.right) + ")"

    def eval(self, env):
        return self.left.eval(env) / self.right.eval(env)



class Const(Expr):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def eval(self, env):
        return self.val


class Var(Expr):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self, env):
        return env[self.name]


# Variable assignement
env = {
    "x" : 2,
    "y" : 4
}

#                 3 *     (      y  +      z   )  = 3*(y+z)
e1 = Times( Const(3), Plus( Var("y"), Var("x") ) )

#               (       3 *      y )  +      x    = (3*y)+x
e2 = Plus( Times( Const(3), Var("y") ), Var("x") )

e3 = Minus( Const(5), Divided( Times( Var("x"), Const(8) ), Var("y") ) )

print(e1, e1.eval(env))
print(e2, e2.eval(env))
print(e3, e3.eval(env))
