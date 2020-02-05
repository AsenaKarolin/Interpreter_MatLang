import math
import sys
class Matrix:
    def __init__(self, m, n):
        self.n=n
        self.m=m
        self.rows=[[0]*n for x in range(m)]
    
    def __mul__(self,o): #multiplication operation overloading
        if(isinstance(o,Matrix)):
            result=Matrix(self.m,o.n)
            if self.n==o.m :
                for i in range(self.m):
                    for j in range(o.n):
                        for k in range(o.m):
                            result.rows[i][j] += self.rows[i][k]*o.rows[k][j]
            else: #printing error when sizes are not compatible
                print("Error")
            return result
        elif(isinstance(o,int) or (isinsance(o,float))): #if the elements of matrix are float
            result=Matrix(self.m,self.n)
            for i in range(self.m):
                for j in range(self.n):
                    result.rows[i][j]=self.rows[i][j]*o
            return result
    def __rmul__(self,o): #handle the case of multiplication in which first operand is scalar and the second one is matrix
        if (isinstance(o,int) or isinstance(o,float)):
            result=Matrix(self.m,self.n)
            for i in range(self.m):
                for j in range(self.n):
                    result.rows[i][j]=self.rows[i][j]*o
            return result
    
    def __add__(self,o): #summation operation overloading for matrix class
        if isinstance(o, Matrix):
            result=Matrix(self.m, self.n)
            if ((self.m == o.m) and (self.n == o.n)):
                for i in range(self.m):
                    for j in range(self.n):
                        result.rows[i][j] = self.rows[i][j] + o.rows[i][j]
            else:
                print("Error")
            return result
        else:
            print("Error")
    def __sub__(self,o): #substraction operation overloading for matrix class
        if isinstance(o,Matrix):
            result=Matrix(self.m, self.n)
            if ((self.m == o.m) and (self.n == o.n)):
                for i in range(self.m):
                    for j in range(self.n):
                        result.rows[i][j] = self.rows[i][j] - o.rows[i][j]
            else:
                print("Error")
            return result
        else:
            print("Error")
    def fill(self, strg): #function in order to fill the matrix elements by taking the row of statement definiton
        result = Matrix(self.m, self.n)
        numbers = [None] * (self.m*self.n) #put the elements of matrix in an array 
        strg = strg[strg.find("{")+1: strg.find("}")]
        if (len(strg.split())!=self.m*self.n):
            print("Error")
        for s in range(self.m*self.n):
            if ("." not in strg.split()[s]):
                numbers[s] = int(strg.split()[s])
            else:
                numbers[s] = float(strg.split()[s])
        k=0
        for i in range(self.m):
            for j in range(self.n):
                result.rows[i][j]=numbers[k]
                k=k+1
        return result
    def __str__(self): #overload print function to matrix class
        strng = ""
        for i in range(self.m):
            for j in range(self.n):
                if (isinstance(self.rows[i][j],float)):
                    self.rows[i][j] = '{:.7f}'.format(self.rows[i][j])
                mystr = "{}"
                mystr = mystr.format(self.rows[i][j])
                strng = strng + mystr
                if (i<self.m-1) or (j<self.n-1):
                    strng = strng + "\n"
        return strng       
        
def tr(o): #function to take transpose of a matrix
    if isinstance(o, Matrix):
        result=Matrix(o.n,o.m)
        for i in range(o.m):
            for j in range(o.n):
                result.rows[j][i]=o.rows[i][j]
        return result
    else:
        print("Error")
def choose(e1,e2,e3,e4): #function for choose operation
    if (isinstance(e1,float) or isinstance(e1,int)):
        if e1==0:
            if (isinstance(e2,float) or isinstance(e2,int)):
                return e2
            elif (isinstance(e2, Matrix)):
                return e2.rows[0][0]
        elif e1>0:
            if (isinstance(e3,float) or isinstance(e3,int)):
                return e3
            elif (isinstance(e3, Matrix)):
                return e3.rows[0][0]
        else:
            if (isinstance(e4,float) or isinstance(e4,int)):
                return e4
            elif (isinstance(e4, Matrix)):
                return e4.rows[0][0]
    elif (isinstance(e4,Matrix)):
        if e1.rows[0][0]==0:
            if (isinstance(e2,float) or isinstance(e2,int)):
                return e2
            elif (isinstance(e2, Matrix)):
                return e2.rows[0][0]
        elif e1.rows[0][0]>0:
            if (isinstance(e3,float) or isinstance(e3,int)):
                return e3
            elif (isinstance(e3, Matrix)):
                return e3.rows[0][0]
        else:
            if (isinstance(e4,float) or isinstance(e4,int)):
                return e4
            elif (isinstance(e4, Matrix)):
                return e4.rows[0][0]
        
def sqrt(num): #function for sqrt operation
    if (isinstance(num,Matrix)):
        if num.n==1 and num.m==1:
            if (num.rows[0][0]>=0):
                return math.sqrt(num.rows[0][0])
            else:
                print("Error")
    elif (isinstance(num,int) or isinstance(num,float)):
        if (num>=0):
            return math.sqrt(num)
        else:
            print("Error")
    else:
        print("Error")
        
def myPrint(o): #in order to print integers without floating points and printing floats with first seven decimal points
    if (isinstance(o,int)):
        print(o)
    elif (isinstance(o,float)):
        print('{:.7f}'.format(o))
    elif (isinstance(o,Matrix)):
        print(o)

