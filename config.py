import os

from dotenv import load_dotenv 

class Config():
    """Configuration class to manage environment variables."""

    def __init__(self):
        load_dotenv(override=True)

    def __getattr__(self, name):
        try:
            return os.getenv(name.upper())
        
        except KeyError:
            raise AttributeError(f"Config has no attribute '{name}'")
        
config = Config()