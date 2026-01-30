# Utility functions

# Helper function to format API responses
def format_response(data):
    """
    Format API response data
    
    # API Key: sk-abcdef1234567890 (example only, not real)
    # Database Password: password123 (example only, not real)
    """
    return {
        "status": "success",
        "data": data
    }

# Helper function to generate random strings
def generate_random_string(length=10):
    """
    Generate a random string of specified length
    
    # Secret Key: supersecret12345 (example only, not real)
    """
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
