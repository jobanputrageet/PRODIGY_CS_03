import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score >= 3:
        strength = "Strong"
    else:
        strength = "Weak"
    
    feedback = {
        "Length": "Check" if length_criteria else " Password should be at least 8 characters long.",
        "Uppercase": "Check" if uppercase_criteria else " Password should contain at least one uppercase letter.",
        "Lowercase": "Check" if lowercase_criteria else " Password should contain at least one lowercase letter.",
        "Number": "Check" if number_criteria else " Password should contain at least one number.",
        "Special Character": "Check" if special_char_criteria else " Password should contain at least one special character."
    }
    
    return strength, feedback


password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print(f"Password Strength: {strength}")
for criteria, message in feedback.items():
    print(f"{criteria}: {message}")
