import os, os.path

MODULE = 'lombok'
VERSION = '0.10.0-RC3'
JDT_JAR='org.eclipse.jdt.core-3.6.0.jar'
LOMBOK_JAR='lombok-' + VERSION + '.jar'
ALTERED_COMMANDS = ['run','test','auto-test','start','precompile','deploy']

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

    if command in ALTERED_COMMANDS:
        args.append('-javaagent:' + os.path.join(app.path, 'lib', LOMBOK_JAR))
        args.append('-Xbootclasspath/a:' + os.path.join(app.path, 'lib', LOMBOK_JAR))
        args.append('-Xbootclasspath/a:' + os.path.join(env["basedir"], 'framework', 'lib', JDT_JAR))


# This will be executed after any command (new, run...)
def after(**kargs):
    command = kargs.get("command")
    app = kargs.get("app")
    args = kargs.get("args")
    env = kargs.get("env")

    if command == "new":
        pass
