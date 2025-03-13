import itertools
import threading
import time
import sys
import os
import tkinter


os.system("clear")

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rCarregou! \n')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True


print(" __  __    _    _   _ _  __   ___  ____       _   ___   ___  ")
print("|  \/  |  / \  | \ | | |/ /  / _ \/ ___|     / | / _ \ / _ \ ")
print("| |\/| | / _ \ |  \| | ' /  | | | \___ \     | || | | | | | |")
print("| |  | |/ ___ \| |\  | . \  | |_| |___) |    | || |_| | |_| |")
print("|_|  |_/_/   \_\_| \_|_|\_\  \___/|____/     |_(_)___(_)___/ ")
print("Mank Operating System v1.0.0, oficial version,by lealpontopy enterprises")



print("Pasta Atual: home")
print("User: ")
print("")

rodando = True
while rodando = True:
    commandInput = str(input(">$ "))
    if commandInput == "help" or "Help" or "hep":
        print("Desgraça")

import os
