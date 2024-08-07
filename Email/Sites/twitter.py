from Email.Sites.spoof import Spoof

class twitter:
    def __init__(self) -> None:
        pass
    
    def headers(self):
        headers = {
            "User-Agent": Spoof().user_agent(),
        }
        return headers

    def check(self, session, email):
        params = {"email": email}
        headers = self.headers()
        r = session.get("https://api.twitter.com/i/users/email_available.json", headers=headers, params=params)
        if r.json().get("taken", ""):
            return True , r.status_code, "taken", r.json().get("taken")
        return False, r.status_code, "taken", r.json().get("taken")