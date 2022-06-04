import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

tort = {"наполеон": [["мука", "маргарин", "ванилин"], 4, 1500], "медовик": [["сметана", "мед", "сахар"], 6, 2000]}
engine.say("Какой торт Вы хотели бы приобрести: ")
engine.runAndWait()
a = input("Какой торт Вы хотели бы приобрести: ").lower()
engine.say("Что Вы хотели бы уточнить: ")
engine.runAndWait()
b = input("Что Вы хотели бы уточнить: ").lower()
for k, v in tort.items():
    if k == a:
        if b == "описание":
            engine.say(f"Торт состоит из {v[0]}")
            engine.runAndWait()
            print("Торт состоит из", *v[0])
        elif b == "стоимость":
            engine.say(f"Торт стоит {v[-2]} рублей")
            engine.runAndWait()
            print(v[-2], "рубля")
engine.say("Сколько торта Вам положить: ")
engine.runAndWait()
gramm = int(input("Сколько торта Вам положить: "))
engine.say("Какой торт Вы хотели бы приобрести: ")
engine.runAndWait()
client_tort = input("Какой торт Вы хотели бы приобрести: ").lower()
# client_discont = input("У вас есть наша 5 %-ая дисконтная карта?: ").lower()
print(f"к оплате {tort[client_tort][1] * gramm / 100}")
engine.say(f"торта {client_tort} осталось {tort[client_tort][-1] - gramm} грамм")
engine.runAndWait()
print(f"торта {client_tort} осталось {tort[client_tort][-1] - gramm} грамм")