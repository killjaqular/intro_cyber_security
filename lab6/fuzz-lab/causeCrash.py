# causeCrash.py

"""
Script used to search for vulnerable HTTP protocol fields on the target
"""

from boofuzz import *

def main():

    target_ip = "127.0.0.1"
    start_cmd = ["./webserver", ""]
    procmon   = ProcessMonitor(target_ip, 26002)
    procmon.set_options(start_commands = [start_cmd])
    session   = Session(target = Target(connection = TCPSocketConnection("127.0.0.1", 8888),
                        monitors = [procmon]))
    define_proto(session = session)
    session.fuzz()

def define_proto(session):

    s_initialize (name = "URI")
    s_static     ("Accept-Encoding: ", name = "Method")
    s_delim      (" ", name = "space-1")
    s_string     ("gzip, deflate", name = "gzipLine")
    s_static     ("\r\n", name = "returnNewLine")

    session.connect(s_get("URI"))

if __name__ == "__main__":
    main()
