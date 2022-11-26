import os
while True:
    values = []
    participants = {}
    option = ' '
    while option != 'no':
        os.system("CLS")
        name = input("Please give me the name of the participant: ")
        money = int(input("Please say how much money will you offer: "))
        participants[name]=  money
        option = input("Is another participant? Type 'yes' or 'no': ")
    for keys in participants:
        values.append(participants[keys])
    maximum = max(values)
    for keys in participants:
        if maximum == participants[keys]:
            print(f"{keys} is the winner with {maximum} dollars uwu")
            os.system("PAUSE")