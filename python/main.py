from typing import Tuple, List
import pyaes, random, base64
import passcode_instructions, math_problems

# user-config
NUM_MATH_PROBLEMS = 5
SECONDS_DISPLAY_EACH_PASSCODE_ENTRY_STEP = 1.5

assert NUM_MATH_PROBLEMS <= 32  # AES keys can’t be longer than 256 bits


def pad_int_list_AES_key(bytes_as_int_list: List[int]) -> List[int]:
    VALID_AES_KEY_LENS = (16, 20, 24, 32)  # bytes
    # the list gets filled with the last number til the length of the next smallest allowed AES key size
    l = len(bytes_as_int_list)
    try:
        len_padded_key = next(n for n in VALID_AES_KEY_LENS if n >= l)
    except StopIteration:
        print(f"Too Many Math Problems! Max Allowed Is {max(VALID_AES_KEY_LENS)}.")
        quit()
    trailing_pad = (len_padded_key - l) * [bytes_as_int_list[-1]]
    return bytes_as_int_list + trailing_pad


def encrypt_passcode(plaintext: str, len_key_bytes: int) -> Tuple[str, List[int]]:
    key_ints_list = [random.randrange(256) for _ in range(len_key_bytes)]
    key_bytes = bytes(pad_int_list_AES_key(key_ints_list))

    aes = pyaes.AESModeOfOperationCTR(key_bytes)
    ciphertext = base64.b64encode(aes.encrypt(plaintext)).decode("utf-8")

    return ciphertext, key_ints_list


def main() -> Tuple[str, List[int]]:
    passcode: str = passcode_instructions.generate()

    passcode_ciphertext, decrypt_key_ints = encrypt_passcode(
        passcode, NUM_MATH_PROBLEMS
    )  # key length (bytes) = number of math problems in challenge

    with open("passcode_encrypted.txt", "w") as f:
        print(passcode_ciphertext, file=f)  # stores encrypted passcode in file

    with open("unlock_challenge.txt", "w") as f:
        print(
            math_problems.generate(decrypt_key_ints), file=f
        )  # stores math problems in file

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
