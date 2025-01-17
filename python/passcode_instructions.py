import random
from tqdm import tqdm
from time import sleep


def random_digit() -> int:
    return random.randrange(1, 10)


def generate() -> str:
    return "".join([str(random_digit()) for _ in range(4)])


def clear_console():
    print("\033[H\033[J", end="")  # ANSI


def depth_at_index(iterable, pos: int) -> int:
    depth: int = 0
    max_depth: int = 0
    for c in iterable:
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        if depth > max_depth:
            max_depth = depth
    return max_depth


def show_timed_progress_bar(seconds: float, n_divisions: int):
    interval_s: float = seconds / n_divisions
    for _ in tqdm(range(n_divisions)):
        sleep(interval_s)


def print_entry_directions(
    passcode: str, bullshit_multiplier: int, time_interval_s: float
):
    PROGRESS_BARS_SMOOTHNESS_STEPS = 100
    L = len(passcode)

    clear_console()
    print("Get Ready\n")
    show_timed_progress_bar(5, PROGRESS_BARS_SMOOTHNESS_STEPS)

    i = 0  # i is for flashing the * symbol to differentiate 2 of the same number in a row

    N_FAKES_GROUPS = L - 1  # [fakes1, real1, fakes2, real2, fakes2, real3, real4]
    MAX_DEPTHS = [
        L - n - 1 for n in range(N_FAKES_GROUPS)
    ]  # fake steps must not reach 4 digits!

    for _ in range(2):  # need to enter passcode twice on iPhone to set

        fake_steps_groups = [[] for _ in range(N_FAKES_GROUPS)]
        for _ in range(
            bullshit_multiplier * L
        ):  # fixed number of fake steps = bullshit_multiplier x passcode length
            is_insert_valid = False
            while not is_insert_valid:
                # weighted random choice, fake steps are more likely to be inserted earlier in the sequence
                insertion_group_index = random.choices(
                    list(range(N_FAKES_GROUPS)), weights=MAX_DEPTHS
                )[0]
                insertion_group = fake_steps_groups[insertion_group_index]
                insertion_index = random.randrange(0, len(insertion_group) + 1)
                is_insert_valid = (
                    depth_at_index(insertion_group, insertion_index)
                    < MAX_DEPTHS[insertion_group_index]
                )

            # insertion method guarantees valid parantheses
            fake_steps_groups[insertion_group_index] = (
                insertion_group[:insertion_index]
                + ["(", ")"]
                + insertion_group[insertion_index:]
            )

        # places fake steps between real steps
        # flattens list
        steps = [
            e
            for g in [
                fake_steps + [real_step]
                for fake_steps, real_step in zip(fake_steps_groups, passcode[:-1])
            ]
            for e in g
        ] + [passcode[-1]]

        # displays instructions in terminal
        for c in steps:
            clear_console()

            # flashes a '>' symbol alternating on and off like colons in digital clocks
            indicator = "> " if i % 2 == 0 else "  "

            if c == "(":
                print(f"{indicator}Type {random_digit()}")
            elif c == ")":
                print(f"{indicator}Press DELETE")
            else:
                print(f"{indicator}Type {c}")

            print()
            show_timed_progress_bar(time_interval_s, PROGRESS_BARS_SMOOTHNESS_STEPS)

            i += 1

    clear_console()
