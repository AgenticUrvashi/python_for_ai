'''Password class banao:

username
private __password
set_password(new_password) → password ko update kare
get_password() → password return kare

Condition: password ki length 6 se kam ho toh "Password too short" print karo.'''

# restate:class banao aur password upadate karo with condition length 6 se kam nhi honi chahiye.

# example: username = anushaka321 then password= Queen$1234, updated password = om_shanti_om

# pseudocode:
            # 1.create class Password.
            # 2.create special method __init__(self,username,password)
            # 3.create method set_password(self,new_password).if len(new_password)<6: print password too short,else self.__password=
            #   new_password print password upadated.
            # 4.create another method get_password(self) return self.__password
            # 5.create obj = Password("anushaka321","Queen$1234")
            # 6.print(obj.get_password())
            # 7.obj.set_password("om_shanti_om") then print obj.get_password()

# translate:
class Password:
    def __init__(self,username,password):
        self.username = username
        self.__password = password

    def set_password(self,new_password):
        if len(new_password) < 6:
            print("password too short")
        else:
            self.__password = new_password
            print("password updated")
            
    def get_password(self):
        return self.__password

obj = Password("anushaka321","Queen$1234")

print(obj.get_password())

obj.set_password("om_shanti_om")

print(obj.get_password())

# dry run:
# Queen$1234
# password updated
# om_shanti_om    