# causeCrash.py

"""
Script used to search for vulnerable HTTP protocol fields on the target
"""

from boofuzz import *

def main():

    target_ip = "127.0.0.1"
    start_cmd = ["./game", ""]
    procmon   = ProcessMonitor(target_ip, 31689)
    procmon.set_options(start_commands = [start_cmd])
    session   = Session(target = Target(connection = TCPSocketConnection("127.0.0.1", 8888),
                        monitors = [procmon]))
    define_proto(session = session)
    session.fuzz()

def define_proto(session):

    s_initialize (name = "Brute")
    s_string     ("random", name = "gzipLine")

    session.connect(s_get("Brute"))

if __name__ == "__main__":
    main()
