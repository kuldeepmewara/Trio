import csv
import os
import datetime
fields = ['name', 'regi_no', '11', '12', '13', '14', '15', '16','T1', '21', '22', '23', '24', '25', '26','T2', '31', '32',
                  '33', '34', '35', '36', 'T3','41', '42', '43', '44', '45', '46', 'T4','51', '52', '53', '54', '55', '56','T5', '61',
                  '62', '63', '64', '65', '66','T6','1DMS','2DMS','3DMS','4DMS','5DMS','1MP','2MP','3MP','4MP','5MP','1POC','2POC','3POC','4POC','5POC','1PPL','2PPL','3PPL','4PPL','5PPL','1SE','2SE','3SE','4SE','5SE','1SPT','2SPT','3SPT','4SPT','5SPT']
#name of csv file
filename = "record.csv"

#display the notification
def read():
    with open('notification.csv','r',newline='') as csvFile:
        reader=csv.reader(csvFile)
        print("\nVirtual Bulletin Board  : \n")
        for row in reader:
            print("# ",row[0])
    csvFile.close()
#adding a new news
def add_news(filename, line):
        now = datetime.datetime.now()
        line = str('(T) ')+str(now.date()) + str(" ") + str(line)
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)



#return data of student
def return_data(mr):
    with open('record.csv', 'r', newline='') as csvinput:
            names=[]
            for row in csv.reader(csvinput):
                names.append(row[0])
            csvinput.close()
            if mr in names:
                with open('record.csv', 'r', newline='') as csvinput:
                    for row in csv.reader(csvinput):
                        if row[0]==mr:
                            return row
            else:
                return "name"

    csvinput.close()
#return mid term field name

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
#deleting a record
def delete_entry(n):
    input = open('record.csv', 'r',newline='')
    output = open('records.csv', 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[0]!=n:
            writer.writerow(row)
    input.close()
    output.close()
    move()

def move():
    input = open('records.csv', 'r',newline='')
    output = open('record.csv', 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
            writer.writerow(row)
    input.close()
    output.close()

def total(mydic):
    for i in range(1, 6):
        total = 0
        for j in range(1, 7):
            field = str(i) + str(j)
            if mydic[field]!= ''and mydic[field]!='Ab':
                total = total + int(mydic[field])
            else:
                mydic[field] = 'Ab'
        mydic[str('T')+str(i)]=total

#writing a data into database
def data_entry(myrec):
    with open(filename, 'a',newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        #writing headers (field names)
        with open('record.csv','r',newline='') as csvinput:
            reader=csv.reader(csvinput)
            data=list(reader)
            no_lines=len(data)
        if no_lines ==0:
              writer.writeheader()
        # writing data rows
        writer.writerows(myrec)
    csvfile.close()

# return assignment field name
def assignment():
    term = input("WHICH ASSIGNMENT [1],[2],[3],[4] OR [5]")
    if int(term) not in range(1,6) :
         print("INVALID INPUT ...")
         return 0
    else:
        subject = int(input("SUBJECT : [1]MP\t[2]DMS\t[3]PPL\t[4]SE\t[5]POC]\t[6]SPT"))
        if subject ==1:
            return term+"MP"
        elif subject==2:
            return term+"DMS"
        elif subject==3:
            return term+"PPL"
        elif subject==4:
            return term+"SE"
        elif subject==5:
            return term+"POC"
        elif subject==6:
            return term+"SPT"
        else:
            print("INVALID SELECTION ..")
            return 0

def analysis(m):
    n=0
    att=0
    total=0
    n=size()
    max=0
    with open('record.csv','r')as f:
        reader=csv.DictReader(f)
        row.next()
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
        print("Average marks                       : ",(total/att))
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


print("\t"*10,"****************Teacher MODE******************")
print("[1] See  notification\n[2] Add notification \n[3] Add mid term marks\n[4] Adding Assignment Status \n[5] Analysis \n[6] Exit\n\n")
choice=1
mydic={}

while choice!=0:
    while True:
        try:
            choice = int(input("\n\nENTER THE CHOICE : "))
            break
        except:
            print("\n\tINVALID INPUT..")
    if choice==1:
        read()
    elif choice==2:
        text=input("\nENTER THE NEWS")
        add_news("notification.csv",text)
    elif choice==3:
        mr = input("Name : ")
        a = return_data(mr)
        if a!="name":
            for i in range(0, len(a)):
                mydic[fields[i]] = a[i]
            m = mid_term()
            if m!=0:
                while True:           #exception handling concept here
                    try:
                        marks = int(input("\nEnter the marks ..."))
                        if marks in range(0,11):
                              break
                    except:
                        print("\n\tThat's not a valid input!")
                for key in mydic.keys():
                    if key == m:
                        mydic[key] = marks
                delete_entry(mr)
                total(mydic)
                mylist = []
                mylist.append(mydic)
                data_entry(mylist)
                print("\n\tMarks is successfully Uploaded")

            else:
                print("\n\tINVALID INPUT NO ACTION PERFORMED ,YOU HAVE TO TRY ONCE AGAIN ")
        else:
            print("\n\tRecord with name ", mr, " is not present ")

    elif choice==4:
        mr =input("Name             : ")
        a = return_data(mr)
        if a!="name":
            for i in range(0, len(a)):
                mydic[fields[i]] = a[i]
            m=assignment()
            if m!=0:
                marks=9
                while int(marks) != 1 and int(marks) != 0:  #handling of run time error
                    marks = input("ASSIGNMENT SUBMITTED [1] OR NOT [0] : ")
                for key in mydic.keys():
                    if key==m:
                       mydic[key] = marks
                delete_entry(mr)
                mylist = []
                mylist.append(mydic)
                data_entry(mylist)
                print("\n\tAssingment status  is successfully Uploaded")
            else:
                print("\n\tNO ACTION PERFORMED ,YOU HAVE TO TRY ONCE AGAIN ")
        else:
            print("\n\tRecord with name ", mr, " is not present ")
    elif choice==5:
        print("select the term and subject : ")
        m = mid_term()
        if m!=0:
            analysis(m)
        else:
            print("Input out of choice..")
    elif choice==6:
        choice = 0

