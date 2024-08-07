import requests, socket, threading

class Ip:
    def __init__(self):
        self.curr  = 0

    def iplookup(self, ip):
        data = {}
        api = "https://api.ipapi.is/?q={}".format(ip)
        rqst = requests.get(api)
        for key, value in rqst.json().items():
            if isinstance(value, dict):
                temp = {}
                for k, v in value.items():
                    temp[k] = v
                data[key] = temp
            else:
                data[key] = value
        return (True, data)
    
    def reversedns(self, ip):
        data = socket.gethostbyaddr(ip)
        result = {
            "Domain": data[0],
            "Mx": data[1],
            "Ips": [i for i in data[2]]
        }
        return (True, result)
    def portscan(self, ip):
        open = {}
        ports = [(22, "ssh"), (80, "http"), (443, "https"), (8080, "http"), (8443, "https")]

        def scan(ip, port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port[0]))
            if result == 0:
                open[str(port[0])] = str(port[1])
            self.curr += 1
            sock.close()

        for port in ports:
            threading.Thread(target=scan, args=(ip, port)).start()
        while self.curr < len(ports) - 1:
            pass

        return (True, open)


        