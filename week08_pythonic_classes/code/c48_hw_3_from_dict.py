'que : User class mein from_dict classmethod banao.'

# restate:User naam ki class banao classmethod from_dict banao

# example:name = asha and age = 21

# pseudocode:
            # 1.create class User
            # 2.create special method __init__(self,name,age) then self.name = name , self.age = age
            # 3.write @classmethod
            # 4.create method from_dict(cls,data) return cls(data["name"], data["age'])
            # 5.obj = User.from_dict({"name": "Asha", "age": "21"})
            # 6.print obj.name , obj.age


# translate:
class User:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls,data):
        return cls(data["name"], data["age"])

d = User.from_dict({"name": "Asha", "age": "21"})

print(d.name , d.age)

# dry run:
# asha  21