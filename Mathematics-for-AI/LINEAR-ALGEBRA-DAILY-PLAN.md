# Linear Algebra — 112-Day AI Mastery Plan

## How to use this plan

Every study day follows:

1. **Video / intuition** — 3Blue1Brown, *Essence of Linear Algebra*
2. **Theory** — MIT 18.06 with Gilbert Strang
3. **Practice** — MIT problem sets + selected textbook exercises
4. **Code** — Python + NumPy, preferably from scratch before library verification
5. **Visualization** — Matplotlib when the idea benefits from it
6. **AI/ML connection** — write 3–5 lines on where the concept appears
7. **GitHub** — save the notebook and a short Markdown note

### Resource key

- **3B** = 3Blue1Brown, *Essence of Linear Algebra*
- **MIT18.06** = MIT OpenCourseWare 18.06 Linear Algebra
- **MIT18.065** = MIT OpenCourseWare 18.065 Matrix Methods in Data Analysis, Signal Processing, and Machine Learning
- **Book** = Gilbert Strang, *Introduction to Linear Algebra*
- **Lab** = Python + NumPy + Matplotlib + Jupyter

## Time rule

Normal day: 90–120 minutes.
Strong day: 2–3 hours.
Minimum day: 60 minutes.

Do not skip practice just because you have less time. Reduce lecture time first.

---

# PHASE 1 — Vectors, Geometry, Dot Products
## Days 1–14

### Day 1 — What is Linear Algebra?
- 3B: start *Essence of Linear Algebra*
- MIT18.06: course introduction / first lecture
- Practice: identify vectors vs scalars in 10 real examples
- Code: create vectors with NumPy; inspect shape and dtype
- Output: `daily-log/day-01.md`

### Day 2 — Scalars and Vectors
- 3B: vectors intuition
- MIT18.06: vectors / geometry section
- Practice: vector addition and scalar multiplication by hand
- Code: build a vector class-like set of functions for add/scale
- AI link: feature vectors

### Day 3 — Vector Geometry
- 3B: geometric interpretation of vectors
- MIT18.06: geometric vector problems
- Practice: distance between points, vector length
- Code: plot 2D vectors with Matplotlib
- Output: first vector visualization notebook

### Day 4 — Norms and Distance
- MIT18.06 + Book: vector length / norm
- Practice: L1, L2, infinity norm
- Code: implement norms from scratch, then verify with NumPy
- AI link: distance-based models

### Day 5 — Dot Product
- 3B: dot product intuition
- MIT18.06: dot product
- Practice: 15 dot-product questions
- Code: implement dot product with a loop, then NumPy verification
- AI link: similarity

### Day 6 — Angles and Cosine Similarity
- 3B: dot product geometry
- Practice: calculate angles between vectors
- Code: cosine similarity from scratch
- AI link: embeddings / semantic similarity
- Mini task: compare similarity of 5 synthetic vectors

### Day 7 — WEEK 1 REVIEW
- No new lecture
- Re-solve 10 representative problems without notes
- Re-code vector operations from memory
- Create one-page concept map
- GitHub: commit Week 1
- Self-test: explain vector, norm, dot product, cosine similarity aloud

### Day 8 — Projection
- 3B: projection intuition
- MIT18.06: projections
- Practice: vector projection by hand
- Code: projection function from scratch
- AI link: least squares preview

### Day 9 — Orthogonality
- 3B: orthogonal ideas
- MIT18.06: orthogonality
- Practice: determine whether vectors are orthogonal
- Code: orthogonality checker
- Visualization: perpendicular vector examples

### Day 10 — Linear Combination
- MIT18.06: linear combinations
- Book: examples
- Practice: express vectors as combinations of others
- Code: experiment with weighted vector combinations
- AI link: feature composition

### Day 11 — Span
- 3B: span intuition
- MIT18.06: span
- Practice: determine the span of vector sets
- Code: generate points from linear combinations and plot them
- Output: span visualization

### Day 12 — Linear Independence
- MIT18.06 + Book
- Practice: test independence in 2D/3D examples
- Code: experiment using matrix rank
- AI link: redundant features

### Day 13 — Vector Spaces (Intuition)
- 3B / MIT18.06
- Learn vector space axioms conceptually, not by memorization
- Practice: classify examples/non-examples
- Code: small experiments with subspaces
- Explain: why model features form vector spaces

