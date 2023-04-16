def get_full_name(first_name,last_name,middle_name=""):
    if middle_name == "":
       print(first_name,last_name)
    else:
        print(first_name,middle_name,last_name)
get_full_name(first_name="a",last_name="c")


def English_to_codeMorse():    
    
    dictionnaire = {"A":"·−",
                "B" :"−···",
                "C"	:"−·−·",
                "D" :"−··",
                "E":"·",
                "F" :"··−·",
                "G":"−−·",
                "H":"····",
                "I":"··",
                "J":"·−−−",
                "K":"−·−",
                "L":"·−··",
                "M":"−−",
                "N":"−·",
                "O":"−−−",
                "P":"·−−·",
                "Q":"−−·−",
                "R":"·−·",
                "S":"···",
                "T":"−",
                "U":"··−",
                "V":"···−",
                "W":"·−−",
                "X":"−··−",
                "Y":"−·−−",
                "Z":"−−··"}
   
    phrase = input("Veuillez saisir une phrase en anglais: ")
    phrase = phrase.upper()
    for item in phrase:
        if item in dictionnaire.keys():
            phrase = phrase.replace(item, dictionnaire[item])  
        print(phrase)
English_to_codeMorse()




def Codemorse_to_English():
    dictionnaire = {"·−" : "A",
                "−···" : "B",
                "−·−·" : "C",
                "−··" : "D",
                "·" : "E",
                "··−·" : "F",
                "−−·" : "G",
                "····" : "H",
                "··" : "I",
                "·−−−" : "J",
                "−·−" : "K",
                "·−··" : "L",
                "−−" : "M",
                "−·" : "N",
                "−−−" : "O",
                "·−−·" : "P",
                "−−·−" : "Q",
                "·−·" : "R",
                "···" : "S",
                "−" : "T",
                "··−" : "U",
                "···−" : "V",
                "·−−" : "W",
                "−··−" : "X",
                "−·−−" : "Y",
                "−−··" : "Z"}
   
    phrase = input("Veuillez saisir une phrase en Code Morse: ")
    phrase = phrase.split("/")
    for item in phrase:
        if item in dictionnaire.keys():  
            phrase = phrase.replace(item, dictionnaire[item])
    print(phrase)
Codemorse_to_English()
    
    
    
    
    
    
    
