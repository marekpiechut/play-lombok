import os, os.path

MODULE = 'lombok'
VERSION = '1.2.4'

# Commands that are specific to your module

COMMANDS = []

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

def findjar(libDir):
    for name in os.listdir(libDir):
        if name.find('lombok-') == 0:
            return os.path.join(libDir, name)
    return ''

# This will be executed before any command (new, run...)
def before(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")
    lombokJar = findjar(os.path.join(app.path, 'lib'))
    
    args.append('-javaagent:' + lombokJar + '=ECJ')

# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
