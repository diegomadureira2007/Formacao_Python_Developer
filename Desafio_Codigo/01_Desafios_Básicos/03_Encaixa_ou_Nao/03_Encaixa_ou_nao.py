#Paulinho tem em suas mãos um novo problema. 
#Agora a sua professora lhe pediu que construísse um programa para verificar, 
#à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.


n = int(input())

for i in range(n):
    a, b = input().split()
    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")