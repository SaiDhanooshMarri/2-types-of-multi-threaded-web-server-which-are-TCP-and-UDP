import socket
import threading    
import time
def tcp_client(Siri_dhanoosh,rqsdt_sd):
    dhanoosh_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        dhanoosh_t.connect(Siri_dhanoosh)
        dfms = dhanoosh_t.recv(1024).decode()
        sdt = dhanoosh_t.recv(8192)
        with open(f"C_files/{dfms}", "wb") as dimf:
            dimf.write(sdt)
        print(f"Saved the received image as '{dfms}'")
    except Exception as fd:
        print(f"Error: {fd}")
    finally:
        dhanoosh_t.close()

if __name__ == "__main__":
    Siri_dhanoosh = ("localhost", 8080)
    nscsrd = 30
    threads = []
    rqsdt_sd = b"request"
    d_s=time.time()
    for _ in range(nscsrd): 
        thread = threading.Thread(target=tcp_client, args=(Siri_dhanoosh,rqsdt_sd))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    de_st=time.time()
    print("Time taken by TCP server is :  ",de_st-d_s)
