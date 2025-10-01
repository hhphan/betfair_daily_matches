import os

class Config:
    @staticmethod
    def _env_vars():
        return {
            "USERNAME": os.getenv("BF_USERNAME"),
            "PASSWORD": os.getenv("BF_PASSWORD"),
            "APP_KEY":   os.getenv("BF_APP_KEY"),
            "CERTS":     os.getenv("BF_CERT_DIR"),
        }

    @classmethod
    def validate(cls):
        env = cls._env_vars()
        missing = [key for key, value in env.items() if not value]
        if missing:
            raise ValueError(f"Missing required environment variables: {missing}")
        return True
