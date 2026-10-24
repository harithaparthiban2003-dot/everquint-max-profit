def max_profit(n):
    max_earnings = 0
    solutions = set()

    def calculate(time_left, t, p, c, earnings):
        nonlocal max_earnings, solutions

        if earnings > max_earnings:
            max_earnings = earnings
            solutions = {(t, p, c)}
        elif earnings == max_earnings:
            solutions.add((t, p, c))

        # Build a Theatre
        if time_left >= 5:
            calculate(
                time_left - 5,
                t + 1, p, c,
                earnings + 1500 * (time_left - 5)
            )

        # Build a Pub
        if time_left >= 4:
            calculate(
                time_left - 4,
                t, p + 1, c,
                earnings + 1000 * (time_left - 4)
            )

        # Build a Commercial Park
        if time_left >= 10:
            calculate(
                time_left - 10,
                t, p, c + 1,
                earnings + 2000 * (time_left - 10)
            )

    calculate(n, 0, 0, 0, 0)

    print(f"Earnings: ${max_earnings}")

    for t, p, c in sorted(solutions):
        print(f"T: {t} P: {p} C: {c}")


if __name__ == "__main__":
    n = int(input("Enter time unit: "))
    max_profit(n)