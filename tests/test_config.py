import pytest
from betfair_app.config import Config

def test_missing_env(monkeypatch):
    for v in ['BF_USERNAME','BF_PASSWORD','BF_APP_KEY','BF_CERT_DIR']:
        monkeypatch.delenv(v, raising=False)
    with pytest.raises(ValueError):
        Config.validate()

def test_all_env(monkeypatch):
    for k,v in [('BF_USERNAME','u'),('BF_PASSWORD','p'),('BF_APP_KEY','k'),('BF_CERT_DIR','c')]:
        monkeypatch.setenv(k, v)
    assert Config.validate() is True
