# flam_assignement
FLAM Assignment for Research and Development / AI

from pathlib import Path

readme_text = """## 📌 Parametric Curve Fitting — README

### 🔹 Problem Statement

We are given a list of observed 2D points `(x, y)` and the following parametric curve:

\\[
\\begin{aligned}
x(t) &= t\\cos\\theta \\;-\\; e^{M|t|}\\sin(0.3t)\\sin\\theta \\;+\\; X,\\\\[4pt]
y(t) &= 42 \\;+\\; t\\sin\\theta \\;+\\; e^{M|t|}\\sin(0.3t)\\cos\\theta,
\\end{aligned}
\\]

Unknown variables:

\\[
\\theta,\\; M,\\; X
\\]

With constraints:

\\[
0^\\circ < \\theta < 50^\\circ,\\quad -0.05 < M < 0.05,\\quad 0 < X < 100
\\]

Parameter `t` range:

\\[
6 \\le t \\le 60
\\]

Goal:  
**Find θ, M, X that minimize the L1 distance between the observed curve and the modeled curve.**

---

### ✅ Final Result

| Parameter | Value |
|----------|-------|
| θ (degrees) | **30.029348421860174°** |
| θ (radians) | **0.5241** |
| M | **-0.004550200343689979** |
| X | **55.32918602068894** |
| Total L1 Distance | **28256.622462306572** |

---

### ✅ Final Parametric Equation (LaTeX Submission Format)

```latex
\\[
\\left(
t\\cos(0.5241)
- e^{-0.0045502\\left|t\\right|}\\sin(0.3t)\\sin(0.5241)
+ 55.329186,\\;
42 + t\\sin(0.5241)
+ e^{-0.0045502\\left|t\\right|}\\sin(0.3t)\\cos(0.5241)
\\right)
\\]
