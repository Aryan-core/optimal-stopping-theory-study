Optimal Stopping and the Secretary Problem

A rigorous study of the classical no-information secretary problem, combining exact combinatorial analysis, asymptotics, dynamic reasoning, and Monte Carlo validation.

**Author:** Aryan Khan  
Undergraduate Probability Study Project  

---

## Overview

We study the optimal stopping problem in which candidates arrive in uniformly random order and only relative ranks are observable.

The classical threshold strategy:

1. Observe (and reject) the first **r** candidates.  
2. Record the best rank among them.  
3. Accept the first subsequent candidate who beats that benchmark.  
4. If none does, accept the final candidate.

The objective is to maximize the probability of selecting the overall best candidate.

---

## Exact Finite-n Success Probability

For a fixed threshold $begin:math:text$ r $end:math:text$, the exact probability of success is:

```
P_n(r) = (r/n) * sum_{k=r+1}^{n} 1/(k-1)
       = (r/n) * (H_{n-1} - H_{r-1})
```

where $begin:math:text$ H_m $end:math:text$ denotes the m-th harmonic number.

This formula is derived combinatorially in the paper and proven rigorously.

---

## Asymptotic Optimal Strategy

Let

```
r = floor(n / e)
```

Then

```
lim_{n→∞} P_n(r) = 1/e
```

Thus the optimal strategy is:

> Skip approximately **37%** of candidates, then accept the next record.

The constant $begin:math:text$ 1/e \\approx 0.3679 $end:math:text$ is a canonical result in optimal stopping theory.

---

## Mathematical Contributions

This project includes:

- Full derivation of the finite-n formula $begin:math:text$ P_n(r) $end:math:text$
- Proof of asymptotic optimality
- Dynamic reasoning behind threshold strategies
- Harmonic number analysis
- Large-n approximation via asymptotics
- Monte Carlo validation of theoretical results
- Statistical confidence intervals for empirical estimates

---

## Repository Structure

```
optimal-stopping-secretary/
│
├── paper.pdf        # Full mathematical write-up
├── paper.tex        # LaTeX source
├── simulation.py    # Monte Carlo validation
└── README.md
```

---

## Monte Carlo Validation

The simulation estimates:

```
P(select best)
```

under threshold strategies and compares empirical results to:

- Exact finite-n theory
- The asymptotic limit 1/e

Run with:

```
python simulation.py
```

---

## Why This Project Matters

The secretary problem captures core ideas used in:

- Optimal stopping theory  
- Sequential decision making  
- Dynamic programming intuition  
- Threshold-based policies  
- Probabilistic asymptotics  

It is a clean example of turning combinatorial reasoning into a precise probabilistic statement.

---

## Extensions

Possible extensions explored or suggested:

- Unknown horizon versions  
- Continuous-time formulations  
- Random arrival distributions  
- Multiple-choice secretary variants  
- Bayesian variants  
- Connections to prophet inequalities  

---

## Author

Aryan Khan  
Drexel University 
