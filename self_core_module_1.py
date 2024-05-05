
#Greatest of all three number
num1,num2,num3=100,100,100

if num1>num2 and num1>num3:
    print('num1 is the greater')
elif num2>num1 and num2>num3:
    print('num2 is the greatest')
elif num3>num1 and num3>num2:
    print('num3 is the greatest')
else:
    print('All number are equal')

#Some functions

a=1
b=2

print('If {0} is the first rank means then {1} is the second rank'.format(a,b))
print(f'If {a} is the first rank means then {b} is the second rank')



#IF

print('Writing a complex nested if contional structure')
print('Enter the input value of upcoming or ask menu')
ques=input()

if ques=='upcoming':
    print('Entered into the upcoming menu')
    batch=input()
    if batch=='DE Weekday':
        print('Class timing is 7Am to 9AM')
    elif batch=='DE Weekend':
        print('Class timing is 9AM to 2PM')
    else:
        print('Choose proper timing')
elif ques=='ask':
    print('Entered into ask menu')
    box=input()
    if box=='mobile':
        print('Enter your mobile number')
        mobile=int(input())
        print('Details has been sent to mobile')
    elif box=='email':
        print('Enter the email address')
        email=input()
        print('Details has been to sent to mail')
else:
    print('Choose the proper menu')



#Loop
name='mafaz'
print(type(name))

for i in name:
    print(i)

name=['mafaz','ishu','salih','shakila','salman','saleem']

for na in name:
    print(na)

order_no=[1,2,3,4,5]
names=['Thameej','Shakila','Salman','Mafaz','Saleem']

for ord in enumerate(order_no):
    for nam in names:
        print(f'First birth childs are {ord} {nam}')


salary=[100,200,300]
bonus=15

for i in salary:
    nett_sal=(salary)+(salary*15)/100
    print(nett_sal)

lst = list(range(0, 10))
print(lst)

for loop_lst in lst:
    print(loop_lst)

lst2 = list(range(2, 59))
print(lst2)





name='Mafaz T S'

print(name.partition(' '))
print(name)
print(name.join(name))



employername="inceptez technologies {0} {1}"
modifed_employername=employername.format("pvt.","ltd.").capitalize()
employername="inceptez technologies"
print(modifed_employername)
joinword='inception'
print(employername.join(joinword))
print(employername.partition(' '))

names='mafaz t be mechnaical engg'
print(names.partition(' '))

course='bigdata'
tutor='irfan'
print(course.join(tutor))

dat='5-6-2202'
print(str(dat).zfill(9))




amt=60
print(str(amt).zfill(5))

amt='INR600'
print(amt.isalnum())
amt=' '
print(amt.isspace())
amt='100'
print('encode')
print(amt.encode('utf-8'))

inst_name='"Inceptezs technologies"'
print(inst_name)
print(inst_name.strip('"'))
print(inst_name.replace('"','123',1))

amt=100
name='mafaz'
print(len(name))
print(amt.__lt__(99))
print(amt.__gt__(99))
print(amt.__eq__(100))
amt=-100
print(abs(amt))

title='Mafaz T BE Mechanical Engineering'
print(title.partition(" "))


id=list([1,2,3,4,5])
name=list(['mafaz','salman','saleem','farook','fayaz'])
print(id)
print(name)

for sch_id in id:
    print(sch_id)

for sch_name in name:
    print(sch_name)

emp_id=[1,2,3]
emp_sal=[100,200,300]

for ix,e_id in enumerate(emp_id):
    e_sal=emp_sal[ix]
    print(f"For this {e_id} employee salary is {e_sal} ")

    stu_name=['stu1','stu2','stu3']
    stu_dep=['Mech','ECE','CSE']

for idx,s_name in enumerate(stu_name):
    s_dep=stu_dep[idx]
    print(f'{s_name} department is {s_dep}')


#Login module

UN='hduser'
PWD='hduser'
cnt=1

