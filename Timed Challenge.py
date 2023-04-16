def function():
    phrase = input('veuillez entrer un mot ou une phrase: ')
    lettre = input("veuillez entre un mot dans test: ")
    if lettre in phrase:
        occurence = phrase.count(lettre)
        print(occurence)
    else:
        occurence = 0
        print(occurence)
function()