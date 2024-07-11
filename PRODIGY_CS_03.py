import re

def password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Score calculation
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Feedback
    feedback = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    # Detailed feedback
    suggestions = []
    if not length_criteria:
        suggestions.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        suggestions.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        suggestions.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        suggestions.append("Password should include at least one number.")
    if not special_char_criteria:
        suggestions.append("Password should include at least one special character.")

    return feedback[score], suggestions

def main():
    print("Password Strength Checker")
    while True:
        password = input("Enter a password to check its strength: ")
        strength, suggestions = password_strength(password)
        print(f"Password Strength: {strength}")
        if suggestions:
            print("Suggestions to improve your password:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
        
        another = input("Do you want to check another password? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    main()