while cnt<=5:
    pwd = input()
    if PWD==pwd:
        print('Logged in succesfully')
    elif PWD!=pwd:
        print('Wrong password entered')
        if cnt==5:
            print("Reached maximum limit")
    cnt=cnt+1

#Login module try -2

UN='hduser'
PWD='hduser'
cnt=1
while cnt<=3:
    print('Welcome! Please enter username: ')
    if UN == input():
        break
    else:
        print('Enter the correct username')
        cnt=cnt+1
    if  PWD==input():
        print('Logged in successfully')
        break

        names = list(['Mafaz', 'Salman', 'Saleem'])
        salary = list([1000, 20000, 30000])
        bonus = 20

        for na, id in enumerate(names):
            sal = na(id)
            nett = sal + ((sal * bonus) / 100)
            print(f'{na} salary is {nett}')

#above two snippet is Still not working need to look into it.


#tables for school

table1=list(range(2,5))
table2=list(range(1,11))

for t1 in table1:
    for t2 in table2:
        print(f'{t2} X {t1} =',t2*t1)


#Collection:
lst=[1,2,3,3,4]
print(type(lst))
print(lst)
print(lst[1])

tup=(1,'mafaz',42)
print(type(tup))
print(tup)
print(tup[1])

dic={1:23,2:'mafaz',3:41,'query':'Salman'}
print(type(dic))
print(dic)
print(dic['query'])

st={1,2,5,4,3,2,1,5,6,7}
print(type(st))
print(st)

sal_lst=[10000,20000,30000,40000]
print(sal_lst)
print(sal_lst[1])
print(type(sal_lst))
sal_lst=[10000,20000,30000,'40000']
print(sal_lst)
print(type(sal_lst))

sal_lst=[10000,20000,30000,40000]
for i in sal_lst:
    print(int(i)+150)

#access
sal_lst = [10000, 20000, 30000, 40000]
print(type(sal_lst))
for j in sal_lst:
        print(type(j))
        print('Find the min value from list', min(sal_lst))
        print('Find the max value from list', max(sal_lst))
        print('Find the index 2 value from list', sal_lst[2])
        break

#List


sal_lst=[1000,2000,3000,2000,30000,4000]
#insert using append function
sal_lst.append(15000)
print(sal_lst)

#remove
sal_lst.remove(2000)
print('removing the value',sal_lst)

#insert
sal_lst.insert(3,2345)
print('Insert into list based on index', sal_lst)

#update
sal_lst[1]=95000
print(sal_lst)

sal_lst=[1000,2000,3000,2000,30000,4000]
sal_lst[1:3]=[2222,3333,44444]
print(sal_lst)
sal_lst.pop(2)
print(sal_lst)

sal_lst=[1000,2000,3000,2000,30000,4000]

for i in sal_lst:
    if i==2000:
        sal_lst.remove(i)
        print(i)
print(sal_lst)


# swiggy Usecase method1
try:
    swiggy_cart_purchase_values = {'offmax': 100, 'min_cart': 500, 'off_max_prct': 10, 'min_pur_value':299}

    print('Please enter the cart value:')
    product_val = int(input())
    print('Cart value ', product_val)
    if product_val >= swiggy_cart_purchase_values['min_pur_value'] and product_val <= 1500:
        print('you are eligible for offers')
        off_val = (product_val * 10) / 100
        print('your offer value is ', off_val)
        if off_val >= 100:
            bill_amt = product_val - off_val
            print(f'Final bill amount to pay {bill_amt}')
            print("Maximum offer value is 100")
        elif off_val < 100:
            bill_amt = product_val - off_val
            print('Bill amount of the product', bill_amt)
    elif product_val > 1500:
        bill_amt = (product_val) - swiggy_cart_purchase_values['offmax']
        print('Maximum discount is 100, your bill amount is', bill_amt)
        print(f'Final bill amount to pay {bill_amt}')
    else:
        yet_to_add = swiggy_cart_purchase_values['min_pur_value'] - product_val
        print(f'Add {yet_to_add}rs more to place order')
