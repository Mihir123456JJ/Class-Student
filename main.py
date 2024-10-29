class students:
    grade= "4th"
    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
stu1=students("Mia","10 years","I7jjuibht6TGhTTr")
stu2=students("Mihir","10 years","FgbKGIuy4")
stu3=students("Kabirr","11 years","HJFd7T65GHv7g67F")
print("Mia's id number is {} Mia is in {} grade.".format(stu1.id,stu1.grade))
print("Mihir's id number is {} Mihir's is in {} grade.".format(stu2.id,stu2.grade))
