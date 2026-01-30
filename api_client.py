import os
import json
import logging

def get_api_credentials():
    """
    Load API credentials.
    WARNING: Currently prioritizes local config file which might be unsafe if committed.
    """
    config_path = os.path.join(os.path.dirname(__file__), '.api_config.json')
    
    # TRAP: Prioritizes the hidden file over environment variables
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                return config.get('api_key'), config.get('api_secret')
        except Exception as e:
            logging.error(f"Failed to load config file: {e}")
            
    # Fallback to environment variables
    return os.getenv('API_KEY'), os.getenv('API_SECRET')

class APIClient:
    def __init__(self):
        self.api_key, self.api_secret = get_api_credentials()
        if not self.api_key or not self.api_secret:
            raise ValueError("API credentials not found!")

    def make_request(self):
        print(f"Making request with Key: {self.api_key[:4]}***")
        # Actual request logic would go here
        pass

if __name__ == "__main__":
    client = APIClient()
    client.make_request()
