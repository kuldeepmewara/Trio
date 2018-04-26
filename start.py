import os
import subprocess
os.system('cls')
def clear():
    subprocess.call("cls",shell=True)

mode=1
os.system('cls')
while mode!=0:
    print("\n[1]\tAdmin \n[2]\tTeacher\n[3]\tStudent\n[4]\tExit")
    while True:
        try:
            mode=int(input("\n\nEnter the mode : "))
            break
        except:
            print("Invalid   ")
    if mode==1:
        os.system('cls')
        clear()
        import admin
    elif mode==2:
        #os.system('cls')
        clear()
        import teacher
    elif mode==3:
        os.system('cls')
        import student
    else:
        mode=0
        print("Thank you ,have Good Day...")