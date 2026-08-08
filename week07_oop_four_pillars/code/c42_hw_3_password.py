'Ek Password class with _password aur ek check(guess) method jo True/False de.'

# restate: isa class banao jo password check kare aur True/False return kare.

# example:password = Time@1234 and guess = urvashi , Time@1234

# pseudocode:
            # 1.create class password.
            # 2.create special method __init__(self,password) then self.password = password.
            # 3.create another method check(self,guess) if self.password == guess then print True, else print False
            # 4.create object = Password(password)
            # 5.call the object.check(guess)

# translate:
class Password:
    def __init__(self,_password):
        self._password = _password

    def check(self,guess):
        if self._password == guess:
            print(True)
        else:
            print(False)

pass1 = Password("Time@1234")

pass1.check("urvashi")

pass1.check("Time@1234")

# dry run:
# False
# True