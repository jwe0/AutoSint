from Email.Sites.spoof import Spoof

class replit:
    def __init__(self) -> None:
        pass

    def headers(self):
        headers = {
            "User-Agent": Spoof().user_agent(),
            "X-Requested-With": "XMLHttpRequest",
            "Referer" : "https://replit.com/signup"
        }
        return headers
    
    def check(self, session, email):
        data = {"email": email}
        r = session.post("https://replit.com/data/user/exists", headers=self.headers(), data=data)
        if r.json().get("exists"):
            return True, r.status_code, "exists", r.json().get("exists")
        return False, r.status_code, "exists", r.json().get("exists")