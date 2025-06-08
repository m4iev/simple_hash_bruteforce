import hashlib
import itertools
import string
import time

def bruteforce_hash(target_hash, hash_type, charset, max_length):
    """
    Attempts to bruteforce a given hash using a specified character set and maximum length.

    Args:
        target_hash (str): The hash string to crack.
        hash_type (str): The type of hash (e.g., 'md5', 'sha1', 'sha256').
        charset (str): A string containing all characters to use for permutations (e.g., 'abcdefg12345').
        max_length (int): The maximum length of the plaintext to try.

    Returns:
        str or None: The cracked plaintext string if found, otherwise None.
    """
    print(f"[*] Starting bruteforce for hash: {target_hash} (Type: {hash_type.upper()})")
    print(f"[*] Character set: '{charset}'")
    print(f"[*] Max length to try: {max_length}")

    start_time = time.time()
    attempts = 0

    # Iterate through possible lengths
    for length in range(1, max_length + 1):
        print(f"Trying permutations of length {length}...")
        # Generate all permutations of the charset for the current length
        for attempt in itertools.product(charset, repeat=length):
            attempts += 1
            plaintext = "".join(attempt)

            # Calculate the hash of the generated plaintext based on the specified type
            if hash_type == 'md5':
                current_hash = hashlib.md5(plaintext.encode('utf-8')).hexdigest()
            elif hash_type == 'sha1':
                current_hash = hashlib.sha1(plaintext.encode('utf-8')).hexdigest()
            elif hash_type == 'sha256':
                current_hash = hashlib.sha256(plaintext.encode('utf-8')).hexdigest()
            else:
                print(f"[!] Error: Unsupported hash type '{hash_type}'. Supported types: md5, sha1, sha256")
                return None

            # Compare the generated hash with the target hash
            if current_hash == target_hash:
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"\n[+] Hash cracked!")
                print(f"[+] Plaintext: '{plaintext}'")
                print(f"[+] Attempts: {attempts}")
                print(f"[+] Time taken: {elapsed_time:.2f} seconds")
                return plaintext

            # Optional: Print progress periodically
            if attempts % 1000000 == 0: # Print every 1 million attempts
                print(f"  Attempted {attempts} combinations (current: '{plaintext}')", end='\r')

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n[-] Plaintext not found within the specified constraints.")
    print(f"[-] Total attempts: {attempts}")
    print(f"[-] Time taken: {elapsed_time:.2f} seconds")
    return None

if __name__ == "__main__":
    # --- Configuration for your bruteforce ---

    # Example 1: MD5 hash of "cat"
    # target_hash_to_crack = "4d791244e803d1685959146c26563e46"
    # hash_algorithm = "md5"
    # characters_to_use = string.ascii_lowercase # all lowercase letters
    # max_possible_length = 5

    # Example 2: SHA256 hash of "test"
    # target_hash_to_crack = "9f86d081884c7d659a2feaa0c55ad015a3bf41f021e162796030990334860dfd"
    # hash_algorithm = "sha256"
    # characters_to_use = string.ascii_lowercase + string.digits # lowercase letters and digits
    # max_possible_length = 5

    # --- Set your desired values here for the assignment ---
    target_hash_to_crack = input("Enter the hash to crack: ").strip()
    hash_algorithm = input("Enter the hash type (md5, sha1, sha256): ").strip().lower()
    characters_to_use = input("Enter the characters to use (e.g., 'abcABC123!@#$'): ").strip()
    max_possible_length = int(input("Enter the maximum length of the plaintext to try: "))

    # --- Run the bruteforce ---
    bruteforce_hash(target_hash_to_crack, hash_algorithm, characters_to_use, max_possible_length)

