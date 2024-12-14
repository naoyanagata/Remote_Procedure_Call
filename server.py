import socket
import os
import json

def create_response(json_data):
    floor = lambda n: int(n)
    sort = lambda str: "".join(sorted(str))

    def execute_function(json_data):
        func = {
            "floor": floor,
            "sort": sort
        }
        return func[json_data["method"]](json_data["params"])
    
    result = execute_function(json_data)
    return '{' + f'"results": "{result}", "result_type": "{type(result)}", "id": {json_data["id"]}' + '}'

def create_socket(pass_name):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server_address = pass_name
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass
    sock.bind(server_address)
    return sock

def socket_into_listen_state(sock):
    sock.listen(1)

def request_processing(sock):
    sockets = {}
    while True:
        connection, address = sock.accept()
        try:
            while True:
                data = connection.recv(128)
                data_str = data.decode("utf-8")
                json_data = json.loads(data_str)
                if str(json_data["id"]) not in sockets:
                    sockets[str(json_data["id"])] = connection
                if data:
                    response = create_response(json_data)
                    sockets[str(json_data["id"])].sendall(response.encode())
                else:
                    break
        finally:
            sockets[str(json_data["id"])].close()

def main():
    sock = create_socket("/tmp/socket_file")
    socket_into_listen_state(sock)
    request_processing(sock)

if __name__ == "__main__":
    main()