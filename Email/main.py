import threading, tls_client, importlib, os
class Scan:
    def __init__(self) -> None:
        self.taken   = {}
        self.prog    = 0
        self.modules = [file.split(".py")[0] for file in os.listdir("Email/Sites") if file.endswith(".py") and file != "spoof.py"]
        self.session = tls_client.Session()

    def module_check(self, modulename, email):
        check = False
        try:
            module = importlib.import_module(f"Email.Sites.{modulename}")
            module_class = getattr(module, modulename)
            checker = module_class()
            check = checker.check(self.session, email)
            if check[0]:
                # Site, Status, Error, Message
                self.taken[str(modulename.title())] = {"Status": "Taken", "Error": check[2], "Message": check[3]}
        except Exception as e:
            pass
        self.prog += 1
        return check
    
    def run(self, email):
        print(self.modules)
        for module in self.modules:
            threading.Thread(target=self.module_check, args=(module, email)).start()
        while self.prog < len(self.modules):
            pass
        if self.taken:
            return (True, self.taken)
        return (False, self.taken)