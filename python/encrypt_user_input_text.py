from new_screentime_passcode import NUM_MATH_PROBLEMS
import math_problems, encryption

if __name__ == "__main__":

    plaintext: str = input("Text you want to encrypt: ")

    ciphertext, decrypt_key_ints = encryption.encrypt_str_with_new_random_key(
        plaintext, NUM_MATH_PROBLEMS
    )  # key length (bytes) = number of math problems in challenge

    try:
        with open("user_input_encrypted.txt", "x") as f:
            print(ciphertext, file=f)  # stores encrypted passcode in file

        with open("user_input_unlock_challenge.txt", "x") as f:
            print(
                math_problems.generate(decrypt_key_ints), file=f
            )  # stores math problems in file
    except FileExistsError as e:
        print(f"ERROR: The file '{e.filename}' already exists.")
        quit()

    print("DONE: Encrypted and saved to files.")
