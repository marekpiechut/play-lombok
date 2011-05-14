# Here you can create play commands that are specific to the module, and extend existing commands

MODULE = 'play-lombok'
VERSION = '0.10.0-BETA2'
JDT_JAR='org.eclipse.jdt.core-3.6.0.jar'

# Commands that are specific to your module

COMMANDS = []

def execute(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")


# This will be executed before any command (new, run...)
def before(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")
	
    if command == 'run' or command == 'test' or command == 'auto-test' or command == 'start':
        args.append('-javaagent:' + env["basedir"] + '/modules/' + MODULE + '-' + VERSION + '/lib/lombok-0.10.0-BETA2.jar')
        args.append('-Xbootclasspath/a:' + env["basedir"] + '/modules/' + MODULE + '-' + VERSION + '/lib/lombok-0.10.0-BETA2.jar')
        args.append('-Xbootclasspath/a:' + env["basedir"] + '/framework/lib/' + JDT_JAR)


# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
