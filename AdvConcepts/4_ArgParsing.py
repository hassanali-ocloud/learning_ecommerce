import sys
import getopt

opts, args = getopt.getopt(sys.argv[1:], "f:m:a:p:", ["fileName", "message", "address", "port"])

for opt, arg in opts:
    if opt == "-f":
        fileName = arg
    elif opt == "-m":
        message = arg
    elif opt == "-a":
        address = arg
    elif opt == "-p":
        port = arg

with open(fileName, "w") as file:
    file.write(f"Writing this message: {message} and sending to {address}:{port}")