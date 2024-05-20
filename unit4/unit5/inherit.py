class person: #the parent class
    #assiging attributes
    def _init_(self, name, age, cid):
         self.name = name
         self.age = age
         self.cid = cid
    #def behaviour / methods
    def walk(self) :
         print(self.name, "is walking")
    def talk(self) :
         print(self.name,"is talking")
    def sleep(self) :
         print(self.name, "is sleeping")
    def eat(self):
         print(self.name, "is eating")

class Teacher(person):
    def _init_(self, name, age, cid, subject, salary,department, designation) :
        super(). _init_ (name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self. designation = designation
    def teach(self) :
         print(self.name,"is teaching")
    def grade_students(self):
         print(self.name,"is grading")
    def attend_meeting(self):
         print(self.name,"is attending meeting")

class Student(person):
    def _init_(self,name,age,cid,std_id,course,year,gpa) :
        super(). _init_ (name,age,cid)
        self.std_id = std_id
        self.course = course
        self.year = year
        self.gpa = gpa
    def study(self):
         print(self.name,'is studying')
    def attend_class(self):
         print(self.name,'is attending class')
    def write_exam(self):
         print(self.name,'is writinf exam')
t1 = Teacher("Tashi",38,12345,"accounts",30000,"commerce","assistant")
s1 = Student("sonam",18,10803001026,280,"BBI",1,3)
s2 = Student("choden",18,10803001027,284,"BBI",1,3.2)
if s1.gpa > s2.gpa:
     print(s1.name,'is better than's2.name)
     student_information = "year: " + str(s1.year) + "course: " + s1.course
     print(student_information)
else:
     print(s2.name,'is better than's1.name)
     student_information = "year: " + str(s2.year) + "course: " + s2.course
     print(student_information)
student_storage = [s1, s2]

for std in student_storage:
     print(std.name)
     print(std.gpa)
     print(std.course)


    
     

