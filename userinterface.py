print("-------------------------------------------User Interface----------------------------------------------")
print("\n")

from pynput import keyboard

#Outer enter, empty box print("\u2610\n") 

#Inner enter, filled box print("\u2612\n") 

emptyballot = "    \u2610\n"

xdballot = "    \u2612\n"

ballots = [emptyballot, xdballot]

options = [xdballot, emptyballot, emptyballot, emptyballot, emptyballot, emptyballot, emptyballot]

def on_press(key):
    on_press.currentkey = key
    return False

def listenOn():
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


# ---------------------------------------------------------- Using the definitions


while True:
    print("____________________________________________HELLO USER_____________________________________________\n")
    
    for i in range(0,len(options)):
        print(options[i])

    listenOn()

    if on_press.currentkey == keyboard.Key.esc:
        break


    else:
        if on_press.currentkey == keyboard.Key.down:
            options.insert(0,emptyballot)
            options.pop()

        if on_press.currentkey == keyboard.Key.up:
            options.append(emptyballot)
            options.pop(0)

        for i in range(0,len(options)):
            print(options[i])
