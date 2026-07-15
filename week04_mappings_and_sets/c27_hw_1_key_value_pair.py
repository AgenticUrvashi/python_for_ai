##que1: 3 dosto ka phone book banao (naam: number) aur .items() se sab print karo.

phone_book={
    "kashish":56789,
    "kanchan":675432,
    "purva":346876
}

for key,value in phone_book.items():
    print(f"{key}:{value}")