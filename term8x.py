#!/usr/bin/python

############################################################

name = "bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# '"
continuePrompt = "\nClick [Return] to continue"

############################################################

import sys
import argparse
import os
import subprocess
import signal
import time

############################################################

class bcolors:
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    purple = '\033[95m'
    white = '\033[0m'
    cyan = '\033[36m'
    orange = '\033[40m'
    black = '\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'

############################################################

def clearScr():
    os.system('clear')

def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)

def nmapp():
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print(bcolors.red + "######################################## ")
    print(" ")
    print(bcolors.white + "Welcome to the NMAP Section of Term8x!")
    print(" ")
    print(bcolors.white + "IP Address You Want To Scan: " + bcolors.red + nmap)
    print(" ")
    print(bcolors.red + "[1]"+ bcolors.blue + "   Scan Ip (No Verbosity Lvl)")
    print(bcolors.red + "[2]"+ bcolors.blue + "   Scan Ip (Verbosity 1)")
    print(bcolors.red + "[3]"+ bcolors.blue + "   Scan Ip (Verbosity 2)")
    print(bcolors.red + "[4]"+ bcolors.blue + "   Scan Network for Active Computer")
    print(bcolors.red + "[5]"+ bcolors.blue + "   Perform a Fast Scan")
    print(bcolors.red + "[6]"+ bcolors.blue + "   Show Open Port")
    print(bcolors.red + "[7]"+ bcolors.blue + "   OS Detection")
    print(bcolors.red + "[8]"+ bcolors.blue + "   Sevice Version Detection")
    print(bcolors.red + "[9]"+ bcolors.blue + "   Firewall Detection")
    print(bcolors.red + "[10]"+ bcolors.blue + "  No Ping (Disable Host)")                 
    print(bcolors.red + "[11]"+ bcolors.blue + "  Stealthy Scan")
    print(bcolors.red + "[12]"+ bcolors.blue + "  Disable DNS Resolution")
    print(bcolors.red + "[13]"+ bcolors.blue + "  Determine Support IP Protocols")
    print(bcolors.red + "[14]"+ bcolors.blue + "  Scan for all TCP Ports")
    print(bcolors.red + "[15]"+ bcolors.blue + "  Scan for particular TCP Ports (Type: 80)")
    print(bcolors.red + "[16]"+ bcolors.blue + "  Scan for all UDP Ports")
    print(bcolors.red + "[17]"+ bcolors.blue + "  Scan for particular UDP Ports (Type: 53)")
    print(bcolors.red + "[99]"+ bcolors.blue + "  Back to Main Menu")
    print(" ")
    print(bcolors.red + "######################################## ")
    print(" ")
    na = input(bcolors.green + 'lin8x@android' + bcolors.white + ':~# ')    
    if na == '1':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '2':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -v ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '3':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -vv ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '4':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sn ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '5':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -F ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '6':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -open ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '7':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -O ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '8':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sV ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '9':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sA ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '10':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -Pn ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '11':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sS ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '12':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -n ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '13':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sO ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '14':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sT ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '15':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -p T:80 ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '16':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -sU ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '17':
        clearScr()
        clearScr()
        clearScr()
        os.system('nmap -p U:53 ' + nmap)
        print(" ")
        answernmap = input("Press Any Key to Go Back to the Nmap Menu")
        nmapp()
    if na == '99':
        subprocess.call(["python3", "term8x.py"])

def hd():
    clearScr()
    clearScr()
    clearScr()
    print(bcolors.red + "######################################## ")
    print(" ")
    print(bcolors.white + "Welcome to Hydra on Term8x")
    print(" ")


############################################################

clearScr()
clearScr()
clearScr()
print(bcolors.red + "######################################## ")

print(" ")

print(bcolors.red + "I AM NOT RESPONSIBLE FOR ANY ILLGAL ACTIONS YOU MAY DO WITH THIS TOOL")
print(" ")
print(bcolors.red + "[Type python3 term8x.py to start back up this tool when you need to]")
print(bcolors.green + """
  _____                            ___           
 |_   _|   ___      _ _   _ __    ( _ )   __ __  
   | |    / -_)    | '_| | '  \   / _ \   \ \ /  
  _|_|_   \___|   _|_|_  |_|_|_|  \___/   /_\_\  """) 
print(bcolors.yellow + """_|+++++|_|+++++|_|+++++|_|+++++|_|+++++|_|+++++| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'  
""")


print(bcolors.yellow + " ---------------------------- ")
print(bcolors.yellow + " Developed By the Lin8x Team")
print(bcolors.yellow + " ---------------------------- ") 
print(bcolors.red + " [1] " + bcolors.blue + " Nmap (IP Scanning) ")
print(bcolors.red + " [97] " + bcolors.blue + "Learn Hacking ") 
print(bcolors.red + " [98] " + bcolors.blue + "Credits ")
print(bcolors.red + " [99] " + bcolors.blue + "Exit (Or Press CTRL + C)")

print(" ")

print(bcolors.red + "######################################## ")

print(" ")

############################################################

answer = input(bcolors.green + 'lin8x@android' + bcolors.white + ':~# ')

if answer == '1':
    nmap = input(bcolors.white + 'Please Type the IP Address you want to scan: ')
    nmapp()
if answer == '97':
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print(bcolors.red + "######################################## ")
    print(" ")
    print(bcolors.yellow + "Feel free to learn hacking at: http://www.hackerhighschool.org")
    print(" ")
    print(bcolors.red + "[99]" + bcolors.blue + " Back to Menu ")
    print(" ")
    print(bcolors.red + "######################################## ")
    print(" ")
    six = input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if six == '99':
        subprocess.call(["python", "term8x.py"])
    else:
        subprocess.call(["python", "term8x.py"])

if answer == '98':
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    print(bcolors.red + "######################################## ")
    print(" ")
    print(bcolors.white + "          " + bcolors.underline + "Developer List")
    print(bcolors.white + bcolors.bold + "[Founder & Dev]       AnonymousContent")
    print(bcolors.white + bcolors.bold + "[Developer]           iByNiki_")
    print(bcolors.white + bcolors.bold + "[Developer]           AnonymousBen")
    print(bcolors.white + bcolors.bold + "[Supporter]           Devore07")
    print(bcolors.white + bcolors.bold + "[Supporter]           FCCAGut")
    print(" ")
 
    print(bcolors.red + "[99]" + bcolors.blue + " Back to Menu")    
    
    print(" ")

    print(bcolors.red + "######################################## ")

    cr = input(bcolors.bold + bcolors.green + 'lin8x@kali' + bcolors.white + ':~# ')
    if cr == '99':
        subprocess.call(["python", "term8x.py"])
    else:
        subprocess.call(["python", "term8x.py"])

if answer == '99':
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    clearScr()
    os.kill(os.getppid(), signal.SIGHUP)