### Day 14 — PROJECT 1
## Vector Geometry Explorer
Build a notebook that:
- accepts vectors
- calculates norm, distance, dot product, angle, projection
- plots the vectors
- labels geometric relationships
- includes a short AI/ML use-case section
- Commit project + README

---

# PHASE 2 — Matrices and Linear Transformations
## Days 15–28

### Day 15 — Matrix Basics
- 3B: matrices
- MIT18.06: matrices as arrays / transformations
- Practice: dimensions and indexing
- Code: create matrices and inspect shapes

### Day 16 — Matrix Addition and Scalar Multiplication
- MIT18.06 + Book
- Practice: 15 calculations
- Code: implement operations from scratch
- AI link: parameter tensors

### Day 17 — Matrix Multiplication
- 3B: matrix multiplication intuition
- MIT18.06: matrix multiplication
- Practice: 15 products by hand
- Code: implement matrix multiplication with nested loops
- Verify with `A @ B`

### Day 18 — Matrix Multiplication as Composition
- 3B: transformations / composition
- Practice: compare AB vs BA
- Code: visualize sequential transformations
- AI link: stacked transformations

### Day 19 — Identity Matrix
- MIT18.06
- Practice: prove/check AI = A and IA = A
- Code: construct identity matrices
- Understand: identity as “do nothing” transformation

### Day 20 — Transpose
- MIT18.06
- Practice: transpose properties
- Code: transpose from scratch + NumPy verification
- AI link: (X^T X)

### Day 21 — WEEK 3 REVIEW
- Mixed problems: vectors + matrices
- Rebuild matrix multiplication from memory
- Visualization challenge: transform a point cloud
- GitHub: Week 3 commit

### Day 22 — 2D Transformations
- 3B: linear transformations
- Practice: scaling/rotation/reflection matrices
- Code: transform a square/triangle
- Output: transformation notebook

### Day 23 — Rotation
- 3B: rotation
- Book: rotation matrix examples
- Practice: 10 rotation problems
- Code: interactive angle experiment
- AI/CV link: geometric transformations

### Day 24 — Reflection and Scaling
- MIT18.06 + 3B
- Practice: predict transformed coordinates
- Code: reflection/scaling visualizer

### Day 25 — Shearing
- MIT18.06 / 3B transformation intuition
- Practice: shear matrices
- Code: animate shear of a grid
- Explain: matrix changes geometry

### Day 26 — Inverse Matrix
- 3B: inverse intuition
- MIT18.06: inverse
- Practice: 2x2 inverses
- Code: 2x2 inverse from formula, then NumPy verification
- AI link: solving transformations backward

### Day 27 — Determinant Intuition
- 3B: determinant
- MIT18.06: determinant meaning
- Practice: determinants of 2x2 and 3x3
- Code: determinant from recursive idea for small matrices
- Visualization: area/volume scaling

### Day 28 — PROJECT 2
## Matrix Transformation Studio
Build:
- 2D point cloud
- rotation, scaling, reflection, shear
- composition of transformations
- inverse transformation
- determinant/area change display
- README with geometric explanations

---

# PHASE 3 — Linear Systems, Elimination, Rank
## Days 29–49

### Day 29 — The (Ax=b) View
- MIT18.06: systems of linear equations
- Practice: translate equations into matrix form
- Code: create augmented matrices
- AI link: linear models

### Day 30 — Gaussian Elimination
- MIT18.06: elimination
- Practice: 2x2 and 3x3 systems
- Code: implement elimination from scratch

### Day 31 — Row Operations
- MIT18.06
- Practice: swap, scale, eliminate
- Code: functions for elementary row operations

### Day 32 — Row Echelon Form
- MIT18.06
- Practice: reduce matrices manually
- Code: implement REF

### Day 33 — RREF
- MIT18.06 + Book
- Practice: 10 RREF problems
- Code: implement RREF
- Verify selected cases with SymPy/NumPy

### Day 34 — Unique / Infinite / No Solution
- MIT18.06
- Practice: classify systems
- Code: build a system classifier

### Day 35 — WEEK 5 REVIEW
- One timed mixed problem set
- Rebuild Gaussian elimination without notes
- Debug your implementation
- GitHub commit

### Day 36 — Pivot Variables
- MIT18.06
- Practice: identify pivots/free variables
- Code: pivot detection

### Day 37 — Free Variables and Parametric Solutions
- MIT18.06
- Practice: write solution sets parametrically
- Code: represent free-variable solutions

