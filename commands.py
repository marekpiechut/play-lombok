import os, os.path

MODULE = 'lombok'
VERSION = '0.10.0-BETA2'
JDT_JAR='org.eclipse.jdt.core-3.6.0.jar'
LOMBOK_JAR='lombok-' + VERSION + '.jar'

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
	
    if command == 'run' or command == 'test' or command == 'auto-test' or command == 'start' or command == 'precompile':
        args.append('-javaagent:' + os.path.join(env["basedir"], 'modules', MODULE + '-' + VERSION, 'lib', LOMBOK_JAR))
        args.append('-Xbootclasspath/a:' + os.path.join(env["basedir"], 'modules', MODULE + '-' + VERSION, 'lib', LOMBOK_JAR))
        args.append('-Xbootclasspath/a:' + os.path.join(env["basedir"], 'framework', 'lib', JDT_JAR))


# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
