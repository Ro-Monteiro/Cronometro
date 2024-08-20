from datetime import datetime
import tkinter as tk
import win32gui
import win32con

def set_always_on_top(window_title):
    # Encontra a janela com o título especificado
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        # Define a janela como sempre no topo
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def cronometro():
    target = datetime(2024, 10, 13)
    now = datetime.now()

    leftover = target - now
    days = str(leftover.days)
    
    hours = str(leftover.seconds//3600).zfill(2)
    resto = leftover.seconds%3600

    minutes = str(resto//60).zfill(2)
    resto = resto%60

    seconds = str(resto).zfill(2)

    # miliseconds = str(leftover.microseconds)[0:2]
    
    texto = days + ' days ' + hours + 'h '+ minutes + 'm ' + seconds + "s "
    # texto = days + ' :' + hours + ': '+ minutes + ': ' + seconds + ": " + miliseconds

    return texto



def update(cheat_tracker):
    cronometro_text.config(text = cronometro())
    set_always_on_top('Você precisa estudar por mais...')
    root.after(50, lambda: update(cheat_tracker))

def key_tracker(event):
    global cheat_tracker
    global count

    cheat_tracker.append(event.keysym.lower())
    
    if cheat_tracker and count<10:
        if cheat_tracker[0] == close[count]:
            count += 1
            cheat_tracker.pop(0)
        else:
            count = 0
            cheat_tracker.pop(0)
    if count == 10:
        root.destroy()



root = tk.Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

janela_w = 290
janela_h = 40
x = w - janela_w - 10
y = 30

cheat_tracker = []
count = 0
close = ['up','up','down','down','left','right', 'left', 'right', 'a','s']

root.title('Você precisa estudar por mais...')
root.geometry(f"{janela_w}x{janela_h}+{x}+{y}")
root.config(background= "#000000")
root.overrideredirect(True)



cronometro_text = tk.Label(root, text = "")
cronometro_text.grid(column=1, row=0)
cronometro_text.config(background= "#000000", fg= "#FFFFFF", font= ("Helvetica", 20, "bold"))

root.bind("<KeyPress>", key_tracker)




update(cheat_tracker)

root.mainloop()
