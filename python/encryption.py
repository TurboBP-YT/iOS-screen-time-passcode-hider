from typing import Tuple, List
import pyaes, random, base64


class TooLongEncryptionKeyException(Exception):
    """AES Encryption Key Longer Than 32 Bytes Is Unsupported"""

    pass


def pad_int_list_AES_key(bytes_as_int_list: List[int]) -> List[int]:
    VALID_AES_KEY_LENS = (16, 20, 24, 32)  # bytes
    # the list gets filled with the last number til the length of the next smallest allowed AES key size
    l = len(bytes_as_int_list)
    try:
        len_padded_key = next(n for n in VALID_AES_KEY_LENS if n >= l)
    except StopIteration:
        raise TooLongEncryptionKeyException()

    trailing_pad = (len_padded_key - l) * [bytes_as_int_list[-1]]
    return bytes_as_int_list + trailing_pad


def encrypt_str_with_new_random_key(
    plaintext: str, len_key_bytes: int
) -> Tuple[str, List[int]]:
    key_ints_list = [random.randrange(256) for _ in range(len_key_bytes)]
    key_bytes = bytes(pad_int_list_AES_key(key_ints_list))

    aes = pyaes.AESModeOfOperationCTR(key_bytes)
    ciphertext = base64.b64encode(aes.encrypt(plaintext)).decode("utf-8")

    return ciphertext, key_ints_list
