print("=== DIGITAL ID GENERATOR ===\n")

full_name = input("Enter your full naame: ").strip().title()
email = input("Enter your email").strip().lower()

at_position = email.find("@")

username = email[:at_position]
domain = email[at_position + 1:]

clean_username = username.replace(".", " ").title()

print("\n" + "="*35)
print(f"|{'ID CARD':^31}")
print("="*35)
print(f"|Name:  {full_name:<21} |")
print(f"|User:  {clean_username:<21} |")
print(f"|Domain: {domain:<21} |")
print("="*35)