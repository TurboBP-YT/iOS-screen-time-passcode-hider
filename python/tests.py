import new_screentime_passcode, unlock
from encryption import pad_int_list_AES_key

if __name__ == "__main__":
    input(
        "WARNING: Running tests will overwrite your save files (if exists). Press ENTER to proceed."
    )

    N_TESTS = 100
    for _ in range(N_TESTS):
        passcode, challenge_answers = new_screentime_passcode.main(
            allow_overwrites=True
        )

        with open("passcode_encrypted.txt", "r") as f:
            passcode_ciphertext: str = f.read()
            print(
                unlock.decrypt_passcode(
                    passcode_ciphertext, bytes(pad_int_list_AES_key(challenge_answers))
                )
                == passcode
            )
