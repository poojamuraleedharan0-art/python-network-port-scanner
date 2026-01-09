import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

target = "127.0.0.1"

print(f"Scanning target: {target}\n")

for port in range(1, 1025):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)


    if sock.connect_ex((target, port)) == 0:
        service = COMMON_PORTS.get(port, "Unknown")
        print(f"[OPEN] Port {port} -> {service}")


    sock.close()
