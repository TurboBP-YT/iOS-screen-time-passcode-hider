import random, time, os


def random_digit() -> int:
    return random.randrange(1, 10)


def generate() -> str:
    return "".join([str(random_digit()) for _ in range(4)])


def clear_console():
    print("\033[H\033[J", end="")  # ANSI


def print_entry_directions(
    passcode: str, bullshit_multiplier: int, time_interval_s: float
):
    steps = list(passcode)
    for i in range(bullshit_multiplier * len(passcode)):
        insertion_index = random.randrange(0, len(steps))
        steps = steps[:insertion_index] + ["(", ")"] + steps[insertion_index:]

    clear_console()
    print("Get Ready")
    time.sleep(time_interval_s)
    clear_console()
    print("Countdown: [==]")
    time.sleep(time_interval_s)
    clear_console()
    print("Countdown: [= ]")
    time.sleep(time_interval_s)
    clear_console()
    print("Countdown: [  ]")

    # i is for flashing the * symbol to differentiate 2 of the same number in a row
    for i, c in enumerate(steps):
        time.sleep(time_interval_s)
        clear_console()

        # alternates like colons in digital clocks
        indicator = "* " if i % 2 == 0 else "  "

        if c == "(":
            print(f"{indicator}Type {random_digit()}")
            continue
        elif c == ")":
            print(f"{indicator}Press DELETE")
            continue
        print(f"{indicator}Type {c}")

    time.sleep(time_interval_s)
    clear_console()
