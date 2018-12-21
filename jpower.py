from colorama import Fore, Style, init
import json
import sys
import os

#colors
cRed = Style.BRIGHT + Fore.RED
cDefault = Style.RESET_ALL
cGreen = Style.BRIGHT + Fore.GREEN
cYellow = Style.BRIGHT + Fore.YELLOW

sourceFilePath =''
setTo =''
data = {}
args = sys.argv
args.pop(0)
foundString=''
recursive =0
toPop =[]
postHook='powerline-daemon --replace'

#show recursive
def formatData(t,s):
    if not isinstance(t,dict) and not isinstance(t,list):
        print(cGreen+":"+str(t) ,end='')
    else:
        for key in t:
            print(cDefault + '\n' + "> "*s+str(key), end='')
            if not isinstance(t,list):
                formatData(t[key],s+1)


#parse arguments 
for i in range(len(args)):
    if args[i].startswith('--'):
        if args[i] == '--r':
            recursive = 1
            toPop.append(i)
    elif args[i].startswith('-'):
        args[i] = args[i].replace('-','',1)
    elif '.json' in args[i]:
        sourceFilePath = args[i]
        toPop.append(i)
        i = i-1
    else:
        setTo = args[i]
        args.pop(i)

toPop = sorted(toPop, reverse=True)

for i  in range(len(toPop)):
    args.pop(toPop[i])

#open file
if sourceFilePath == '':
    print('please provide .json file')
else:
    with open(sourceFilePath, 'r') as read_file:
        data = json.load(read_file)
    
    #print information
    print(sourceFilePath)
    print(args)
    print('depth: ' + str(len(args)))
    print()
    
    #show objects under given path
    elem=data
    for i in range(len(args)):
        elem=elem[args[i]]
    
    if recursive:
        #recursive
        formatData(elem,0)
    else:
        #only actual level
        for e in elem:
            if len(e) == 1:
                foundString = 1
            else:
                print(e)
    
    print('')
    if foundString:
        print(cGreen + elem)
        if setTo != '':
            #change data to input
            if len(args) == 3:
                print(cDefault + 'change ' + data[args[0]][args[1]][args[2]] + ' to ' + setTo)
                #backup actual config
                os.system('cp ' + sourceFilePath + ' ' + sourceFilePath + '.old')
                data[args[0]][args[1]][args[2]] = setTo
                #write to file
                with open(sourceFilePath, 'w') as write_file:
                    json.dump(data, 
                            write_file,
                            ensure_ascii = False,
                            sort_keys = True,
                            indent = 4 )
                os.system(postHook)
