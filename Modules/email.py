from Email.main import Scan

class Email:
    def __init__(self):
        pass
    
    def site_check(self, email):
        scan = Scan()
        return scan.run(email)
    def snusbase_check(self, email):
        ""