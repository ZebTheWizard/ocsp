import subprocess
import os
import tempfile


def cli(*cmd, **kwargs):
    """Get the stdout, stderr from a command. Commands must be passed in as an array, ie split at the spaces"""
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, input=kwargs.get("stdin", b'\n'))
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')


tmpPaths = {}


def getTempPath(name):
    return tmpPaths.get(name)


def removeTempFile(name):
    try:
        os.remove(getTempPath(name))
        del tmpPaths[name]
    except:
        pass


def makeTempFile(name, content):
    f, path = tempfile.mkstemp()
    tmpPaths[name] = path
    try:
        with os.fdopen(f, 'w') as tmp:
            tmp.write(str(content))
    except:
        pass
    return path


def removeAllTempFiles():
    for key in tmpPaths.keys():
        removeTempFile(key)
