import csv
import datetime
import string

fields = ['name', 'regi_no', '11', '12', '13', '14', '15', '16','T1', '21', '22', '23', '24', '25', '26','T2', '31', '32',
                  '33', '34', '35', '36', 'T3','41', '42', '43', '44', '45', '46', 'T4','51', '52', '53', '54', '55', '56','T5', '61',
                  '62', '63', '64', '65', '66','T6','1DMS','2DMS','3DMS','4DMS','5DMS','1MP','2MP','3MP','4MP','5MP','1POC','2POC','3POC','4POC','5POC','1PPL','2PPL','3PPL','4PPL','5PPL','1SE','2SE','3SE','4SE','5SE','1SPT','2SPT','3SPT','4SPT','5SPT']
#name of csv file
filename = "record.csv"

def data_entry():
    myrec = []
    mystudent = {}
    name = input("NAME              : ")
    #reg_no=input("REGISTRATION NO   : ")
    mystudent['name']=name
    mystudent['regi_no'] ="jics"+ str(last_id())
    myrec.append(mystudent)
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

def last_id():
    id=0
    n=0
    n = size()
    if n>0:
        with open(filename,'r',newline='') as csvfile:
            # creating a csv dict writer object
            reader = csv.DictReader(csvfile, fieldnames=fields)
            for row in  reader:
                id = row['regi_no']
                #print(row['b_id'])
            csvfile.close()
            #c = 1
            c = id[-3:].strip()
            k = str(int(c) + 1).zfill(3)
            return k
    else:
        return "000"

def size():
    n=0
    with open(filename, 'r', newline='') as csvfile:
        # creating a csv dict writer object
        reader = csv.DictReader(csvfile, fieldnames=fields)
        for row in reader:
            data = list(reader)
            n = len(data)
        return n

def data_entries(n):
    for i in range(1,n+1):
        myrec = []
        mystudent = {}
        name=input("NAME of student "+str(i)+"             : ")
        mystudent['name']=name
        mystudent['regi_no']="jics" +str(last_id())
        myrec.append(mystudent)
        with open(filename, 'a',newline='') as csvfile:
            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # writing headers (field names)
            # writer.writeheader()
            with open('record.csv', 'r', newline='') as csvinput:
                reader = csv.reader(csvinput)
                data = list(reader)
                no_lines = len(data)

            if no_lines == 0:
                writer.writeheader()

            # writing data rows
            writer.writerows(myrec)
            csvfile.close()


def delete_entry(n):
    input = open('record.csv', 'r',newline='')
    output = open('records.csv', 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if row[0]!=n:
            writer.writerow(row)
    input.close()
    output.close()

def move():
    input = open('records.csv', 'r',newline='')
    output = open('record.csv', 'w',newline='')
    writer = csv.writer(output)
    for row in csv.reader(input):
            writer.writerow(row)
    input.close()
    output.close()

def add_news(filename, line):
        now = datetime.datetime.now()
        line=str('(A) ')+str(now.date())+str(" ")+str(line)
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)

def show_news():
   with open('notification.csv','r',newline='') as csvFile:
        reader=csv.reader(csvFile)
        print("\nVirtual Bulletin Board  : \n")
        for row in reader:
            print("# ",row[0])
   csvFile.close()

choice=1
print("\t"*10,"****************ADMIN MODE******************")
print("[1] WANT TO ENTER A RECORD \n[2] WANT TO ADD NO OF RECORDS \n[3] WANT TO DELETE AN RECORD")
print("[4] ADD NEWS \n[5] SHOW NEWS\n[6] EXIT")
while choice!=0:
    while True:
        try:
            choice = int(input("\n\nENTER THE CHOICE  : "))
            break
        except:
            print("\n\tINVALID INPUT...")
    if choice==1:
        data_entry()
        print("ENTRY IS added INTO DATABASE")
    elif choice==2:
        while True:
            try:
                n=int(input("no student to add into record : "))
                break
            except:
                print("integer only")
        data_entries(n)
        print(n,"ENTRY IS ADDED INTO DATABASE")
    elif choice==3:
        while True:
            try:
                n=str(input("Enter the Name : "))
                break
            except:
                print("Invalid name entered ..")
        delete_entry(n)
        move()
        print("RECRD OF ",n," IS DELETED")
    elif choice==4:
        news=str(input("enter the news"))
        add_news("notification.csv",news)
    elif choice==5:
        show_news()
    elif choice==6:
        choice=0
