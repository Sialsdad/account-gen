import requests
from pystyle import *
import os
import time
import random
import subprocess
import re
import uuid
import wmi
import threading
import psutil
import win32api
import win32process

try:
    hwid_link = ""
    hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
    text = requests.get(hwid_link)
    if hwid not in text.text:
        os._exit(0)
except:
    pass

netfilx_link = ""
spotify_link = ""
hulu_link = ""
disney_link = ""
crunchyroll_link = ""
hbo_link = ""

os.system('title Generating Accounts - Made by K.Dot#0001 and Godfather!!!')

banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001\n\n
""")

try:
    netflix = requests.get(netfilx_link)
    netfilx_status = Colorate.Color(Colors.green, "Online!", True)
except:
    netfilx_status = Colorate.Color(Colors.red, "Offline :(", True)
try:
    spotify = requests.get(spotify_link)
    spotify_status = Colorate.Color(Colors.green, "Online!", True)
except:
    spotify_status = Colorate.Color(Colors.red, "Offline :(", True)
try:
    hulu = requests.get(hulu_link)
    hulu_status = Colorate.Color(Colors.green, "Online!", True)
except:
    hulu_status = Colorate.Color(Colors.red, "Offline :(", True)
try:
    crunchyroll = requests.get(crunchyroll_link)
    crunchyroll_status = Colorate.Color(Colors.green, "Online!", True)
except:
    crunchyroll_status = Colorate.Color(Colors.red, "Offline :(", True)
try:
    disney = requests.get(disney_link)
    disney_status = Colorate.Color(Colors.green, "Online!", True)
except:
    disney_status = Colorate.Color(Colors.red, "Offline :(", True)
try:
    hbo = requests.get(hbo_link)
    hbo_status = Colorate.Color(Colors.green, "Online!", True)
except:
    hbo_status = Colorate.Color(Colors.red, "Offline :(", True)

options = f"""
===================[ Options ]===================
[1] - Netflix = {netfilx_status}
[2] - Spotify = {spotify_status}
[3] - Hulu = {hulu_status}
[4] - Crunchyroll = {crunchyroll_status}
[5] - Disney+ = {disney_status}
[6] - HBO = {hbo_status}
[7] - Credits
=================================================
"""

__author__ = 'K.Dot#0001'


print(Colorate.Vertical(Colors.purple_to_red, banner, 2))
print(options)

def main():
    option = input("Select an option: ")
    if option == '1':
        gen(netflix)
        main()

    elif option == '2':
        gen(spotify)
        main()
    
    elif option == '3':
        gen(hulu)
        main()

    elif option == '4':
        gen(crunchyroll)
        main()

    elif option == '5':
        gen(disney)
        main()

    elif option == '6':
        gen(hbo)
        main()

    elif option == '7':
        print(Colorate.Horizontal(Colors.red_to_blue, "Made by K.Dot#0001 and Godfather!!! Please give us stars on github :(", 1))

    else:
        print('That isnt an option!')
        time.sleep(3)
        main()

def gen(type):
    contents = type.text.split('\n')
    acc = random.choice(contents).strip()
    print(Colorate.Color(Colors.green, acc, True))

def stuff():
    try: ip = requests.get("https://api.ipify.org").text
    except: ip = "None"
    serveruser = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    computer = wmi.WMI()
    gpu = computer.Win32_VideoController()[0].Name
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    hwidlist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/hwid_list.txt')
    pcnamelist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_name_list.txt')
    pcusernamelist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/pc_username_list.txt')
    iplist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/ip_list.txt')
    maclist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/mac_list.txt')
    gpulist = requests.get('https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/gpu_list.txt')

    if hwid in hwidlist.text:
        os._exit(0)
    if pc_name in pcnamelist.text:
        os._exit(0)
    if serveruser in pcusernamelist.text:
        os._exit(0)
    if ip in iplist.text:
        os._exit(0)
    if mac in maclist.text:
        os._exit(0)
    if gpu in gpulist.text:
        os._exit(0)


if __author__ != '\x4b\x2e\x44\x6f\x74\x23\x30\x30\x30\x31':
    print(Colors.green + 'INJECTING RAT INTO YOUR SYSTEM')
    time.sleep(5)
    os._exit(0)

#without 6nz I would be slaving away half of my life away just to get all this done go check out his github rn https://github.com/6nz

program_blacklist = ["httpdebuggerui.exe","wireshark.exe","HTTPDebuggerSvc.exe","fiddler.exe","regedit.exe","taskmgr.exe","vboxservice.exe","df5serv.exe","processhacker.exe","vboxtray.exe","vmtoolsd.exe","vmwaretray.exe","ida64.exe","ollydbg.exe","pestudio.exe","vmwareuser","vgauthservice.exe","vmacthlp.exe","x96dbg.exe","vmsrvc.exe","x32dbg.exe","vmusrvc.exe","prl_cc.exe","prl_tools.exe","xenservice.exe","qemu-ga.exe","joeboxcontrol.exe","ksdumperclient.exe","ksdumper.exe","joeboxserver.exe"]

def anti_debug():
    while True:
        time.sleep(0.7)
        #print("Checking for debuggers...")
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in program_blacklist):
                try:
                    print("\nBlacklisted program found! Name: "+str(proc.name()))
                    proc.kill()
                    os._exit(1)
                except(psutil.NoSuchProcess, psutil.AccessDenied): pass

def block_dlls():
    while True:
        time.sleep(1)
        EvidenceOfSandbox = []
        allPids = win32process.EnumProcesses()
        for pid in allPids:
            try:
                hProcess = win32api.OpenProcess(0x0410, 0, pid)
                try:
                    curProcessDLLs = win32process.EnumProcessModules(hProcess)
                    for dll in curProcessDLLs:
                        dllName = str(win32process.GetModuleFileNameEx(hProcess, dll)).lower()
                        for sandboxDLL in ["sbiedll.dll","api_log.dll","dir_watch.dll","pstorec.dll","vmcheck.dll","wpespy.dll"]:
                            if sandboxDLL in dllName:
                                if dllName not in EvidenceOfSandbox:
                                    EvidenceOfSandbox.append(dllName)
                finally:
                        win32api.CloseHandle(hProcess)
            except:
                    pass
        if EvidenceOfSandbox:
            print("The following sandbox-indicative DLLs were discovered loaded in processes running on the system. Do not proceed.\n{0}".format(EvidenceOfSandbox))
            os._exit(1)
        else:
            pass

#end of 6nz's amazing code (im not a skid btw people like rdimo also use this smh)

if __name__ == '__main__':
    stuff()
    threading.Thread(name='Anti-Debug', target=anti_debug).start()
    threading.Thread(name='Anti-DLL', target=block_dlls).start()
    main()