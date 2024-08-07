from Email.Sites.spoof import Spoof

class snapchat:
    def __init__(self) -> None:
        self.session = None

    def headers(self, xsrf, webClientId):
        headers = {
            "Host": "accounts.snapchat.com",
            "User-Agent": Spoof().user_agent(),
            "Accept": "*/*",
            "X-XSRF-TOKEN": xsrf,
            "Accept-Encoding": "gzip, late",
            "Content-Type": "application/json",
            "Connection": "close",
            "Cookie": "xsrf_token=" + xsrf + "; web_client_id=" + webClientId
        }

        return headers
    
    def xsrf(self):
        r = self.session.get("https://accounts.snapchat.com")
        xsrf = r.text.split('data-xsrf="')[1].split('"')[0]
        webClientId = r.text.split('ata-web-client-id="')[1].split('"')[0]

        return xsrf, webClientId
    
    def check(self, session, email):
        self.session = session
        xsrf, webClientId = self.xsrf()
        data = '{"email":' + email + ',"app":"BITMOJI_APP"}'
        r = self.session.post("https://accounts.snapchat.com/accounts/check_email", headers=self.headers(xsrf, webClientId), data=data)
        if r.status_code != 204:
            return True, r.status_code, "204", "Status"
        return True, r.status_code, "204", "Status"