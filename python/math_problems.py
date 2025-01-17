from typing import List
import random, math, sympy


# returns a multiline string of math problems (linear system of 2 equations) from the provided answers
def generate(answers: List[int]) -> str:
    MAX_SOLUTION = 1000  # ≥ 255
    RANGE_SLOPE_INT = (1, 20)
    RANGE_SLOPE_FRAC_DENOM = (2, 10)
    MAX_MULTIPLIER = 10

    MODES = (
        "Find x + y.",
        "Find x - y.",
        "Find y - x.",
    )

    out_text = ""

    for answer in answers:
        # Point–Slope Form : y - y_p = m(x - x_p)
        mode: str = random.choice(MODES)
        if mode == MODES[0]:
            xp = random.randrange(answer + 1)
            yp = answer - xp
        elif mode == MODES[1]:
            yp = random.randrange(MAX_SOLUTION - answer + 1)
            xp = yp + answer
        elif mode == MODES[2]:
            xp = random.randrange(MAX_SOLUTION - answer + 1)
            yp = xp + answer
        out_text += mode + "\n"

        randslope = lambda: random.choice(
            (
                random.randrange(*RANGE_SLOPE_INT)
                * random.choice((-1, 1)),  # random sign
                sympy.Rational(f"1/{random.randrange(*RANGE_SLOPE_FRAC_DENOM)}"),
            )
        )
        m1 = randslope()
        while (
            m2 := randslope()
        ) == m1:  # 2 lines’ slopes can’t be equal for the system to have 1 solution
            m2 = randslope()

        # Standard Form : ax + by = c
        for m in (m1, m2):
            global_multiplier = random.randrange(1, MAX_MULTIPLIER + 1)

            x, y, a, b, c = sympy.symbols("x y a b c")
            a = m
            c = global_multiplier * (m * xp - yp)
            ax_minus_by = global_multiplier * (a * x - y)

            out_text += f"{sympy.simplify(ax_minus_by)} = {c}\n"

        out_text += "\n"

    return out_text.strip()
