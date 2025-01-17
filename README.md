# iOS-screen-time-passcode-hider
Python script. Create an iOS Screen Time passcode that you won’t remember, and hide it from yourself. You can retrieve it by solving math problems. Inspired by Password Locker.

---

## Usage: Set Passcode

1. (iOS) Open Settings
2. (iOS) Go to Screen Time
3. (iOS) Tap <kbd>Turn On Screen Time Passcode</kbd> or <kbd>Change Screen Time Passcode</kbd>
4. (iOS) If you tapped <kbd>Change Screen Time Passcode</kbd> enter the existing passcode
5. (Python) Run `main.py`
6. (iOS) Follow the instructions displayed in the Python console/terminal.
7. Finished. Your encrypted passcode is stored in `passcode_encrypted.txt` and the decryption challenge are stored in `unlock_challenge.txt`

## Usage: Retrieve Encrypted Passcode

1. Solve the algebra problems located in `unlock_challenge.txt` and write down your answers
2. (Python) Run `unlock.py`
3. (Python) Type your answers in and then press <kbd>enter</kbd>
4. (Python) If the answers are correct, the passcode shows up.
