from betfairlightweight import APIClient
from betfair_app.config import Config

class BetfairClient:
    def __init__(self):
        Config.validate()
        self.client = APIClient(
            username=Config.USERNAME,
            password=Config.PASSWORD,
            app_key=Config.APP_KEY,
            certs=Config.CERTS,
        )
        self._logged_in = False

    def __enter__(self):
        self.client.login()
        self._logged_in = True
        return self.client

    def __exit__(self, exc_type, exc_value, traceback):
        if self._logged_in:
            self.client.logout()
