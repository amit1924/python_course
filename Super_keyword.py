class ParentClass:

    def parent_method(self):
        print("i am parent class")


class ChildClass(ParentClass):  # it will call method of Parent class

    def parent_method(self):
        print("I am parent class under child (parent method class)")
        super().parent_method()

    def child_method(self):
        print("i am child class")
        super().parent_method()


child_object = ChildClass()
child_object.child_method()
child_object.parent_method()
