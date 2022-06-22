print("-------------------------------------------Menu----------------------------------------------")
print("\n")
from click import option
from numpy import save
from pynput import keyboard
from datagenerator import LastNames
from SQLCommands import insertSQL, deleteSQL, showinfoSQL, saveSQL

#Outer enter, empty box print("\u2610\n") 

#Inner enter, filled box print("\u2612\n") 

emptyballot = "    \u2610"


xdballot = "    \u2612"

ballots = [emptyballot, xdballot]

options = [xdballot, emptyballot, emptyballot, emptyballot, emptyballot]
optionnames = ["View Patients","Add Patient","Delete Patient","Save", "Exit"]

selected = 0

inmenu = 1

def on_press(key):
    on_press.currentkey = key
    return False

def listenOn():
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


# ---------------------------------------------------------- Using the definitions
for i in range(0,len(options)):
    print(options[i] + "  " + optionnames[i] + "\n")

while inmenu == 1:
    
    listenOn()

    if on_press.currentkey == keyboard.Key.esc:
        break

    if on_press.currentkey == keyboard.Key.enter:

        if selected == 0:
            showinfoSQL()
            print("Showing Patients")
            

        elif selected == 1:
            insertSQL()
            print("Adding value, please save.")

        
        elif selected == 2:
            deleteSQL()
            print("Deleting value, please save.")


        elif selected == 3:
            saveSQL()
            print("Saved")
            inmenu = 0
            break

        elif selected == 4:
            print("Exiting")
            inmenu = 0
            break

        else:   
            print("Erros: Please contact administrator.")

    else:
        print("____________________________________________Menu_____________________________________________\n")

        if on_press.currentkey == keyboard.Key.down:
            options.insert(0,emptyballot)
            options.pop()

        if on_press.currentkey == keyboard.Key.up:
            options.append(emptyballot)
            options.pop(0)

        for i in range(0,len(options)):
            print(options[i] + "  " + optionnames[i] + "\n")
        
        selected = options.index(xdballot)
        print(selected)


# IMPORTANT: DO NOT CLICK COMMAND LINE WHEN USING ARROW KEYS, CLICK DOWN WHERE CODE IS WRITTEN.



























