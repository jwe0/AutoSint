import json, random, string, os
from Modules.ip import Ip
from Modules.phone import Phone
from Modules.email import Email
from Modules.misc import Misc
from Modules.people_searcher import People

class Main:
    def __init__(self):
        self.ip     = Ip()
        self.phone  = Phone()
        self.people = People()
        self.email  = Email()
        self.misc   = Misc()
        self.paste  = {}
        self.name   = None

    def art(self):
        ascii_art = """
    _         _       ____  _       _   
   / \  _   _| |_ ___/ ___|(_)_ __ | |_ 
  / _ \| | | | __/ _ \___ \| | '_ \| __|
 / ___ \ |_| | || (_) |__) | | | | | |_ 
/_/   \_\__,_|\__\___/____/|_|_| |_|\__|
                       
/jwe0 @ Invictus 2024
"""

        print(ascii_art)

    def check_dump_dir(self):
        if not os.path.exists("Dumps"):
            os.mkdir("Dumps")

    def dump(self):
        self.check_dump_dir()
        with open("Dumps/{}.json".format(self.name), "w") as f:
            json.dump(self.paste, f, indent=4)

    def main(self):
        name  = input("[>] Name     :  ")
        uname = input("[>] Username :  ")
        phone = input("[>] Phone    :  ")
        email = input("[>] Email    :  ")
        age   = input("[>] Age      :  ")
        ip    = input("[>] IP       :  ")

        if name:
            self.paste["Name"] = name
        if age:
            self.paste["Age"] = age
        if phone:
            mobile = self.phone.phonelookup(phone)
            if mobile[0]:
                self.paste["Phone"] = phone
                self.paste["Phone"] = mobile[1]
        if email:
            email_paste = self.paste["Email"] = {}
            scan = self.email.site_check(email)
            if scan[0]:
                email_paste["Email"] = email
                email_paste["Site"] = scan[1]
        if ip:
            ip_paste = self.paste["Ip"] = {}
            data = self.ip.iplookup(ip)
            rdns = self.ip.reversedns(ip)
            port = self.ip.portscan(ip)
            if data[0]:
                ip_paste["Iplookup"] = data[1]
            if rdns:
                ip_paste["Reverse DNS"] = rdns[1]
            if port:
                ip_paste["Port scan"] = port[1]
        if uname:
            result = self.misc.usernameosint(uname)
            if result:
                self.paste["Uname"] = uname
                self.paste["Username"] = result
        if self.paste:
            self.name = self.paste.get("Uname") if "Uname" in self.paste else self.paste.get("Name") if "Name" in self.paste else "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
            print("[>] Dumped to {}.json".format(self.name))

        self.dump()

if __name__ == "__main__":
    main = Main()
    main.art()
    main.main()