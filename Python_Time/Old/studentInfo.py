import maya.cmds as cmds
class StudentInfo():
    def __init__(self, name, grade):
        print "I am alive!!"
        self.name = name
        self.grade = grade

    def print_student_info(self):
        print 'Student Name:', self.name, 'Grade:', self.grade


student1 = StudentInfo('Clayton', 'F--')
student2 = StudentInfo('Brandon', 'A++')
student3 = StudentInfo('Casie', 'HighFive')

student1.print_student_info()
student2.print_student_info()
student3.print_student_info()


