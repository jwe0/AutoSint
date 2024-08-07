from bs4 import BeautifulSoup
from Email.Sites.spoof import Spoof

class pornhub:
    def __init__(self) -> None:
        pass

    def headers(self):
        headers = {
            "User-Agent": Spoof().user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en,en-US;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        return headers

    def get_token(self):
        r = self.session.get("https://www.pornhub.com/signup", headers=self.headers())
        soup = BeautifulSoup(r.text, 'html.parser')
        toe = soup.find(attrs={"name" : "token"}).get("value")
        return toe

    def check(self, session, email):
        self.session = session
        token = self.get_token()
        data = {
            "check_what": "email",
            "email": email,
        }
        r = self.session.post("https://www.pornhub.com/user/create_account_check", headers=self.headers(), params={"token": token}, data=data)
        if r.json().get("error_message") == "Email has been taken.":
            return True, r.status_code, "error_message", r.json().get("error_message")
        return False, r.status_code, "error_message", r.json().get("error_message")
