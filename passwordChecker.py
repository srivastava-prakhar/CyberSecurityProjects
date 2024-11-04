import re
import hashlib

def check_password_strength(password):
    if len(password) < 8:
        return "Password too short! Must be at least 8 characters."
    if not re.search(r"[A-Z]", password):
        return "Password should include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password should include at least one lowercase letter."
    if not re.search(r"\d", password):
        return "Password should include at least one number."
    if not re.search(r"[@$!%*?&]", password):
        return "Password should include at least one special character."
    return "Strong password!"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = input("Enter a password to check: ")
strength_result = check_password_strength(password)
print(strength_result)

if strength_result == "Strong password!":
    hashed_password = hash_password(password)
    print("Hashed password:", hashed_password)
else:
    print("Please enter a stronger password to see the hash.")
