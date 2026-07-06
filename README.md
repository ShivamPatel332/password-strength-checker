# password-strength-checker
A Python tool that analyzes password strength using entropy calculation and common password detection

# Password Strength Checker

A Python command-line tool that analyzes password strength using entropy calculation and common password detection — built to understand the actual math and security concepts behind "strong" vs "weak" passwords, not just apply arbitrary rules.

## What It Does

This tool takes a password as input and evaluates it using three checks:

1. **Length and character variety** — checks for uppercase, lowercase, digits, and symbols
2. **Common password detection** — flags passwords found on known lists of frequently breached/leaked passwords
3. **Entropy calculation** — measures password unpredictability in bits, using the formula:

entropy = length × log2(character_pool_size)
Entropy is a real security metric that quantifies how many possible combinations an attacker would need to try in a brute-force attack. Higher entropy = exponentially harder to crack.

## Why Entropy Matters

Many "strength meters" just check boxes (has a number? has a symbol?) without considering length, which is misleading. A password like `P@ss1` looks "complex" but is actually short and low-entropy — easily cracked. Meanwhile, a long passphrase like `horse battery correct staple` has far higher entropy despite using only lowercase letters and spaces.

This project reflects that principle: **length contributes more to real security than complexity does.**

## How to Run

1. Make sure Python 3 is installed
2. Clone this repo:

   git clone https://github.com/ShivamPatel332/password-strength-checker.git
cd password-strength-checker
3. Run the script:
   python checker.py
4. Enter a password when prompted to see its strength rating, entropy score, and any warnings.

## Example Output

Enter a password to check: password123
DANGER: This is one of the most commonly used passwords — it would be cracked instantly.
Entropy: 39.86 bits
Medium: technically varied, but still crackable with effort

## What I Learned

Building this project helped me understand:
- How entropy is calculated and why it's a better strength metric than simple character-type checks
- Why common/leaked passwords remain dangerous even when they "look" complex
- Basic Python fundamentals: string methods, list membership checks, conditional logic, and using the `math` module

## Future Improvements

- Expand the common password list using a larger public dataset (e.g., RockYou wordlist)
- Detect simple patterns like keyboard walks (`qwerty`, `12345`) or repeated characters
- Add a simple GUI or web interface using Flask
- Estimate real-world crack time based on entropy and typical hardware speeds

## Tech Stack

- Python 3
