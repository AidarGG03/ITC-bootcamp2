#names=("Aidar","banana","macbook")
#names_s=["Aidar","apple","bacbook"]
#print(type(names_s),names_s)
#print(type(names),names)
#names_s[0] = names_s[0].title()
#print(names_s)
#names=["Bakyt","Aman","Bakyt"]
#for i in range(0, 6):
#	names.append(i)
#	names.extend(names)
#print(names)
#PROBLEM0
#names=[]
#txt=("Aidar","banana","apple","sdsa","uri")
#names.extend(txt)
#print(names)
#PROBLEM1
#txt=("sdad","sdasd","sadad")
#print(txt[0:3])
#PROBLEM2
#names=[12,"Aidar", 12.3, ("sdadsa"), [12]]
#print(names)
#PROBLEM3
#names=["Aidar", "Arlen", "Bermet","Elzad","Bekbolot"]
#print(" ".join(names))
#PROBLEM4
#names=["dsadsa","dsadasd","ewew"]
#names_2=["dsads","adsds","rtrr"]
#names.extend(names_2)
#print(names)
#PROBLEM5
#names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jimmy', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
#x=names.count('Jack')
#print(f"imya 'Jack' vywel {x} raza v liste.")
#PROBLEM6
#names=['aidar','jack', 'jimmy']
#names.append('Oscar')
#names.pop(3)
#print(names)
#PROBLEM7
numbers = [0,2,3,1,4,3,4,2,5,2,0,-3,-3,2,0,-1]
result=1
for i in range(len(numbers)):
	result*=numbers[i]
print(result)	
