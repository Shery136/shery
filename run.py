import os, platform, time, pycurl
os.system('clear')
print('checking updates')
os.system('git pull')
print('first allow permations (y)')
os.system('termux-setup-storage')
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Your Device Support This Tool")
    from mm import menu___
    menu___()
elif bit == '32bit':
    print("\n\x1b[1;92m Your Device Not Support This Tool")
