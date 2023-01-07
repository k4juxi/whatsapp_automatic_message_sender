import pywhatkit as pw
import csv
import pyautogui
import webbrowser
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

dashboard_mesaj = '''

 _       ____  _____  ___________ ___    ____  ____     ___   __  ____________  __  ______  ________________
| |     / / / / /   |/_  __/ ___//   |  / __ \/ __ \   /   | / / / /_  __/ __ \/  |/  /   |/_  __/  _/ ____/
| | /| / / /_/ / /| | / /  \__ \/ /| | / /_/ / /_/ /  / /| |/ / / / / / / / / / /|_/ / /| | / /  / // /     
| |/ |/ / __  / ___ |/ /  ___/ / ___ |/ ____/ ____/  / ___ / /_/ / / / / /_/ / /  / / ___ |/ / _/ // /___   
|__/|__/_/_/_/_/__|_/_/__/____/_/__|_/_/___/_/_____ /_/__|_\____/_/_/ _\____/_/__/_/_/__|_/_/ /___/\____/   
        /  |/  / ____/ ___/ ___//   | / ____/ ____/  / ___// ____/ | / / __ \/ ____/ __ \                   
       / /|_/ / __/  \__ \\__ \/ /| |/ / __/ __/     \__ \/ __/ /  |/ / / / / __/ / /_/ /                   
      / /  / / /___ ___/ /__/ / ___ / /_/ / /___    ___/ / /___/ /|  / /_/ / /___/ _, _/                    
     /_/  /_/_____//____/____/_/  |_\____/_____/   /____/_____/_/ |_/_____/_____/_/ |_|                     
                                                                                                    
                     Whatsapp Automatic Message Sender | Twitter: -
                                         
'''

                                                                                                        
print(dashboard_mesaj)
#Toplu mesaj gönderme
liste = []
with open('{.csv dosya uzantılı dosyanın yolu}', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        liste.append(row[1])

webbrowser.open('https://web.whatsapp.com/', new=2)
time.sleep(6)
for i in range(len(liste)):
    pyautogui.leftClick(x=521,y=258)
    keyboard.type(liste[i])
    time.sleep(1)
    pyautogui.leftClick(x=400,y=387)
    pyautogui.leftClick(x=1728,y=968)
    keyboard.type("Bu alana göndermek istediğiniz mesajı yazınız.")
    pyautogui.leftClick(x=1786,y=966)

