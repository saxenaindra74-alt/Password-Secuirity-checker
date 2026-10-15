
import string
import secrets
import re


def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters for better security.")
    else:
        feedback.append("Use at least 12 characters.")

    # 2. Check complexity
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # 3. Check common passwords
    common_passwords = (
        "password",
        "password1234",
        "12345678",
        "qwerty123",
        "admin123"
    )

    if password.lower() in common_passwords:
        score = 0
        feedback.append("Avoid common passwords.")

    # 4. Check repeated characters
    if re.search(r"(.)\1{2,}", password):
        score -= 1
        feedback.append("Avoid repeating the same character three or more times.")

    # 5. Determine password strength
    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


def generate_strong_password(length=16):
    # Ensure the password contains every character category
    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]

    password = [secrets.choice(group) for group in groups]

    all_characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    # Add random characters to reach the required length
    password.extend(
        secrets.choice(all_characters)
        for _ in range(length - len(password))
    )

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():
    print("===== PASSWORD STRENGTH CHECKER =====")

    password = input("Enter a password to evaluate: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions for Improvement:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("\nYour password meets the basic checks!")

    if strength != "Strong":
        print("\nSuggested stronger password:")
        print(generate_strong_password())

    print("\nNote: Never share your real password with anyone.")


if __name__ == "__main__":
    main()

