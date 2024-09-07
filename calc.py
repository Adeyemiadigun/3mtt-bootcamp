a= int(input('Enter first num: '))
b= int(input('Enter second num: '))
c=input('Enter arithmetic sign: ')
def add():
  result=a+b
  print(result)
  
def subtract():
  result=a-b
  print(result)  

def division():
  result=a/b
  print(result)  
 

 
if(c=='+'):
  	add()
elif(c=='-'):
  	subtract()
elif(c=='/'):
  	division()
else:
  	print('Invalid arithmetic sign')
