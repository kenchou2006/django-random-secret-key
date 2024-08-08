import secrets

def get_random_secret_key():
    return f"django-insecure-{''.join(secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(50))}"

print(get_random_secret_key())
