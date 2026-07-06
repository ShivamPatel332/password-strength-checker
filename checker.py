import math

password = input("Enter a password to check: ")

# --- Common password check ---
common_passwords = ["123456", "password", "123456789", "qwerty", "abc123", 
                     "password1", "111111", "iloveyou", "admin", "welcome"]

if password.lower() in common_passwords:
    print(" DANGER: This is one of the most commonly used passwords — it would be cracked instantly.")

# --- Basic checks (from Phase 1) ---
length = len(password)
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_symbol = any(not c.isalnum() for c in password)

score = sum([has_upper, has_lower, has_digit, has_symbol])

# --- Entropy calculation ---
pool_size = 0
if has_lower: pool_size += 26
if has_upper: pool_size += 26
if has_digit: pool_size += 10
if has_symbol: pool_size += 32

if pool_size > 0:
    entropy = length * math.log2(pool_size)
else:
    entropy = 0

print(f"Entropy: {entropy:.2f} bits")

# --- Final verdict ---
if length < 8:
    print("Weak: too short")
elif score < 3:
    print("Medium: add more variety (symbols, numbers, capitals)")
elif entropy < 40:
    print("Medium: technically varied, but still crackable with effort")
else:
    print("Strong password!")
    