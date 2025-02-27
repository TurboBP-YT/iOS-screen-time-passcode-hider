from main import encrypt_passcode, NUM_MATH_PROBLEMS
import random, math_problems

# Apple Account’s real password = "$Aa" + the generated digitstring
PASSWORD_PREFIX_CONSTANT = "$Aa"  # to meet password requirements
LEN_RANDOM_PASSWORD_SUFFIX = 15

# passwords must be ≥ 8 chars long
assert LEN_RANDOM_PASSWORD_SUFFIX >= 5

if __name__ == "__main__":

    password = PASSWORD_PREFIX_CONSTANT + "".join(
        [str(random.randrange(0, 10)) for _ in range(LEN_RANDOM_PASSWORD_SUFFIX)]
    )

    password_ciphertext, decrypt_key_ints = encrypt_passcode(
        password, NUM_MATH_PROBLEMS
    )  # key length (bytes) = number of math problems in challenge

    with open("apple_password_encrypted.txt", "w") as f:
        print(password_ciphertext, file=f)  # stores encrypted passcode in file

    with open("apple_account_unlock_challenge.txt", "w") as f:
        print(
            math_problems.generate(decrypt_key_ints), file=f
        )  # stores math problems in file

    print(password)
