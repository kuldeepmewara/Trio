import csv
filename = "record.csv"
fields = ['name', 'regi_no', '11', '12', '13', '14', '15', '16','T1', '21', '22', '23', '24', '25', '26','T2', '31', '32',
                  '33', '34', '35', '36', 'T3','41', '42', '43', '44', '45', '46', 'T4','51', '52', '53', '54', '55', '56','T5', '61',
                  '62', '63', '64', '65', '66','T6','1DMS','2DMS','3DMS','4DMS','5DMS','1MP','2MP','3MP','4MP','5MP','1POC','2POC','3POC','4POC','5POC','1PPL','2PPL','3PPL','4PPL','5PPL','1SE','2SE','3SE','4SE','5SE','1SPT','2SPT','3SPT','4SPT','5SPT']


def show_news():
    with open('notification.csv','r' ,newline='') as csvFile:
        reader=csv.reader(csvFile)
        print("\nVirtual BUlletin Board...")
        for row in reader:
          print("# ",row[0])
    csvFile.close()

def show_term(name):
    with open('record.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name'] == name:
                print("\nMid Term Marks...")
                print("Sub\\Term\t\t[1]\t\t[2]\t\t[3]\t\t[4]\t\t[5]\t\t[Total]\n\n",end='')
                for i in range(1,7):
                    if i == 1:
                        subject = "MP "
                    elif i == 2:
                        subject = "DMS"
                    elif i == 3:
                        subject = "PPL"
                    elif i == 4:
                        subject = "SE "
                    elif i == 5:
                        subject = "POC"
                    elif i == 6:
                        subject = "SPT"
                    print(subject,"->\t\t ",end='')
                    total=0
                    for j in range(1,6):
                        field=str(j)+str(i)
                        if row[field] =='Ab' or row[field]=='':
                            print("  ",row[field],"  ",end='')
                            row[field]=0
                            total = total + int(row[field])
                        else:
                            print("   %2d"%int(row[field]),"  ", end='')
                            total = total + int(row[field])
                    print("\t%2d"%int(total), "\t", end='')
                    print("\n")
                print('-'*52,"\n",end='')
                print("Total (60)\t\t\b",end='')
                for i in range(1,6):
                    if row[str('T')+str(i)]!='Ab' and row[str('T')+str(i)] !='':
                        print("\t%2d" %int(row[str('T')+str(i)]),"\t",end='')

    csvfile.close()

def show_ass(name):
    with open('record.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['name'] == name:
                print("\n\nAssignment Status...")
                print("Sub\\Ass \t\t[1]\t\t[2]\t\t[3]\t\t[4]\t\t[5]\n\n",end='')
                for i in range(1,7):
                    if i == 1:
                        subject = "MP"
                    elif i == 2:
                        subject = "DMS"
                    elif i == 3:
                        subject = "PPL"
                    elif i == 4:
                        subject = "SE"
                    elif i == 5:
                        subject = "POC"
                    elif i == 6:
                        subject = "SPT"
                    print(subject,"->\t\t",end='')
                    for j in range(1,6):
                        field=str(j)+str(subject)
                        if row[field]=='':
                            print("\tNO\t", end='')
                        elif row[field]=='1':
                           print("\tYes\t",end='')
                        else:
                            print("\tNO\t", end='')
                    print("\n")

    csvfile.close()

def name_present(mr):
    with open('record.csv', 'r', newline='') as csvinput:
            names=[]
            for row in csv.reader(csvinput):
                names.append(row[0])
            csvinput.close()
            if mr in names:
                return 1
            else:
                return 0
    csvinput.close()

def show_rec(n):
    with open('record.csv') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             if row['name']==n:
                 print("Name             :",row['name'])
                 print("Registration no. :",row['regi_no'])
                 break
         show_term(name)
         show_ass(name)

    csvfile.close()
def analysis(m):
    n=0
    att=0
    total=0
    n=size()
    max=0
    with open('record.csv','r')as f:
        reader=csv.DictReader(f,fieldnames=fields)
        next(reader)

        for row in reader:

            if row[m]!='Ab':
                row[m]=int(row[m])
                if row[m]>max:
                    max=row[m]
                total=total+row[m]
                att=att+1
        term=int(m[0])
        if term == 1:
            t = "FIRST"
        elif term == 2:
            t = "SECONOD"
        elif term == 3:
            t = "THIRD"
        elif term == 4:
            t = "FOUR"
        elif term == 5:
            t = "FIVE"
        subject=int(m[-1])
        if subject == 1:
                sub="Micro processor"
        elif subject == 2:
                sub= "Discrete Mathematics"
        elif subject == 3:
                sub= "Principl of programming language"
        elif subject == 4:
                sub= "Software engineering"
        elif subject == 5:
                sub= "Principle of communication"
        elif subject == 6:
                sub= "Statistic and probability"
        print("\n******************IN ", t, "mid term for ",sub,"******************\n",end='' )
        print("maximum marks                       : ",max)
        print("Average marks                       : ",round((total/att)))
        print("no of student attend the paper      : ",att)
        print("no of student  not attend the paper : ",n-att)
    f.close()
def size():
    n=0
    with open(filename, 'r', newline='') as csvfile:
        # creating a csv dict writer object
        reader = csv.DictReader(csvfile, fieldnames=fields)
        for row in reader:
            data = list(reader)
            n = len(data)
        return n


def mid_term():
    while True:
        try:
            term = int(input("WHICH MID TERM [1],[2],[3],[4] OR [5] : "))
            break
        except:
            print("integer value only")
    if int(term) not in range(1, 6):
        return 0
    else:
        while True:
            try:
                subject = int(input("SUBJECT : [1]MP\t[2]DMS\t[3]PPL\t[4]SE\t[5]POC]\t[6]SPT : "))
                break
            except:
                print("integer value only")
        if int(subject) not in range(1, 7):
            return 0
        return str(term) + str(subject)
choice=1
print("\t"*10,"****************STUDENT MODE******************")
print("[1] See  notification\n[2] SHOW RECORD \n[3] ANALYSIS \n[4] EXIT")

while choice !=0:
    while True:
        try:
           choice = int(input("\nEnter the choice : "))
           break
        except:
            print("INVALID INPUT..")
    if choice==1:
        show_news()
    elif choice==2:
        name=input("Name             : ")
        a=name_present(name)
        if a==1:
           show_rec(name)
        else:
            print("\n\tRecord with name ", name, " is not present ")
    elif choice==3:
        print("select the term and subject : ")
        m = mid_term()
        if int(m)!=0:
            analysis(m)
        else:
            print("Input out of choice ..")
    elif choice==4:
        choice=0

