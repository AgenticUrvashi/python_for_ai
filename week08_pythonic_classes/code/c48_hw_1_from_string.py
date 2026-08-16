'que : Date class banao with from_string("2026-06-28") classmethod (year, month, day mein todo).'

# restate:data naam ki class banake from_string("2026-06-28") se alag alag karo.

# example: 2026-06-28

# pseudocode:
            # 1.create class Date
            # 2.create special method __init__(self,year,month,day) then self.year = year, self.month = month, self.day = day
            # 3.write @classmethod
            # 4.create method from_string(cls,text) then year,month,day = text.split("-") return cls(int(year),int(month),int(day))
            # 5.obj = class.method(text)
            # 6.print(obj.year,obj.month,obj.day)

# translate:
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls,text):
        year,month,day = text.split("-")
        return cls(int(year), int(month), int(day))

dob = Date.from_string("2026-06-28")

print(dob.year,dob.month,dob.day)

# dry run:
# 2026 06 28