import maya.cmds as cmds
class TestClass():
    def __init__(self):
        print "I am alive!!"

    def print_something(self, arg1, arg2):
        print 'something', arg1, arg2


my_instance = TestClass()
print my_instance
my_instance.print_something('nothing', 'other thing')


