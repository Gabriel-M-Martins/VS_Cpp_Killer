# Visual Studio C++ Killer
This is a simple python script that finds all processes that Visual Studio spawns when jumping to definitions, searching etc and then kills them (the process name is `vcpkgsrv.exe`).

I have also provided an example of the `.bat` that I use to run this script from anywhere on my machine. Just place it on your environment variables if on Windows, which you probably are.

## How to use
1. Create a python venv:
   - `python -m venv venv`
3. Activate the venv:
  - If using PowerShell: `.venv\Scripts\Activate.ps1`
  - If using CMD: `.\venv\Scripts\Activate`
4. Install requirements.txt:
  - Call `pip install -r requirements.txt`

Now everything is setup and you can run the script. I recommend setting up the `.bat` aswell but I will leave you to that.
