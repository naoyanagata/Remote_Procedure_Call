import socket
import sys
import json

def connect_socket(pass_name):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = pass_name
    try:
        sock.connect(server_address)
    except sock.error as err:
        print(err)
        sys.exit(1)
    return sock

def request_and_response_processing(sock):
    try:
        while True:
            req = input("json形式で入力して下さい。：")
            if req == "exit":
                sock.close()
                break
            sock.sendall(req.encode())
            res = sock.recv(128)
            if res:
                json_data = json.loads(res)
                print(json_data)
            else:
                break
    finally:
        sock.close()

def main():
    sock = connect_socket("/tmp/socket_file")
    request_and_response_processing(sock)

if __name__ == "__main__":
    main()