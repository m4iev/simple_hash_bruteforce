# Simple Hash Bruteforce Tool
This is a basic Python script designed for educational purposes, specifically for ID-Networkers Cybersecurity Engineer bootcamp assignments, to demonstrate the concept of hash bruteforcing. It attempts to discover the original plaintext string that corresponds to a given cryptographic hash by systematically trying combinations of characters up to a specified maximum length.
## Features
* Supports MD5, SHA1, and SHA256 hashing algorithms.
* Allows custom definition of the character set (e.g., lowercase letters, numbers, special characters) to be used in the bruteforce.
* Enables setting a maximum length for the plaintext strings to be attempted.
* Provides real-time feedback on progress, including the number of attempts and time elapsed.
## How to Use
### Prerequisites
* Python 3.x installed on your system.
## Installation
1. Clone the repository (or download the script):
    ```
    git clone https://github.com/m4iev/simple_hash_bruteforce.git
    cd simple_hash_bruteforce
    ```
    
2. Save the script: Ensure the hash_bruteforce.py file is in your desired directory.

## Running the Script
1. Open your terminal or command prompt.
2. Navigate to the directory where you saved hash_bruteforce.py.
3. Run the script using the Python interpreter:
    `python hash_bruteforce.py`
4. Follow the on-screen prompts to input the necessary details:
* Enter the hash to crack: The cryptographic hash string you want to bruteforce.
* Enter the hash type (md5, sha1, sha256): Specify the algorithm used to generate the hash.
* Enter the characters to use (e.g., 'abcABC123!@#$'): Define the pool of characters that the script will use to generate plaintext combinations.
* Enter the maximum length of the plaintext to try: Set the longest possible plaintext string the script will attempt.

## Important Notes & Considerations

* Educational Purpose Only: This tool is intended for learning and demonstrating the concept of bruteforce attacks. It is not designed for real-world password cracking due to its simplicity and computational limitations.

* Computational Cost: Bruteforcing is extremely resource-intensive. As the character set size or the maximum plaintext length increases, the time required to find a match grows exponentially. Even small increases can make cracking practically impossible.

* Hash Strength: Modern cryptographic hashes (especially SHA256 and stronger) are designed to be highly resistant to bruteforce attacks. This script will take an extremely long time (likely centuries on standard hardware) to crack anything but very short, simple hashes.

* Responsible Use: Always ensure you have explicit permission before attempting to bruteforce any hash that is not your own or provided for authorized testing purposes. Misuse of such tools can have serious legal consequences.

## Disclaimer

This software is provided "as is," without warranty of any kind, express or implied. The author is not responsible for any misuse or damage caused by this software. Use responsibly and ethically.
