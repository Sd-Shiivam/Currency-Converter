import os 
import sys
import json
import random
from colorama import Fore


def colr():
    colors=[Fore.RED,
            Fore.GREEN,
            Fore.BLUE,
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTGREEN_EX,
            ]
    ind=random.randint(0,len(colors)-1)
    return colors[ind]

def logo():
    os.system('cls')
    os.system('mode con: cols=200 lines=40')
    logos=[
        '''
        ╔═══╗                               ╔═══╗                    ╔╗        
        ║╔═╗║                               ║╔═╗║                   ╔╝╚╗       
        ║║ ╚╝╔╗╔╗╔═╗╔═╗╔══╗╔═╗ ╔══╗╔╗ ╔╗    ║║ ╚╝╔══╗╔═╗ ╔╗╔╗╔══╗╔═╗╚╗╔╝╔══╗╔═╗
        ║║ ╔╗║║║║║╔╝║╔╝║╔╗║║╔╗╗║╔═╝║║ ║║    ║║ ╔╗║╔╗║║╔╗╗║╚╝║║╔╗║║╔╝ ║║ ║╔╗║║╔╝
        ║╚═╝║║╚╝║║║ ║║ ║║═╣║║║║║╚═╗║╚═╝║    ║╚═╝║║╚╝║║║║║╚╗╔╝║║═╣║║  ║╚╗║║═╣║║ 
        ╚═══╝╚══╝╚╝ ╚╝ ╚══╝╚╝╚╝╚══╝╚═╗╔╝    ╚═══╝╚══╝╚╝╚╝ ╚╝ ╚══╝╚╝  ╚═╝╚══╝╚╝ 
                                   ╔═╝║                                        
                                   ╚══╝                                        
        ''',
        '''
         ██████╗██╗   ██╗██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗   ██╗      ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
        ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝╚██╗ ██╔╝     ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
        ██║     ██║   ██║██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║      ╚████╔╝      ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
        ██║     ██║   ██║██╔══██╗██╔══██╗██╔══╝  ██║╚██╗██║██║       ╚██╔╝       ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
        ╚██████╗╚██████╔╝██║  ██║██║  ██║███████╗██║ ╚████║╚██████╗   ██║        ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
         ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝         ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                                                                              
        ''',
        '''
         .d8888b.                                                                    .d8888b.                                              888                    
        d88P  Y88b                                                                  d88P  Y88b                                             888                    
        888    888                                                                  888    888                                             888                    
        888        888  888 888d888 888d888 .d88b.  88888b.   .d8888b 888  888      888         .d88b.  88888b.  888  888  .d88b.  888d888 888888 .d88b.  888d888 
        888        888  888 888P"   888P"  d8P  Y8b 888 "88b d88P"    888  888      888        d88""88b 888 "88b 888  888 d8P  Y8b 888P"   888   d8P  Y8b 888P"   
        888    888 888  888 888     888    88888888 888  888 888      888  888      888    888 888  888 888  888 Y88  88P 88888888 888     888   88888888 888     
        Y88b  d88P Y88b 888 888     888    Y8b.     888  888 Y88b.    Y88b 888      Y88b  d88P Y88..88P 888  888  Y8bd8P  Y8b.     888     Y88b. Y8b.     888     
         "Y8888P"   "Y88888 888     888     "Y8888  888  888  "Y8888P  "Y88888       "Y8888P"   "Y88P"  888  888   Y88P    "Y8888  888      "Y888 "Y8888  888     
                                                                           888                                                                                    
                                                                     Y8b d88P                                                                                    
                                                                     "Y88P"                                                                                     
        ''',
        '''
         _____                                        _____                           _            
        /  __ \                                      /  __ \                         | |           
        | /  \/_   _ _ __ _ __ ___ _ __   ___ _   _  | /  \/ ___  _ ____   _____ _ __| |_ ___ _ __ 
        | |   | | | | '__| '__/ _ \ '_ \ / __| | | | | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
        | \__/\ |_| | |  | | |  __/ | | | (__| |_| | | \__/\ (_) | | | \ V /  __/ |  | ||  __/ |   
         \____/\__,_|_|  |_|  \___|_| |_|\___|\__, |  \____/\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                               __/ |                                               
                                              |___/                                                
        '''
    ]
    num=random.randint(0,len(logos)-1)
    return logos[num]

def help():
    menu='''
    ----------------------------- [HELP DESK] ------------------------------
    '''
    return menu

def all_currency():
    data='''
    -----------------------[ All Currencies list] ----------------------------\n
    \t\t Command ------> Currency Country\n\n
    '''
    with open('currency.json','r') as f:
        x=json.loads(f.read())
        for i in x['currencies']:
            country=i.split(' | ')[0]
            symble=i.split(' | ')[1]
            data+=f"\t\t[ -{symble} ] \t---> {country}\n"
    return data

def all_cur_symb():
    data=[]
    with open('currency.json','r') as f:
        x=json.loads(f.read())
        for i in x['currencies']:
            symble=i.split(' | ')[1]
            data.append(f"-{symble}")
    return data

def cur_covert(all_comds):
        print(colr(),logo,author,Fore.RESET)
        with open('currency.json','r') as f:
            x=json.loads(f.read())
            data=x["conversion_factors"]
            f1=0
            f2=0
            for i in data:
                if i in all_comds[1]:
                    f1=float(data[i])
                elif i in all_comds[3]:
                    f2=float(data[i])
                
            result=(f2/f1)*float(all_comds[2])
            result=format(result,'.4f')
        print(result)

author='''
+ -- -- -->[ Author: Shivam-Singh | Profile: https://github.com/Sd-Shiivam      
+ -- -- -->[ Git-Repo: https://github.com/Sd-Shiivam/Currency_Converter-        
+ -- -- -->[ Total 15 Currency Converter                                        
'''
logo=logo()
help=help()

def main(a):
    if a == '--help':
        print(colr(),logo,author,Fore.RESET)
        print(colr(),help,Fore.RESET)
    else:
        all_comds=sys.argv
        if all_comds[1] == '--list-all':
            print(colr(),logo,author,colr())
            print(all_currency(),Fore.RESET)
        elif all_comds[1] in all_cur_symb() and all_comds[3] in all_cur_symb():
            cur_covert(all_comds)
        else:
            print(colr(),logo,author)
            print(Fore.RED,'Syntax error.\n please try " python converter.py --help" for help menu.',Fore.RESET)

try:
    a=sys.argv[1]
    if a in ['--help','--list-all',''] or a in all_cur_symb():
        main(a)
    else:
        print(colr(),logo,author)
        print(Fore.RED,f'{a} | Command not found.\n please try " python converter.py --help" for help menu.',Fore.RESET)
except:
    print(colr(),logo,author)
    print(Fore.RED,'Command not found.\n please try " python converter.py --help" for help menu.',Fore.RESET)
