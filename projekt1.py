'''
author =
'''
from typing import KeysView, Text


TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#uživatelé slovník
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

line = 40 * "-"

#login + vstup uživatele
username = input("Enter username: ")
password = input("Enter password: ")

if username in uzivatele.keys() and password == uzivatele[username]:
    print(f"""
{line}
Welcome to the app, {username}
We have {(len(TEXTS))} texts to be analyzed
{line}""")
    chosen_number = input(f"Enter a number btw. 1 and {(len(TEXTS))} to select: ")
    print(line)
    if chosen_number.isdigit() and int(chosen_number) <= len(TEXTS):
        number_of_text = int(chosen_number) -1
    else:
        print("Neplatný vstup, ukončuji..")
        quit()
else:
    print("Neplatné uživatelské jméno nebo heslo!")
    quit()

#list slov bez speciálních znaků
list_of_words = []

for word in TEXTS[number_of_text].split():
    list_of_words.append(word.strip(",.:;"))
while "" in list_of_words:
        list_of_words.remove("")

#Počet slov v textu
print(f"There are {len(list_of_words)} words in the selected text.")

#počet slov zařínající s velkým písmenem
list_of_capitals = []

for word in list_of_words:
    firts_letter = word[0].isupper()
    if firts_letter is True:
        list_of_capitals.append(word)
print(f"There are {len(list_of_capitals)} titlecase words.")

#počet slov nasapné pouze velkými písmeny
list_of_uppers = []

for word in list_of_words:
    if word.isupper() and word.isalpha():
        list_of_uppers.append(word)
print(f"There are {len(list_of_uppers)} uppercase words.")

#počet slov malým písmenem
list_of_lowers = []

for word in list_of_words:
    if word.islower() and word.isalpha():
        list_of_lowers.append(word)
print(f"There are {len(list_of_lowers)} lowercase words.")


#počet čísel zapsaných jako string
list_of_numbers = []

for word in list_of_words:
    if word.isdigit():
        list_of_numbers.append(word)
print(f"There are {len(list_of_numbers)} numeric strings.")

#součet číšel v textu
total = 0

for number in list_of_numbers:
    total += int(number)

print(f"""The sum of all the numbers {total}
{line}
""")

#počet slov vůči délce slova 1-11 písmen
    #proměné
count_of_len_words = []
dict_len_num = {}

    #Vypsání délek textu do listu
for word in list_of_words:
    count_of_len_words.append(len(word))

    #Spočítání délek z listu a zapsáno do slovníku
for number in count_of_len_words:
    number_count = count_of_len_words.count(number)
    dict_len_num.update({number: number_count})

    #Vypsání výsledků
print(
    f"LEN|", "OCCURENCES".center(24), "|NR."
)
print(line)

list_len_num = list(dict_len_num.keys())
list_len_num.sort()

for i in list_len_num:
    hodnota = dict_len_num.get(i)
    print(f"{i:>3}|{'*' * hodnota:<26}|{hodnota}")

print(line)
        
    

       
    
    
   




   