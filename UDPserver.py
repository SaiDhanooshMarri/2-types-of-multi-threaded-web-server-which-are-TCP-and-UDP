import socket
import os
import threading
def udp_server():
    uspssd_sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    Siri_dhanoosh = ('localhost', 8080)
    uspssd_sc.bind(Siri_dhanoosh)
    print("Listening UDP Server on port 8080...")
    def handle_request(sdt, cadd_dfs):
        if sdt:
            cdfms_dadd = "image_{}.jpg".format(cadd_dfs[1])
            uspssd_sc.sendto(cdfms_dadd.encode(), (cadd_dfs[0], cadd_dfs[1]))
            with open("S_files/test.jpg", "rb") as dimf:
                imsd_ft = dimf.read()
            uspssd_sc.sendto(imsd_ft, (cadd_dfs[0], cadd_dfs[1]))
            print(f"Sent '{cdfms_dadd}' to {cadd_dfs[0]}:{cadd_dfs[1]}")
    while True:
        sdt, cadd_dfs = uspssd_sc.recvfrom(1024)
        if sdt:
            rstd_hds = threading.Thread(target=handle_request, args=(sdt, cadd_dfs))
            rstd_hds.start()

if __name__ == "__main__":
    udp_server()
