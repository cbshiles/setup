def readLines(fname):
    with open(fname) as f:
        return f.readlines()

config_file = 'boh/core.conf' 
#configs split each line @ the first = sign

conf = {}    
for line in readLines(config_file):
    pos = line.find('=')
    if (pos > 0):
        conf[line[0 : pos].strip()] = line[pos+1:].strip()
    elif line.strip():
        conf[line.strip()] = True

def confirm(ques):
    print(ques)
    res = input('->').lower()
    return res == 'y' or res == 'yes'

import subprocess

exec(open("boh/"+conf['engine']).read())

def runCmd(cmd):
    if cmd[0] in deb:
        if not deb[cmd[0]](cmd[1:]):
            raise OSError('Command failed')
    else:
        raise SyntaxError('Not familiar with command '+cmd[0])

def run(fl):
    if confirm( 'Are you sure you want to run file '+fl+'?'):
        count = 1
        try:
            for line in readLines(fl):
                line = line.strip()
                if line and line[0] != '#':
                    runCmd(line.split())
                count += 1
        except SyntaxError as err:
            print ('Error on line '+str(count))
            print (err)
            quit()
        except OSError as err:
            print ('Error on line '+str(count))
            print (err)
            quit()

run('cmds.txt')

for k, v in conf.items():
    print (type(v) == type(True))#(k+" ~ "+v)
