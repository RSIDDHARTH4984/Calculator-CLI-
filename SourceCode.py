#calculator

print('''
  _____          _      _____ _    _ _            _______ ____  _____  
 / ____|   /\   | |    / ____| |  | | |        /\|__   __/ __ \|  __ \ 
| |       /  \  | |   | |    | |  | | |       /  \  | | | |  | | |__) |
| |      / /\ \ | |   | |    | |  | | |      / /\ \ | | | |  | |  _  / 
| |____ / ____ \| |___| |____| |__| | |____ / ____ \| | | |__| | | \ \ 
 \_____/_/    \_\______\_____|\____/|______/_/    \_\_|  \____/|_|  \_\


        Made By R.Siddharth With Python
                                                                             ''')

userinput = input('''What Do You Want? Addition, Subtraction, Multiplication, Division ?

[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division       

Choose Your Option (1/2/3/4) = ''')

a = input("Enter Your First Number : ")
b = input("Enter Your Second Number : ")

if userinput ==('1'):
    print("Your Answer Is =", int(a)+int(b))
elif userinput ==('2'):
    print("Your Answer Is =", int(a)-int(b))
elif userinput ==('3'):
    print("Your Answer Is =", int(a)*int(b))
elif userinput ==('4'):
    print("Your Answer Is =", int(a)/int(b))

input("\nPress Enter Key To Exit\n")
#Made By R.Siddharth 
                                            