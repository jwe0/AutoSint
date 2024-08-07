import threading, tls_client, json
from bs4 import BeautifulSoup
from Email.Sites.spoof import Spoof

class Misc:
    def __init__(self) -> None:
        self.session = tls_client.Session()
        self.sites   = {}
        self.prog    = 0
        self.total   = 0

    def load_sites(self):
        with open("Assets/sites.json", "r") as f:
            self.sites = json.load(f)

    def usernameosint(self, username):
        self.load_sites()
        self.heads = {"User-Agent": Spoof().user_agent()}
        results = {}
        def check(url, type, code):
            r = self.session.get(url, headers=self.heads)
            try:
                if type == "status-code":
                    if r.status_code == int(code):
                        results[url] = {"Status" : "Found", "Type" : type, "Code" : code}
                elif type == "site-content":
                    soup = BeautifulSoup(r.text, "html.parser")
                    if code in soup.text:
                        results[url] = {"Status" : "Found", "Type" : type, "Code" : code}
                elif type == "title-content":
                    soup = BeautifulSoup(r.text, "html.parser")
                    title = soup.find("title").text
                    if code in title:
                        results[url] = {"Status" : "Found", "Type" : type, "Code" : code}
            except:
                pass
            self.prog += 1
            
        self.total = len(self.sites) - 1

        for site in self.sites:
            url  = self.sites[site]["url"].format(username)
            type = self.sites[site]["type"]
            code = self.sites[site]["check-value"]
            threading.Thread(target=check, args=(url, type, code)).start()

        while self.prog != self.total:
            pass

        self.prog = 0
        self.total = 0
        return results