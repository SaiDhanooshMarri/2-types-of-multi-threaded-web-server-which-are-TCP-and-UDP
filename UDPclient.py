import socket
import threading
import time
def udp_client(Siri_dhanoosh, rqsdt_sd):
    uspssd_sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        uspssd_sc.sendto(rqsdt_sd, Siri_dhanoosh)
        bffsz_s = 8192
        fcdsn, _ = uspssd_sc.recvfrom(bffsz_s)
        sdt, _ = uspssd_sc.recvfrom(bffsz_s)
        fcdsn = str(fcdsn)
        fcdsn = fcdsn.split("'")
        fcdsn = fcdsn[1]
        with open(f"C_files/{fcdsn}", "wb") as dimf:
            dimf.write(sdt)
        print(f"Saved the received image as '{fcdsn}'")
    finally:
        uspssd_sc.close()
if __name__ == "__main__":
    Siri_dhanoosh = ("localhost", 8080)
    nscsrd = 30
    
    threads = []
    rqsdt_sd = b"request"
    s_t=time.time()
    for _ in range(nscsrd): 
        thread = threading.Thread(target=udp_client, args=(Siri_dhanoosh, rqsdt_sd))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    de_st=time.time()
    print("Time taken by UDP server is :  ",de_st-s_t)