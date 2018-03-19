import time
import socket


class Client:
    def __init__(self, host, port, timeout=None):
        self.sock = socket.create_connection((host, port), timeout=timeout)

    def put(self, key, value, timestamp=None):
        if timestamp is None:
            timestamp = str(int(time.time()))
        else:
            timestamp = str(timestamp)
        value = str(value)
        recv_buf = b""
        try:
            self.sock.sendall(
                f"put {key} {value} {timestamp}\n".encode())
            while not recv_buf.endswith(b"\n\n"):
                recv_buf += self.sock.recv(128)
        except:
            raise ClientError

        recv_buf = recv_buf.decode()
        if recv_buf == "ok\n\n":
            return
        else:
            raise ClientError

    def get(self, key):
        key = str(key)
        recv_buf = b""
        res = {}
        try:
            self.sock.sendall(f"get {key}\n".encode())
            while not recv_buf.endswith(b"\n\n"):
                recv_buf += self.sock.recv(1024)
        except:
            raise ClientError
        recv_buf = recv_buf.decode()
        for line in recv_buf.splitlines():
            if line == 'ok':
                continue
            elif line == 'error':
                raise ClientError
            elif line == '':
                return res
            words = line.split()
            if res.get(words[0]) is None:
                res[words[0]] = [(int(words[2]), float(words[1]))]
            else:
                res[words[0]].append((int(words[2]), float(words[1])))
        for i in res:
            res[i].sort(key=lambda x: x[0])
        return res


class ClientError(Exception):
    pass