except ValueError as err_msg:
    print('Error occured due to arguments mistakes', err_msg)

###30
#Generate mail
mail_values={'firstname':'Mafaz','lastname':'T','domain':'gmail.com'}
def generatemail():
    lower=mail_values['firstname']
    mailID=(mail_values['firstname']).lower()+(mail_values['lastname']).lower()+'@'+(mail_values['domain'])
    print(mailID)
    return mailID

generatemail()

###31
'''Write a single program to find the given number is even or whether it is negative and print the output as (the
 given number is even but not negative or the given number is not even but negative or the given number is neither negative nor even) '''

nums=[-2,-9,5,9,12,]

for i in nums:
    val=i % 2
    print(f'Return of module {val}')
    if val==0 and i>0:
        print(f'{i} the given number is even but not negative')
    elif val==1 and i<0:
        print(f'{i} the given number is not even but negative')
    else:
        print(f'{i} the given number is neither negative nor even')


###All the possible way of creating function:

#1
def no_arg_return():
    print('No arguments and return is passed')

no_arg_return()

#2
def arg_return(arg):
    multiplication=arg+100
    print('With arguments and return passed')
    print(multiplication)
    return multiplication

arg_return(20)

#3
def arg_no_return(arg):
    sqrt=arg*arg
    print(sqrt)

arg_no_return(30)


def no_arg_with_return():
    faddition=20+20
    print(faddition)
    return faddition

no_arg_with_return()



def bon_sal(salary,bonus,incentive):
    bon=(salary*bonus)/100
    print(bon)
    bon_sal_inc=salary+bon+incentive
    print(bon_sal_inc)
    return bon_sal_inc


tot_bon_sal_pos=bon_sal(12000,20,1200)
print('positional arguments',tot_bon_sal_pos)

def bon_sal(salary,bonus,incentive):
    bon=(salary*bonus)/100
    print(bon)
    bon_sal_inc=salary+bon+incentive
    print(bon_sal_inc)
    return bon_sal_inc

tot_bon_sal_named=bon_sal(salary=15000,incentive=1450,bonus=30)
print('Nmaed arugment', tot_bon_sal_named)

def bon_sal(salary=1000,bonus=10,incentive=1000):
    bon=(salary*bonus)/100
    print(bon)
    bon_sal_inc=salary+bon+incentive
    print(bon_sal_inc)
    return bon_sal_inc

tot_bon_sal_named=bon_sal(4000)
print('default arugment', tot_bon_sal_named)


#Arbitary Arguments
def func1(*args):
    length_of=len(args)
    print(length_of)
    if length_of==1:
        print(type(func1))
        sal = args[0]
        bon_sal = sal
        return bon_sal
    elif length_of==2:
        print(type(func1))
        sal = args[0]
        bon = args[1]
        bon_sal = sal + bon
        return bon_sal
    elif length_of==3:
        print(type(func1))
        sal = args[0]
        bon = args[1]
        incen = args[2]
        bon_sal = sal + bon +incen
        return bon_sal

print(func1(10000,30,300))
print(func1(10000))
print(func1(10000,30))


def func():
    print('HI')

func()
print(func)


def names(fname,lname):
    name=fname+lname
    return name

def mail_ID():
    domain='@gmdail.com'
    mail=names('mafaz','t')+domain
    return mail

print(mail_ID())

###32

''' Write a nested if then else to print the course fees - check if student choosing bigdata, then fees is 25000, if student choosing
 spark then fees is 15000, if the student choosing datascience then check if machinelearning then 25000 or if deep learning then 45000 otherwise if both then 25000+25000.'''

courses={'bigdata':25000, 'spark':15000, 'datascience':25000,}


class sample():
    def sal_bon(self,sal, bon):
        sal=sal*bon
        return sal

class example():
    def sal_lop(self,wd,sal_per_day):
        lop_month=wd*sal_per_day
        return lop_month


