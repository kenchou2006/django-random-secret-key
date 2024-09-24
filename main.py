import secrets

def get_random_string(allowed_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    return "".join(secrets.choice(allowed_chars) for i in range(50))

def get_random_secret_key():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return f"django-insecure-{get_random_string(chars)}"

print(get_random_secret_key())
