import os
import sys
import threading
import itertools
import time
import pytermgui as ptg

# Função para rodar seu código dentro do terminal fake
def rodar_mank_os():
    os.system("clear")

    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                return
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rCarregou!\n')

    t = threading.Thread(target=animate)
    t.start()

    time.sleep(10)
  
    done = True

    print(" __  __    _    _   _ _  __   ___  ____       _   ___   ___  ")
    print("|  \/  |  / \  | \ | | |/ /  / _ \/ ___|     / | / _ \ / _ \ ")
    print("| |\/| | / _ \ |  \| | ' /  | | | \___ \     | || | | | | | |")
    print("| |  | |/ ___ \| |\  | . \  | |_| |___) |    | || |_| | |_| |")
    print("|_|  |_/_/   \_\_| \_|_|\_\  \___/|____/     |_(_)___(_)___/ ")
    print("Mank Operating System v1.0.0, oficial version, by lealpontopy enterprises")

    input("$> ")

# Criando janela com terminal fake
with ptg.WindowManager() as manager:
    window = ptg.Window("[bold green]Mank OS Terminal[/]", "")
    manager.add(window)

    # Rodar o Mank OS no terminal GUI
    threading.Thread(target=rodar_mank_os, daemon=True).start()