from pyspark.sql.session import SparkSession
spark=SparkSession.builder.appName("Mafaz RDD program").getOrCreate()
sc=spark.sparkContext
sc.setLogLevel("ERROR")

#1
file_RDD=sc.textFile("file:///home/hduser/hive/data/txns")
print(file_RDD.take(2))

#2
lam_spl=lambda row:row.split(',')
map_RDD=file_RDD.map(lam_spl)
print(map_RDD.take(2))

#3
splitrow=lambda srow:float(srow[3])
col_RDD=map_RDD.map(splitrow)
print(col_RDD.take(3))
print(col_RDD.sum())
print(col_RDD.name())
print(col_RDD.min())

print('New Job taken')
file_RDD=sc.textFile("file:///usr/local/hadoop/logs/hadoop-hduser-namenode-localhost.localdomain.log")
print(file_RDD.take(3))
row_split_RDD1=file_RDD.map(lambda hadoop_row:hadoop_row.split(' '))
print("row split is priting")
print(row_split_RDD1.take(3))

filter_RDD3=row_split_RDD1.filter(lambda arg2:len(arg2) > 2 and arg2[2]=='ERROR')
print('Filter applied')
print(filter_RDD3.collect())




file_rdd=sc.textFile("file:///home/hduser/hive/data/txns_20201213_PADE1")#57MB data
file_rdd1=sc.textFile("file:///home/hduser/hive/data/txns")#8.1MB data
print("Local FS created partition-57MB data ",file_rdd.getNumPartitions())
print("Local FS created partition-8MB data ",file_rdd1.getNumPartitions())

hdfs_rdd=sc.textFile("hdfs:///user/hduser/hadoopsample.txt")
print("HDFS created partition ",hdfs_rdd.getNumPartitions())
hdfs_rdd_child=hdfs_rdd.map(lambda x:x%2==0)
print("hdfs child partition",hdfs_rdd_child.getNumPartitions())

prgm_rdd=sc.parallelize(range(1,14))
print("Program based RDD partition",prgm_rdd.getNumPartitions())


print("Partition redefine")

file_rdd=sc.textFile("file:///home/hduser/hive/data/txns_20201213_PADE1", 8)#57MB data
file_rdd1=sc.textFile("file:///home/hduser/hive/data/txns", 8)#8.1MB data
print("Local FS created partition-57MB data ",file_rdd.getNumPartitions())
print("Local FS created partition-8MB data ",file_rdd1.getNumPartitions())

hdfs_rdd=sc.textFile("hdfs:///user/hduser/hadoopsample.txt", 10)
print("HDFS created partition ",hdfs_rdd.getNumPartitions())
hdfs_rdd_child=hdfs_rdd.map(lambda x:x%2==0)
print("hdfs child partition",hdfs_rdd_child.getNumPartitions())


rdd1_part=sc.textFile("/user/hduser/txns_big1")#total partitions will be 2 only
rdd1_part=sc.textFile("/user/hduser/txns_big1",1)#total partitions will be 2 only since minimum 1 is needed, but 2 is available hence 2 is considered
rdd1_part=sc.textFile("/user/hduser/txns_big1",4)#total partitions will increase from 2 to 4
print(rdd1_part.getNumPartitions())

prgm_rdd_redefine= sc.parallelize(range(1,100))
print(prgm_rdd_redefine.getNumPartitions())
print(prgm_rdd_redefine.glom().collect())
prgm_rdd_redefine= sc.parallelize(range(1,100),30)
print(prgm_rdd_redefine.getNumPartitions())
print(prgm_rdd_redefine.glom().collect())


rdd1=sc.parallelize(range(1,1001))
print(rdd1.getNumPartitions())
rdd2=rdd1.repartition(10)
print(rdd2.getNumPartitions())

rdd3=rdd2.filter(lambda x:x%2==0)
print(rdd3.getNumPartitions())

