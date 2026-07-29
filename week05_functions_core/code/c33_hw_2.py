# restate: make_config(**settings) jo saari settings ek dict ke roop mein print kare.

# example:game="subway",level="easy" then the output is game:subway , level:easy.

# pseudocode:
            # 1.create new variable make_config(**settings)
            # 2.use for loop for key value in settings items.then print key value pair.
            # 3.call the function.

# translate:
def make_config(**settings):
    print("======================================")
    print("SETTING")
    print("======================================")
    for key,value in settings.items():
        print(f"{key}:{value}")

make_config(game = "puzzle",Level = "hard")

print("=======================================")

# final output:
# game:puzzle
# Level:hard