### Day 38 — Column Space
- MIT18.06
- Practice: identify column space basis
- Code: experiment using pivot columns
- AI link: representable outputs

### Day 39 — Nullspace
- MIT18.06
- Practice: solve Ax=0
- Code: small nullspace solver
- AI link: non-unique parameter directions

### Day 40 — Rank
- MIT18.06
- Practice: calculate rank through pivots
- Code: implement rank from your elimination routine
- Verify with NumPy

### Day 41 — Rank-Nullity
- MIT18.06
- Practice: 15 rank-nullity questions
- Code: verify examples computationally
- Explain theorem in plain language

### Day 42 — Row Space
- MIT18.06
- Practice: basis for row space
- Code: basis extraction

### Day 43 — Four Fundamental Subspaces
- MIT18.06
- Learn row, column, null, left-null spaces
- Draw a conceptual map
- AI link: under/over-parameterization

### Day 44 — Existence and Uniqueness
- MIT18.06
- Practice: when does Ax=b have a solution?
- Code: build simple consistency tests

### Day 45 — Conditioning Preview
- Book / MIT supplemental material
- Understand sensitivity to small changes
- Code: perturb a system and compare solutions

### Day 46 — Numerical vs Exact Thinking
- Learn floating-point limitations
- Code: compare exact small systems with floating-point outputs
- AI link: numerical stability

### Day 47 — Problem Marathon
- 20 mixed problems from MIT/Book
- No videos
- Track errors by category

### Day 48 — PROJECT 3
## Gaussian Elimination From Scratch
Requirements:
- REF
- RREF
- pivot detection
- rank
- solution classification
- solve small Ax=b systems
- tests against known answers

### Day 49 — Project Review
- Refactor code
- Add tests
- Improve README
- Explain algorithm complexity
- Commit release version

---

# PHASE 4 — Vector Spaces, Basis, Dimension
## Days 50–63

### Day 50 — Vector Space Definition
- MIT18.06
- Practice: examples/non-examples
- Code: simple closure experiments

### Day 51 — Subspaces
- MIT18.06
- Practice: subspace tests
- Code: generate subspace points

### Day 52 — Basis
- 3B / MIT18.06
- Practice: find bases
- Code: basis extraction from columns

### Day 53 — Dimension
- MIT18.06
- Practice: dimension from rank
- Code: verify dimension examples

### Day 54 — Coordinates in a Basis
- Book + MIT18.06
- Practice: change coordinates
- Code: solve for coordinates in a custom basis

### Day 55 — Change of Basis
- MIT18.06
- Practice: basis conversion
- Code: change-of-basis matrix

### Day 56 — WEEK 8 REVIEW
- Mixed basis/dimension problems
- One visual explanation
- GitHub commit

### Day 57 — Linear Transformations
- 3B: linear transformations
- MIT18.06
- Practice: test linearity
- Code: create simple transformation functions

### Day 58 — Matrix Representation of a Transformation
- MIT18.06
- Practice: derive matrix from basis images
- Code: build transformation matrices

### Day 59 — Kernel and Image
- MIT18.06
- Practice: kernel/image examples
- Code: connect nullspace and column space

### Day 60 — Dimension Theorem
- MIT18.06
- Practice: rank-nullity from transformation viewpoint
- Explain verbally

### Day 61 — Composite Transformations
- 3B
- Practice: matrix composition
- Code: multi-stage transformation pipeline

### Day 62 — Invertible Transformations
- MIT18.06
- Practice: equivalence conditions
- Code: test invertibility for small matrices

### Day 63 — MINI PROJECT
## Linear Transformation Explorer
- custom basis
- coordinate conversion
- kernel/image demo
- composition
- inverse when available

---

# PHASE 5 — Orthogonality, QR, Least Squares
## Days 64–77

### Day 64 — Orthogonal Complements
- MIT18.06
- Practice: find orthogonal complements
- Code: numerical examples

### Day 65 — Orthonormal Bases
- MIT18.06
- Practice: normalize vectors
- Code: orthonormality checker

### Day 66 — Gram-Schmidt
- MIT18.06
- Practice: manually orthogonalize vectors
- Code: implement Gram-Schmidt

### Day 67 — Gram-Schmidt Visualization
- Visualize original vs orthogonalized basis
- Explain why the algorithm works

