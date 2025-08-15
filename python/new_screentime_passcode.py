# user-config
NUM_MATH_PROBLEMS = 5
SECONDS_DISPLAY_EACH_PASSCODE_ENTRY_STEP = 1.5

#

MAX_VALID_AES_KEY_LEN = 32
assert (
    NUM_MATH_PROBLEMS <= MAX_VALID_AES_KEY_LEN
)  # AES keys can’t be longer than 256 bits

from typing import Tuple, List
import passcode_instructions, math_problems, encryption


def encrypt_passcode(plaintext: str, len_key_bytes: int) -> Tuple[str, List[int]]:
    try:
        return encryption.encrypt_str_with_new_random_key(plaintext, len_key_bytes)
    except encryption.TooLongEncryptionKeyException:
        print(f"Too Many Math Problems! Max Allowed Is {MAX_VALID_AES_KEY_LEN}.")
        quit()


def main(allow_overwrites: bool = False) -> Tuple[str, List[int]]:
    passcode: str = passcode_instructions.generate_4digit_passcode()

    passcode_ciphertext, decrypt_key_ints = encrypt_passcode(
        passcode, NUM_MATH_PROBLEMS
    )  # key length (bytes) = number of math problems in challenge

    file_open_mode = "w" if allow_overwrites else "x"
    try:
        with open("passcode_encrypted.txt", file_open_mode) as f:
            print(passcode_ciphertext, file=f)  # stores encrypted passcode in file

        with open("unlock_challenge.txt", file_open_mode) as f:
            print(
                math_problems.generate(decrypt_key_ints), file=f
            )  # stores math problems in file
    except FileExistsError as e:
        print(f"ERROR: The file '{e.filename}' already exists.")
        quit()

    if __name__ == "__main__":
        # 2 times more bullshit numbers than actual numbers.
        # The higher the BS factor, the better you ensure you won’t remember the passcode you entered.
        passcode_instructions.print_entry_directions(
            passcode,
            bullshit_multiplier=2,
            time_interval_s=SECONDS_DISPLAY_EACH_PASSCODE_ENTRY_STEP,
        )

    return passcode, decrypt_key_ints  # for testing purposes


if __name__ == "__main__":
    main()
