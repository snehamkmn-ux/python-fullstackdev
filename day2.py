# for i in range(10):
#     print("GOOD MORNING SIR")





# for i in range(1,21):
#     print("GOOD MORNING SIR")



# i=1
# while i>=1:
#     print("hi how are you??")
#     i+=1



# def great():                 # fun
#     print("hi sir")
#     print("thank you sir")
# great()



# def add(a,b):
#     result=a+b
#     print(result)
# add(10,20)                 #fun with parameter
# add(30,30)



##############**###############


# student=["bb","priya","navya"]          #list

# student.append("appi")
# student.remove("bb")
# student.insert(4,"bb")
# print(student)
# print(student[2])

###############-------###############


# student=("bb","priya","navya")      #tupple
# print(student)  
# print(student[0])   

##############--------#############

# student={"name":"pooju","age":21,"address":"kkone"}
# student["course"]="python programming"
# student["marks"]=85
# student["collge"]="gopalan"            #dictionary
# print(student["name"], 
#       student["course"])



################----class and object----#############

# class student:
#     def display(self):
#         print("hi sir")
#         print("thank you sir")
# s1=student()
# s1.display()


################-------------------------##############

# class student:
#       def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
        
#       def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Marks:",self.marks)

# s1=student("bb",23,44)
# s2=student("pooju",22,44)
# s1.display()
# s2.display()


#############----------------##############

# class student:
#    def __init__(self):
#        self.__marks=0
#    def set_marks(self,marks):
#       self.__marks=marks
#    def show_marks(self):
#       print("student marks:",self.__marks)

#       s1=student()
#       s1.set_marks(85.5)
#       s1.show_marks()

####################--------------###########

# class grandfather:
#    def land(self):
#       print("grand father has a land")    #maltilevel



# class father(grandfather):
#    def house(self):
#       print("father has house")

# class son(father):
#    def car(self):
#       print("son has a car")

# s=son()
# s.land()
# s.house()
# s.car()


###########---------------############

# class father:
#     def house(self):
#         print("father has a house")

# class son(father):
#     def car(self):
#         print("son has a car")         #maltiple

# class daughter(father):
#     def money(self):
#         print("daughter has money")

# d = daughter()
# s = son()

# s.house()
# s.car()
# d.money()


############______________###########

class animal:
    def sound(self):
              print("animal make sound")

class dog(animal):
     def sound(self):
          print("dog barks")

class cat(animal):
     def sound(self):
          print("cat meow")


animals=[dog(),cat(),animal()]
for animal in animals:
     animal.sound()




#**************------------***************

from abc import ABC,abstractmethod

class payment(ABC):
      @abstractmethod
      def pay(self,amount):
            pass
 


class UPI(payment):
      def pay(self,amount):
            print(f"Paid{amount} using UPI")

class Card(payment):
      def pay(self,amount):
            print(f"paid {amount}using card")  

p1=UPI()
p2=Card()
p1.pay(100)
p2.pay(200)


      







      
 