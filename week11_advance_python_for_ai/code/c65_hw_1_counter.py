'Restate: Ek function likho with list[str] parameter aur dict[str, int] return type.'

# example:list = {'hello', 'hii', 'good morning'}

# pseudocode:
            # 1.create function len_words(words:list[str]) -> dict[str,int]
            # 2.return {word : len(word) for word in words}
            # 3.print(len_words(["hello","hii","good morning"]))


# translate:

def len_words(words:list[str]) -> dict[str,int]:
        return {word:len(word) for word in words}

print(len_words(["hello","hii","good morning"]))

# dry run:
# {'hello': 5, 'hii': 3, 'good morning': 12}