from boofuzz import *


def main():
    target_ip="127.0.0.1"
    start_cmd = ['./webserver-1','']
    procmon = ProcessMonitor(target_ip, 26002)
    procmon.set_options(start_commands=[start_cmd])
    session = Session(target=Target(connection=TCPSocketConnection("127.0.0.1", 8888), monitors=[procmon],))
    define_proto(session=session)
    session.fuzz()

def define_proto(session):
    s_initialize(name="URI")
    s_static("GET ", name='Method')
    s_delim(" ", name='space-1')
    s_string("/index.html", name='Request-URI')
    s_static("\r\n", name="Request-Line-CRLF")
    s_static("User-Agent: Mozilla\r\n")
    s_static("Accept-Language: en-US,en;q=0.5\r\n")
    s_static("Accept-Encoding: gzip, deflate\r\n")
    session.connect(s_get("URI"))

if __name__ == "__main__":
    main()
