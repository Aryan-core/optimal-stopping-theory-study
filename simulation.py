"""
simulation.py

Monte Carlo validation of the classical Secretary Problem
(no-information model, threshold strategy).

This script:

1) Estimates success probability P_n(r) via simulation
2) Compares to exact theoretical formula
3) Finds empirically optimal threshold
4) Verifies convergence toward 1/e

No figures are generated — numerical output only.

Run:
    python simulation.py
"""

import math
import numpy as np


# ---------------------------------------------------
# Theoretical success probability
# P_n(r) = (r/n) * (H_{n-1} - H_{r-1})
# ---------------------------------------------------
def theoretical_success_prob(n: int, r: int) -> float:
    r = max(0, min(r, n - 1))
    if r == 0:
        return 1.0 / n

    H_n1 = sum(1.0 / k for k in range(1, n))
    H_r1 = sum(1.0 / k for k in range(1, r)) if r > 1 else 0.0
    return (r / n) * (H_n1 - H_r1)


# ---------------------------------------------------
# One simulation run
# ---------------------------------------------------
def run_once(n: int, r: int, rng: np.random.Generator) -> bool:
    perm = rng.permutation(n) + 1  # ranks 1..n
    best_index = int(np.argmin(perm))

    r = max(0, min(r, n - 1))

    if r == 0:
        benchmark = math.inf
    else:
        benchmark = int(np.min(perm[:r]))

    chosen = None
    for i in range(r, n):
        if perm[i] < benchmark:
            chosen = i
            break

    if chosen is None:
        chosen = n - 1

    return chosen == best_index


# ---------------------------------------------------
# Monte Carlo estimate
# ---------------------------------------------------
def estimate_success(n: int, r: int, trials: int, seed: int = 0):
    rng = np.random.default_rng(seed)
    wins = 0

    for _ in range(trials):
        if run_once(n, r, rng):
            wins += 1

    p_hat = wins / trials
    se = math.sqrt(p_hat * (1 - p_hat) / trials)

    return p_hat, se


# ---------------------------------------------------
# Main analysis
# ---------------------------------------------------
def main():

    print("\nSecretary Problem Monte Carlo Validation\n")

    n = 200
    trials = 100000

    print(f"Horizon n = {n}")
    print(f"Trials per estimate = {trials}\n")

    # Sweep r values
    r_values = range(1, n)
    mc_vals = []
    th_vals = []

    for r in r_values:
        mc, _ = estimate_success(n, r, trials, seed=r)
        th = theoretical_success_prob(n, r)

        mc_vals.append(mc)
        th_vals.append(th)

    mc_vals = np.array(mc_vals)
    th_vals = np.array(th_vals)

    r_star_mc = r_values[int(np.argmax(mc_vals))]
    r_star_th = r_values[int(np.argmax(th_vals))]

    print("Empirical optimal r:", r_star_mc)
    print("Theoretical optimal r:", r_star_th)
    print("Empirical success probability:", round(max(mc_vals), 6))
    print("Theoretical success probability:", round(max(th_vals), 6))
    print("Limit 1/e ≈", round(1 / math.e, 6))

    print("\nConvergence toward 1/e:")

    for n_test in [50, 100, 200, 400, 800]:
        r_test = int(n_test / math.e)
        mc, _ = estimate_success(n_test, r_test, trials // 2, seed=n_test)
        th = theoretical_success_prob(n_test, r_test)

        print(
            f"n={n_test:4d} | r≈n/e={r_test:4d} | "
            f"MC={mc:.5f} | Theory={th:.5f}"
        )

    print("\nDone.\n")


if __name__ == "__main__":
    main()
