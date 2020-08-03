import keyboard
import time
sel = 0
name_list = []
vardict = dict()

while True:
    print("Type a name. Type br to break.")
    name = input()
    if name == "br":
        break
    name_list.append(name)



class namestring:
    def __init__(self, text):
        self.text = text
    def draw(self):
        print(self.text)

def clear():
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

def setlist():
    for i in range(len(name_list)):
        l = i+1
        if sel == l:
            vardict[i] = namestring(">"+str(l)+". "+name_list[i])
            vardict[i].draw()
        else:
            vardict[i] = namestring(str(l)+". "+name_list[i])
            vardict[i].draw()
def UpdateScreen():
    clear()
    setlist()

while True:
    if keyboard.is_pressed('up arrow'):
        if sel == 1:
            sel = len(name_list)
        else:
            sel -= 1
        UpdateScreen()
        time.sleep(0.2)
    elif keyboard.is_pressed('down arrow'):
        if sel == len(name_list):
            sel = 1
        else:
            sel += 1
        UpdateScreen()
        time.sleep(0.2)
