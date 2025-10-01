from betfairlightweight import APIClient
from betfair_app.config import Config

class BetfairClient:
    def __init__(self):
        # Dynamically fetch validated env vars
        env = Config._env_vars()
        Config.validate()
        self.client = APIClient(
            username=env["USERNAME"],
            password=env["PASSWORD"],
            app_key=env["APP_KEY"],
            certs=env["CERTS"],
        )
        self._logged_in = False

    def __enter__(self):
        self.client.login()
        self._logged_in = True
        return self.client

    def __exit__(self, exc_type, exc_value, traceback):
        if self._logged_in:
            self.client.logout()
