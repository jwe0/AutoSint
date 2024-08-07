from bs4 import BeautifulSoup
from Email.Sites.spoof import Spoof

class redtube:
    def __init__(self) -> None:
        pass

    def headers(self):
        headers = {
            'User-Agent': Spoof().user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US;q=0.5,en;q=0.3',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://redtube.com',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

        return headers

    def get_token(self):
        r = self.session.get("https://redtube.com/register", headers=self.headers())
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
        r = self.session.post("ttps://www.redtube.com/user/create_account_check", headers=self.headers(), params={"token": token}, data=data)
        if r.json().get("error_message") == "Email has been taken.":
            return True, r.status_code, "error_message", r.json().get("error_message")
        return False, r.status_code, "error_message", r.json().get("error_message")