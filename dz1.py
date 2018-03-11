num1 = int(input('Введите 1 число:   '))
num2 = int(input('Введите 2 число:   '))
s = (input('Введите символ: + или - или * или /:   '))
otvet =0
if s=='+':
           otvet=num1+num2
           print(otvet)
           
elif s=='-':
    otvet=num1-num2
    print(otvet)

elif s=='*':
    otvet=num1*num2
    print(otvet)

else:
    otvet=num1/num2
    print(otvet)
    
    
    
           
               


