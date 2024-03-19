import winreg as reg

def register_app(extension, app_name, app_path):
    key = reg.HKEY_CURRENT_USER
    path = f"Software\\Classes\\{extension}"

    with reg.OpenKey(key, path, 0, reg.KEY_SET_VALUE) as ext_key:
        reg.SetValue(ext_key, "", reg.REG_SZ, app_name)

    with reg.CreateKey(key, f"Software\\Classes\\{app_name}") as app_key:
        reg.SetValue(app_key, "", reg.REG_SZ, f"{app_name} Document")
        reg.SetValueEx(app_key, "FriendlyTypeName", 0, reg.REG_SZ, f"{app_name} Document")

    with reg.CreateKey(key, f"Software\\Classes\\{app_name}\\shell\\open\\command") as cmd_key:
        reg.SetValue(cmd_key, "", reg.REG_SZ, f'"{app_path}" "%1"')

if __name__ == "__main__":
    app_path = r".\output\viewer.exe"
    app_name = "EmViewerApp"
    extension = ".pes"

    register_app(extension, app_name, app_path)
    print(f"Application {app_name} is registered for extension {extension}.")
