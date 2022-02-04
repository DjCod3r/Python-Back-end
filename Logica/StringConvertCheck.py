num1 =  input("Digite um numero")
num2 =  input("Digite um numero")

print(num1.isnumeric())
if num1.isnumeric() and num2.isnumeric():
    print(int(num1) + int(num2))
elif not num1.isnumeric() or num2.isnumeric():
    print("Digite valores numéricos")