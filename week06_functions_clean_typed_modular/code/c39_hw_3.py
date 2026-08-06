'Words ki list ["hi","hello","hey","welcome"] mein se sirf 4+ letter waale filter se rakho.'

# restate:hame sirf 4 se jyada letter wale words rakhane hai.

# example:list_of_word = ["hi","hello","hey","welcome"] then the output is ["hello","welcome"]

# pseudocode:
            # 1.starts with given list.
            # 2.create variable four_plus = store in list then use filter then use lambda x:len(x)>4,list.
            # 3.print four_plus

list_of_word = ["hi","hello","hey","welcome"]

four_plus = list(filter(lambda x: len(x)>4,list_of_word))

print(four_plus)

# dry run:
["hello","welcome"]
