# Little Screamer
All in one simple python program that will show image in time duration

By default program will run on every startup of system. To disable it 
go to startup in Roaming folder and remove shortcut

```
POPUP_DURATION = 200 # How long picture will be visible
MIN_TIME = 1 # Minimum time between jumpscares
MAX_TIME = 30 # Maximum time between jumpscares
EXE_DEST_PATH = "" # Path where exe should be stored on victim pc
```
# Pictures
Pictures dont need to be downloaded all that is needed to encode them into base64 and put as strings in "images" variable


# Setup

```python
git clone https://github.com/VinNeu/Little-Screamer.git
cd Little-Screamer
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --windowed --icon "windows_program.ico"  "main.py"
```