myfile = open(sys.argv[1]).read().split("\n") #taking input file from terminal
exeFile = "" #this is the string which we add all rows then it will be executed
tabCount = int(0) #number of tabs that we put at beginnings of the inside lines of for loops in order to obey indentation rule of python 
for row in myfile: #reading each row of input file
    row = row.strip()
    for index in range(tabCount): #put necessary number of tabs, 1 tab for single for and two tabs for nested loop, zero for normal lines out of for loops
        exeFile = exeFile + "\t"
    if row.startswith("#"): #do nothing for command lines
        continue
    if row.startswith("scalar"): #initializing integers to zero for scalar definition
        exeFile = exeFile + row.split()[1] + "= 0" + "\n"
    if row.startswith("vector"): #initializing vector to matrix of size(n,1), putting zeros inside it
        str1 = row.split()[1][:row.split()[1].find("[")]
        str2 = row.split()[1][row.split()[1].find("[") + 1:row.split()[1].find("]")]
        exeFile = exeFile + str1 + " = Matrix(" + str2 + ",1)" + "\n"
    if row.startswith("matrix"): #initializing matrix by putting all zeros inside it
        str1 = row.split()[1][:row.split()[1].find("[")]
        str2 = row.split()[1][row.split()[1].find("[")+1: row.split()[1].find(",")].strip()
        str3 = row.split()[1][row.split()[1].find(",")+1: row.split()[1].find("]")].strip()
        exeFile = exeFile + str1 + " = Matrix(" + str2 + "," + str3 + ")" + "\n"
    if( "=" in row) and ("{" in row) and ("}" in row): #assign matrix or vector to their actual values by sending the row as a parameter to "fill" function
        exeFile = exeFile + row.split("=")[0].strip() + " = " + row.split("=")[0].strip() + ".fill(\"" + row + "\")" + "\n"
    if( "=" in row) and ("{" not in row) and ("}" not in row) and ("[" not in row) and ("]" not in row): #initializing the actual value of scalar variable
        row=row.strip()
        exeFile = exeFile + row + "\n"
    if ("[" in row) and ("]" in row) and ("vector" not in row) and ("matrix" not in row): #index representation has to be transformed to our matrix field named "rows"
        if ("print" in row):
            row = row.replace("print","myPrint")
        strg = row[row.find("["):row.find("]")+1]
        if ("," in strg):
            num1=strg[strg.find("[")+1:strg.find(",")] + " - 1"
            num2=strg[strg.find(",")+1:strg.find("]")] + " - 1"
            str2=".rows[" + num1 + "][" + num2 + "]"
            row=row.replace(strg,str2)
        else:
            num = strg[strg.find("[")+1:strg.find("]")] + " -1"
            str2 = ".rows[" + num + "][0]"
            row=row.replace(strg,str2)
        row = row.strip()
        if ("for" not in row):
            exeFile = exeFile + row + "\n"
    if ("printsep" in row): #printsep just prints "--------"" as required
        exeFile = exeFile + "print(\"--------\")\n"
    if ("print" in row) and ("printsep" not in row) and ("[" not in row): #row has given as a parameter to our overriden print functio
        row = row.replace("print","myPrint")
        row=row.strip()
        exeFile = exeFile + row + "\n"
    if ("for" in row) and ("," not in row): #this if statement handles the case of not nested for loop
        iterator = (row[row.find("(")+1 : row.find("in ")]).strip()
        numbers = (row[row.find("in")+2 : row.find(")")]).strip()
        stop = numbers.split(":")[1] + " + 1"
        numbers = numbers.split(":")[0] + ":" + stop + ":" + numbers.split(":")[2]
        numbers = numbers.replace(":",",")
        exeFile = exeFile + "for " + iterator + " in range(" + numbers + "):\n" # converts the statement into python for syntax
        tabCount = 1 #asserts tabCount variable to 1, in order to obey indentation rule
    if ("}" in row) and ("{" not in row): #this is the sign of end of the for loop
        tabCount = 0 #no need to put tab after the end of for loop
        exeFile = exeFile + "\n"
    if ("for" in row) and ("," in row): #these are properties of nested for loop line
        iterator1 = (row[row.find("(")+1 : row.find(",")]).strip()
        iterator2 = (row[row.find(",")+1 : row.find("in ")]).strip()
        numbers1 = ((row.split(",")[1])[row.split(",")[1].find("in ") + 3:]).strip()
        numbers2 = ((row.split(",")[2])[:row.split(",")[2].find(")")]).strip()
        stop1 = numbers1.split(":")[1] + " + 1"
        numbers1 = numbers1.split(":")[0] + ":" + stop1 + ":" + numbers1.split(":")[2]
        numbers1 = numbers1.replace(":",",") #starting,ending and step values of first for loop
        stop2 = numbers2.split(":")[1] + " + 1"
        numbers2 = numbers2.split(":")[0] + ":" + stop2 + ":" + numbers2.split(":")[2]
        numbers2 = numbers2.replace(":",",") #starting,ending and step values of second for loop
        exeFile = exeFile + "for " + iterator1 + " in range(" + numbers1 + "):\n" #executable version of first for loop
        exeFile = exeFile + "\t" + "for " + iterator2 + " in range(" + numbers2 + "):\n" #one tab before the second for loop 
        tabCount = 2 #in order to obey indentation rule, we have to put two tabs at the beginings of lines inside the nested loop
exec(exeFile)        