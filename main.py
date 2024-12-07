from modules import *

characters = []

while True:
    os.system("cls")
    print("1. Начать игру\n2. Выйти из игры")
    choice = input("Ваш выбор:")
    if choice == "1":
        while True:
            os.system("cls")
            print("1. Создать нового персонажа\n2. Выбор персонажа\n3. Вернуться в меню")
            choice = input("Ваш выбор:")
            if choice == "1":
                name = input("Введите имя нового персонажа:")
                characters.append(Hero("Warrior"))
                print("Герой успешно создан!")
                time.sleep(1)
            elif choice == "2":
                if len(characters) < 1:
                    print("У вас нет персонажей!")
                    time.sleep(1)
                else:
                    for i in range(len(characters)):
                        print(f"{i+1}.{characters[i].name}")
                    #
                    time.sleep(1)
            elif choice == "3":
                break
    elif choice == "2":
        break
    else:
        print(colorama.Fore.RED + "Ошибка, такой команды нет!", colorama.Style.RESET_ALL)
        time.sleep(1)
 

   