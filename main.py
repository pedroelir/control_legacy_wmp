import os
import time
from pywinauto.application import Application, WindowSpecification, ProcessNotFoundError

wmp_exe_path: str = "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
media = f"{os.path.abspath(os.curdir)}\\Wildlife.wmv"
app: Application = Application("uia")
app.start(f"{wmp_exe_path} {media}")

try:
    # When First time launching WMP it will launch the setup_wm.exe
    app.connect(path=r"C:\Program Files (x86)\Windows Media Player\setup_wm.exe")
    wmp: WindowSpecification = app["Windows Media Player"]
    wmp.print_control_identifiers()
    print(wmp.Finish.is_enabled())
    wmp.Recommendedsettings.click()
    print(wmp.Finish.is_enabled())
    wmp.Finish.click()
except ProcessNotFoundError:
    print("Setup WMP not launched maybe WMP was already launched for the first time in this system")


app.connect(path=wmp_exe_path)
wmp: WindowSpecification = app["Now Playing"]
wmp.print_control_identifiers()
wmp.Pause.click()
wmp.print_control_identifiers()
wmp.Play.click()
time.sleep(5)
wmp.Close.click()
print("Done")
