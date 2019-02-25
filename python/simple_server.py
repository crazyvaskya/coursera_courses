import asyncio


def run_server(host, port):
    _main(host=host, port=port)


class ClientServerProtocol(asyncio.Protocol):

    data = {}

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def get_key_data(cls, key):
        res = ""
        for i in cls.data[key]:
            res += f"{key} {i[0]} {i[1]}\n"
        return res

    def process_data(cls, decoded_data):
        command = decoded_data.split()
        if command[0] not in["put", "get"]:
            return"error\nwrong command\n\n"
        if command[0] == "put":
            if command[1] not in cls.data:
                cls.data[command[1]] = []
            cls.data[command[1]] = [tup for tup in cls.data[
                command[1]]
                if command[3] != tup[1]]
            cls.data[command[1]].append((command[2], command[3]))
            return "ok\n\n"
        if command[0] == "get":
            res = "ok\n"
            if command[1] == "*":
                for key in cls.data:
                    res += cls.get_key_data(key)
            else:
                if command[1] in cls.data:
                    res += cls.get_key_data(command[1])
            res += "\n"
            return res


def _main(host='127.0.0.1', port=8888):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        '127.0.0.1', 8888
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    _main()
