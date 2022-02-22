class A:
    b = 123


a = A()

A.b = 456

a.b = 789

print(a.b)


print(a.__dict__)