### Day 68 — QR Factorization
- MIT18.06 / later Strang material
- Practice: understand A=QR
- Code: implement QR via Gram-Schmidt

### Day 69 — Projections Revisited
- MIT18.06
- Practice: projection onto a subspace
- Code: projection matrix

### Day 70 — WEEK 10 REVIEW
- 15 mixed problems
- Rebuild Gram-Schmidt from memory
- GitHub commit

### Day 71 — Least Squares
- 3B / MIT18.06
- Learn why exact solution may not exist
- Practice: small overdetermined systems
- Code: least-squares approximation

### Day 72 — Normal Equations
- MIT18.06
- Understand (A^TAx=A^Tb)
- Derive it geometrically

### Day 73 — Linear Regression Mathematics
- Connect least squares to regression
- Code: regression coefficients using linear algebra
- No sklearn

### Day 74 — Bias Term and Design Matrix
- Practice feature matrix construction
- Code: add intercept column
- AI link: supervised learning

### Day 75 — Regression Visualization
- Fit synthetic data
- Plot data + line
- Compare prediction error

### Day 76 — Least Squares vs Gradient Descent
- Understand two routes to regression
- Code both on a tiny dataset
- Compare speed/behavior conceptually

### Day 77 — PROJECT 4
## Linear Regression From Scratch
Build:
- data generation
- design matrix
- closed-form solution
- predictions
- MSE
- visualization
- comparison with sklearn
- clear explanation of the linear algebra

---

# PHASE 6 — Eigenvalues, Eigenvectors, Diagonalization
## Days 78–91

### Day 78 — Eigenvalue Intuition
- 3B: eigenvectors/eigenvalues
- MIT18.06
- Practice: identify simple eigenvectors
- Code: matrix-vector experiments

### Day 79 — (Av=\lambda v)
- MIT18.06
- Practice: verify eigenpairs
- Code: eigenpair checker

### Day 80 — Characteristic Equation
- MIT18.06
- Practice: 2x2 characteristic polynomials
- Code: small-matrix eigenvalue solver conceptually

### Day 81 — Eigenspaces
- MIT18.06
- Practice: find eigenspaces
- Code: connect eigenvectors to nullspaces

### Day 82 — Geometric Visualization
- 3B
- Code: transform many vectors and highlight eigen-directions
- Explain what changes and what does not

### Day 83 — Symmetric Matrices
- MIT18.06
- Learn special properties
- Practice: orthogonal eigenvectors

### Day 84 — WEEK 12 REVIEW
- Mixed eigenvalue problems
- Visualization
- GitHub commit

### Day 85 — Diagonalization
- MIT18.06
- Practice: construct A=PDP^-1
- Code: diagonalization verification

### Day 86 — Powers of Matrices
- MIT18.06
- Practice: use diagonalization conceptually
- Code: compare direct powers vs diagonalized form

### Day 87 — Quadratic Forms
- MIT18.06
- Practice: evaluate x^TAx
- Code: surface/contour experiments for 2D

### Day 88 — Positive Definite Matrices
- MIT18.06
- Practice: recognize positive definiteness
- AI link: optimization and covariance

### Day 89 — Covariance Matrix
- MIT18.065 preview
- Build covariance matrix from data
- Visualize covariance directions

### Day 90 — Eigenvalues Meet Data
- MIT18.065: PCA-related material
- Understand principal directions
- Code: eigenvectors of covariance matrix

### Day 91 — PROJECT 5
## Eigenvalue & Eigenvector Visualizer
Build:
- matrix input
- vector transformation
- eigenpair verification
- graphical eigen-directions
- diagonalization demo for suitable matrices

---

# PHASE 7 — SVD, PCA, ML Applications
## Days 92–105

### Day 92 — Why SVD?
- 3B: SVD-related intuition where available
- MIT18.06 / MIT18.065
- Understand factorization purpose

### Day 93 — Singular Values and Vectors
- MIT18.065
- Practice conceptually
- Code: compute SVD with NumPy and inspect U, Sigma, Vt

### Day 94 — Low-Rank Approximation
- MIT18.065
- Code: reconstruct matrix with top-k singular values
- Explain rank-k approximation

### Day 95 — SVD Visualization
- Visualize matrix action as rotations/scaling/rotations
- Compare original and reconstructed data

### Day 96 — Image Compression
- Code: grayscale image -> SVD -> reconstruction
- Compare k=5, 20, 50, 100

