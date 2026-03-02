Optimal Stopping and the Secretary Problem

A rigorous study of the classical no-information secretary problem, combining
exact combinatorial analysis, asymptotics, dynamic reasoning, and Monte Carlo validation.

⸻

Overview

We study the optimal stopping problem where candidates arrive in random order and only relative ranks are observable.

The classical threshold strategy:
	•	Observe (and reject) the first r candidates.
	•	Record the best rank among them.
	•	Accept the first subsequent candidate who beats that benchmark.
	•	If none does, accept the final candidate.

The goal is to maximize the probability of selecting the overall best candidate.

⸻

Exact Finite-n Success Probability

For a fixed threshold r, the success probability is:

$$
P_n(r)

\frac{r}{n}
\sum_{k=r+1}^{n}
\frac{1}{k-1}

\frac{r}{n}
\left(H_{n-1} - H_{r-1}\right),
$$

where H_m is the m-th harmonic number.

This formula is derived combinatorially and proven in the paper.

⸻

Asymptotic Result

Let

$$
r = \left\lfloor \frac{n}{e} \right\rfloor.
$$

Then

$$
\lim_{n \to \infty} P_n(r) = \frac{1}{e}.
$$

Thus the optimal strategy is:

Skip approximately 37% of candidates, then accept the next record.

This 1/e limit is a canonical result in optimal stopping theory.

⸻

What This Project Contains
	•	Full mathematical derivation of P_n(r)
	•	Proof of asymptotic optimality
	•	Dynamic reasoning behind threshold strategies
	•	Monte Carlo validation of theory
	•	Convergence to the 1/e limit
	•	Statistical confidence intervals for empirical estimates

⸻

Repository Structure

optimal-stopping-secretary/
│
├── paper.pdf          # Full mathematical write-up
├── paper.tex          # LaTeX source
├── simulation.py   # Monte Carlo validation
└── README.md

Monte Carlo Validation

The simulation estimates:

\mathbb{P}(\text{select best})

under threshold strategies and compares empirical estimates to:
	•	Exact finite-n theory
	•	Asymptotic 1/e limit

To run: python simulation.py

Why This Project Matters

This problem captures core ideas used in:
	•	Optimal stopping theory
	•	Sequential decision making
	•	Dynamic programming intuition
	•	Threshold strategies
	•	Probabilistic asymptotics

It is a clean example of turning combinatorial reasoning into a precise probabilistic statement.

⸻

Extensions

Possible extensions explored or suggested:
	•	Unknown horizon versions
	•	Continuous-time formulations
	•	Random arrival distributions
	•	Multiple-choice secretary variants
	•	Bayesian versions
	•	Connection to prophet inequalities

⸻

Author

Aryan Khan

Drexel University
