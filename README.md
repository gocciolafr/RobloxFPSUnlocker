# RobloxFPSUnlocker
With this simple program you can unlock the FPS for your Roblox client in just 2 clicks!

![](https://img.shields.io/github/downloads/JustKleo/RobloxFPSUnlocker/total)
## Archived
As for 27/02/2025,

This project is archived because Roblox added a feature to change the FPS up to 240. You can use that feature instead, this project doesn't work anymore.
You can also use [Bloxstrap](https://bloxstrap.org/) to change the FPS cap.
## How to use
1. Install the `RFPSU.exe` file under [releases page](https://github.com/JustKleo/RobloxFPSUnlocker/releases "releases page")
2. Run it
	- If Windows takes that file as "dangerus" just click on "more info" and "run anyway".
	- You can see the source code of the program at the repo files

## What happens?
The program automatically creates a `ClientSettings` folder and a `ClientAppSettings.json` file inside it (if doesn't exist) and put the value to set the max FPS for your Roblox Client.

## Manual installation
If you still don't trust this program, here's the method to do the same thing the app does manually:
1. Go to your Roblox version files
	- It can be `C:\Users\YourUsername\AppData\Local\Roblox\Versions`
2. Go to the folder where contains the `RobloxPlayerBeta.exe` file
3. Go to the folder `ClientSettings` (create it if it doesn't exist)
4. Go to the file `ClientAppSettings.json` (create it if it doesn't exist)
5. On the `ClientAppSettings.json` file replace the file with this content:
```json
{
    "DFIntTaskSchedulerTargetFps": 999
}
```
6. Save the file

> *Note that you need to do the same thing everytime a new Roblox version is released or the Client gets capped again to 60 fps*

## FAQ
- Can I trust this file?
	- Yes! If you want, you can see the source code of the program at the files of the repo
- I see 60 fps!
	- Run the program again and it shold be unlocked again
