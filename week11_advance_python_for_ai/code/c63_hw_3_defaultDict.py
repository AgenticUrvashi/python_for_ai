'Restate: defaultdict(list) se students ko unki grade ke hisaab se group karo.'
# example:

# pseudocode:
            # 1.from collections import defaultdict
            # 2.group = defaultdict(list)
            # 3.group["A"] = ["Asha","Raju","Sai"] ; group["B"] = ["Amit","Anna","Samar"] ; group["C"] = ["Aina","Ayan","Sajal"]
            #   ; group["D"] = ["Yashika","Himanshu","Samir"]
            # 4. print(group)


# translate:
from collections import defaultdict

group = defaultdict(list)

group["A"] = ["Asha","Raju","Sai"]
group["B"] = ["Amit","Anna","Samar"]
group["C"] = ["Aina","Ayan","Sajal"]
group["D"] = ["Yashika","Himanshu","Samir"]

print(group)

# dry run:
# defaultdict(<class 'list'>, {'A': ['Asha', 'Raju', 'Sai'], 'B': ['Amit', 'Anna', 'Samar'], 
# 'C': ['Aina', 'Ayan', 'Sajal'], 'D': ['Yashika', 'Himanshu', 'Samir']})