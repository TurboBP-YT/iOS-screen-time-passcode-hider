from typing import List
import pyaes, base64
from encryption import pad_int_list_AES_key


def decrypt_passcode(ciphertext: str, key_bytes: bytes) -> str:
    aes = pyaes.AESModeOfOperationCTR(key_bytes)

    # aes.decrypt(…) takes bytes.
    # decrypted data is bytes type. need to decode to plaintext.
    return aes.decrypt(base64.b64decode(ciphertext)).decode("utf-8")


if __name__ == "__main__":
    # reminds end-user to stay on their grind and trust the process
    if input("Are you sure you want to go back to being a Jeffrey? ").lower() not in (
        "y",
        "yes",
    ):
        quit()

    entered_solution: str = input("Enter numbers separated by space: ").strip()
    try:
        input_ints_list: List[int] = [int(s) for s in entered_solution.split()]
    except ValueError:
        print("ERROR: Received Non-Integers or Integers Out of Range [0,255]")
        quit()

    decrypt_key: bytes = bytes(pad_int_list_AES_key(input_ints_list))

    ciphertext_filename: str = input(
        "Enter the name of the file you want to decrypt (type nothing to default to 'passcode_encrypted.txt'): "
    ).strip()

    try:
        with open(
            (
                ciphertext_filename
                if len(ciphertext_filename)
                else "passcode_encrypted.txt"
            ),
            "r",
        ) as f:
            passcode_ciphertext: str = f.read()

            try:
                print(decrypt_passcode(passcode_ciphertext, decrypt_key))

            except UnicodeDecodeError:
                print("Decryption Error")
                quit()
    except FileNotFoundError:
        print("ERROR: File Not Found")
        quit()
