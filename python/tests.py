import main, unlock

if __name__ == "__main__":
    input(
        "WARNING: Running tests will overwrite your save file (if exists). Press ENTER to proceed."
    )

    N_TESTS = 100
    for _ in range(N_TESTS):
        passcode, challenge_answers = main.main()

        with open("passcode_encrypted.txt", "r") as f:
            passcode_ciphertext: str = f.read()
            print(
                unlock.decrypt_passcode(passcode_ciphertext, bytes(challenge_answers))
                == passcode
            )
