import sys

def print_debug(log_line):
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        print(log_line)