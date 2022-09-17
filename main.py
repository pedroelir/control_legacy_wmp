from pywinauto.application import Application, WindowSpecification

app: Application = Application("uia")
app.start(r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe")
# When First time launching WMP it will launch the setup_wm.exe
app.connect(path=r"C:\Program Files (x86)\Windows Media Player\setup_wm.exe")
print(app)

wmp: WindowSpecification = app["Windows Media Player"]
# wmp: WindowSpecification = app["Untitled - Notepad"]

wmp.print_control_identifiers()
print(wmp.Finish.is_enabled())
wmp.Recommendedsettings.click()
print(wmp.Finish.is_enabled())
wmp.Finish.click()
# wmp.child_window(title="Close", control_type="Button").click()
# rec.click()
print("Done")
