from pystyle import Colors, Colorate
import webbrowser
import platform
import ctypes
import os

def Cleaner():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    
def Title(title):
    titlebytes = title.encode('cp1252')
    ctypes.windll.kernel32.SetConsoleTitleA(titlebytes)
    
def Menu():
    menu = r"""
 __          ___       _____            _____    _____      _       _               
 \ \        / (_)     |  __ \     /\   |  __ \  |  __ \    | |     | |              
  \ \  /\  / / _ _ __ | |__) |   /  \  | |__) | | |__) |_ _| |_ ___| |__   ___ _ __ 
   \ \/  \/ / | | '_ \|  _  /   / /\ \ |  _  /  |  ___/ _` | __/ __| '_ \ / _ \ '__|
    \  /\  /  | | | | | | \ \  / ____ \| | \ \  | |  | (_| | || (__| | | |  __/ |   
     \/  \/   |_|_| |_|_|  \_\/_/    \_\_|  \_\ |_|   \__,_|\__\___|_| |_|\___|_|   

    
    1. Start Patching
    2. Open 7-Zip Website (Choose quality)
    3. Exit
    """
    print(Colorate.Vertical(Colors.red_to_yellow, menu))

def patcher():
    content = (
        "RAR registration data\n"
        "WinRAR\n"
        "Unlimited Company License\n"
        "UID=4b914fb772c8376bf571\n"
        "6412212250f5711ad072cf351cfa39e2851192daf8a362681bbb1d\n"
        "cd48da1d14d995f0bbf960fce6cb5ffde62890079861be57638717\n"
        "7131ced835ed65cc743d9777f2ea71a8e32c7e593cf66794343565\n"
        "b41bcf56929486b8bcdac33d50ecf773996052598f1f556defffbd\n"
        "982fbe71e93df6b6346c37a3890f3c7edc65d7f5455470d13d1190\n"
        "6e6fb824bcf25f155547b5fc41901ad58c0992f570be1cf5608ba9\n"
        "aef69d48c864bcd72d15163897773d314187f6a9af350808719796"
    )
    HomeDirectory = os.path.expanduser("~")
    WinRARDir = os.path.join(HomeDirectory, "AppData", "Roaming", "WinRAR")
    if not os.path.exists(WinRARDir):
        os.makedirs(WinRARDir)

    rarreg_key_path = os.path.join(WinRARDir, "rarreg.key")

    with open(rarreg_key_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"'rarreg.key' has been created and patched at: {rarreg_key_path}")

def main():
    while True:
        Cleaner()
        Menu()
        Title("WinRAR Patcher")
        choice = input(Colorate.Horizontal(Colors.red_to_yellow, "Select an option (1-3): "))
        if choice == '1':
            patcher()
            print(Colorate.Horizontal(Colors.green_to_cyan, "Patch applied successfully!"))
        elif choice == '2':
            webbrowser.open("https://www.7-zip.org/")
            print(Colorate.Horizontal(Colors.yellow_to_red, "Opening 7-Zip website..."))
        elif choice == '3':
            print(Colorate.Horizontal(Colors.red_to_black, "Exiting the program."))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice. Please select a valid option."))
        
        input(Colorate.Horizontal(Colors.blue_to_purple, "Press Enter to continue..."))

if __name__ == "__main__":
    main()
