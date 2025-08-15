from new_screentime_passcode import NUM_MATH_PROBLEMS
import random, math_problems, encryption

# account’s real password = "$Aa" + the generated digitstring
PASSWORD_PREFIX_CONSTANT = "$Aa"  # to meet password requirements
LEN_RANDOM_PASSWORD_SUFFIX = 15

# passwords must be ≥ 8 chars long
assert LEN_RANDOM_PASSWORD_SUFFIX >= 8 - len(PASSWORD_PREFIX_CONSTANT)

if __name__ == "__main__":

    password = PASSWORD_PREFIX_CONSTANT + "".join(
        [str(random.randrange(0, 10)) for _ in range(LEN_RANDOM_PASSWORD_SUFFIX)]
    )

    password_ciphertext, decrypt_key_ints = encryption.encrypt_str_with_new_random_key(
        password, NUM_MATH_PROBLEMS
    )  # key length (bytes) = number of math problems in challenge

    try:
        with open("account_password_encrypted.txt", "x") as f:
            print(password_ciphertext, file=f)  # stores encrypted passcode in file

        with open("account_unlock_challenge.txt", "x") as f:
            print(
                math_problems.generate(decrypt_key_ints), file=f
            )  # stores math problems in file
    except FileExistsError as e:
        print(f"ERROR: The file '{e.filename}' already exists.")
        quit()

    print(password)