### Day 97 — WEEK 14 REVIEW
- Explain SVD without formulas first
- Then explain (A=U\Sigma V^T)
- GitHub commit

### Day 98 — PCA Foundations
- MIT18.065
- Center data
- Compute covariance
- Understand principal direction

### Day 99 — PCA with Eigenvectors
- MIT18.065
- Code PCA from scratch using covariance + eigendecomposition

### Day 100 — PCA Dimensionality Reduction
- Reduce 2D/3D synthetic data
- Visualize before/after
- Explain information retention

### Day 101 — PCA on Real Dataset
- Use a small public dataset
- Standardize/center appropriately
- Apply PCA from scratch

### Day 102 — PCA Verification
- Compare from-scratch results with sklearn
- Explain numerical/order differences

### Day 103 — Embeddings and Vector Spaces
- Understand high-dimensional representations
- Code nearest-neighbor search using cosine similarity
- AI link: embeddings

### Day 104 — Matrix Factorization in Recommenders
- Build a toy user-item matrix
- Explore low-rank structure
- AI link: recommendation systems

### Day 105 — PROJECT 6
## PCA From Scratch + SVD Image Compression
Deliverables:
- PCA implementation
- SVD reconstruction
- plots
- explanation of eigenvalues vs singular values
- applications section

---

# PHASE 8 — Neural Networks, Optimization Connections, Mastery
## Days 106–112

### Day 106 — Linear Algebra Inside Neural Networks
- MIT18.065: neural networks
- Study (z=Wx+b)
- Code one dense layer from scratch

### Day 107 — Forward Pass
- Build 2-layer network forward pass with NumPy
- Track every vector/matrix shape

### Day 108 — Gradients as Vectors
- Connect vectors to optimization
- Review gradient intuition
- Code simple gradient calculations

### Day 109 — Jacobian/Hessian Preview
- Learn the role of Jacobian and Hessian
- Do not deep-dive yet
- AI link: optimization/backpropagation

### Day 110 — End-to-End Mathematics for One ML Model
Choose one:
- linear regression
- PCA
- 2-layer neural network

Write the mathematics, code, plots, and explanation in one notebook.

### Day 111 — MASTER REVIEW
Without notes:
- explain vectors
- matrices
- spaces
- rank
- orthogonality
- least squares
- eigenvalues
- SVD
- PCA
- neural-network matrix operations

Solve one mixed problem from every major area.

### Day 112 — CAPSTONE
## Mathematics for AI — Linear Algebra Mastery Portfolio

Combine the strongest work into:
1. Vector Geometry Explorer
2. Matrix Transformation Studio
3. Gaussian Elimination
4. Linear Regression From Scratch
5. Eigenvalue Visualizer
6. PCA + SVD

Create a polished README with:
- what you learned
- mathematical concepts
- from-scratch algorithms
- visualizations
- AI/ML applications
- lessons learned
- future mathematics roadmap

Tag the repository milestone: `linear-algebra-v1.0`.

---

# Mastery Checklist

Do not mark Linear Algebra “done” unless you can:

- [ ] Explain vectors geometrically
- [ ] Compute and visualize dot products
- [ ] Explain matrices as transformations
- [ ] Implement matrix multiplication
- [ ] Solve systems using Gaussian elimination
- [ ] Explain span, basis, dimension, independence
- [ ] Explain rank and nullspace
- [ ] Explain the four fundamental subspaces
- [ ] Implement Gram-Schmidt
- [ ] Explain least squares
- [ ] Build linear regression from scratch
- [ ] Explain eigenvalues/eigenvectors geometrically
- [ ] Understand diagonalization
- [ ] Explain SVD conceptually
- [ ] Implement SVD-based image compression
- [ ] Implement PCA from scratch
- [ ] Explain where each concept appears in AI/ML
- [ ] Write clean NumPy/Matplotlib implementations
- [ ] Explain your work without reading notes

# GitHub Daily Habit

Every completed day should normally produce:
- 1 notebook or code file
- 1 short Markdown note
- 1 Git commit

Suggested commit messages:
- `day-01: start linear algebra foundations`
- `day-17: implement matrix multiplication`
- `day-30: implement gaussian elimination`
- `day-73: linear regression from scratch`
- `day-99: implement PCA`

# Important Rule

Use library functions for **verification**, not as a replacement for understanding.

The long-term goal is:
**Math → Code → Visualization → Application → Explanation**
