#O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
#Conferir se um texto vai caber em um tuíte é sua tarefa.

#A saída é dada em uma única linha. 
#Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. 
#Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

T = input()

if len(T) <= 140:
    print("TWEET")
else:
    print("MUTE")
