class SingleInstanceMetaClass(type):
    def __init__(cls, name, bases, dic):
        cls.__single_instance = None
        super().__init__(name, bases, dic)

    def __call__(cls, *args, **kwargs):
        if cls.__single_instance:
            return cls.__single_instance
        single_obj = cls.__new__(cls)
        single_obj.__init__(*args, **kwargs)
        cls.__single_instance = single_obj
        return single_obj


class Setting(metaclass=SingleInstanceMetaClass):
    def __init__(self):
        self.db = 'MySQL'
        self.port = 3306


set1 = Setting()
set2 = Setting()

print(set1 is set2)
print(set1.db, set2.port)
set1.db = 'ORACLE'
print(set2.db, set2.port)