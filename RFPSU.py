import os
import json
import time

cooldown = 5
empty = ""

while cooldown != 0:
    os.system('cls')
    print("With this program you can unlock the FPS on your Roblox Client.")
    print("Please run this program every time the client updates or the FPS unlocked gets capped again to 60.")
    print(empty)
    print(f"The program will start in {cooldown} seconds!")
    time.sleep(1)
    cooldown = cooldown-1

os.system('cls')
print("With this program you can unlock the FPS on your Roblox Client.")
print("Please run this program every time the client updates or the FPS unlocked gets capped again to 60.")
print(empty)
print(f"Searching for the RobloxPlayerBeta.exe file...")

username = os.environ['USERNAME']
path = ""

base_directory = fr'C:\Users\{username}\AppData\Local\Roblox\Versions'

def find_folders_with_exe(directory):
    folders_with_exe = []

    for root, _, files in os.walk(directory):
        if 'RobloxPlayerBeta.exe' in files:
            folders_with_exe.append(root)

    return folders_with_exe

matching_folders = find_folders_with_exe(base_directory)

if matching_folders:
    for folder in matching_folders:
        os.system('cls')
        print("With this program you can unlock the FPS on your Roblox Client.")
        print("Please run this program every time the client updates or the FPS unlocked gets capped again to 60.")
        print(empty)
        print(f"Injecting ClientAppSettings.json...")
else:
    os.system('cls')
    print("With this program you can unlock the FPS on your Roblox Client.")
    print("Please run this program every time the client updates or the FPS unlocked gets capped again to 60.")
    print(empty)
    print(f"Unable to find RobloxPlayerBeta.exe!")
    time.sleep(999)

if not os.path.exists(fr'{folder}\ClientSettings'):
    os.makedirs(fr'{folder}\ClientSettings')

if not os.path.exists(fr'{folder}\ClientSettings\ClientAppSettings.json'):
    with open(f"{folder}\ClientSettings\ClientAppSettings.json", "w") as file:
        pass

jsonfile = f"{folder}\ClientSettings\ClientAppSettings.json"

data = {
    "DFIntTaskSchedulerTargetFps": 999
}
with open(jsonfile, "w") as json_file:
    json.dump(data, json_file, indent=4)

os.system('cls')
print("With this program you can unlock the FPS on your Roblox Client.")
print("Please run this program every time the client updates or the FPS unlocked gets capped again to 60.")
print(empty)
print(f"Injected! Have fun!")
time.sleep(999)