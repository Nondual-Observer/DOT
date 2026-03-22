# DOT Note: Yang–Mills Mass Gap (Conditional Reading)

**Status:** explanatory note (conditional on DOT axioms)  
**Scope:** this is *not* a Clay Millennium Prize solution text.

## What the Clay problem asks (informal)

The Clay “Yang–Mills existence and mass gap” problem is a **continuum** statement: construct a 4D quantum Yang–Mills theory for a compact gauge group (typically formulated as $SU(N)$) satisfying standard axioms, and prove that the spectrum has a **strictly positive** mass gap.

## What DOT provides (conditional on adopting the discrete carrier)

DOT starts from a **finite discrete carrier** $K(2,2,2)$ (octahedral graph / complete tripartite graph) and a nilpotent boundary operator $\partial$ with $\partial^2 = 0$, then builds a readout in which:

- the relevant spectral object is the carrier Laplacian (or adjacency) whose spectrum is **discrete**;
- “excitations” are organized by spectral subspaces and by a defect functional $\mathcal{D}$ over the 64 binary configurations of the carrier;
- nonzero defect sectors have a **strict positive lower bound** in the carrier normalization (in particular, $\mathcal{D}_{\min} > 0$ in the defect classification).

In this internal reading, a “mass gap” is not surprising: it is a direct consequence of working on a finite carrier with discrete spectrum and a defect quantization.

## Why this is not a Clay proof (and should not be stated as such)

Even if DOT gives a compelling *interpretation* of where a gap “comes from”, this does **not** by itself establish the Clay statement, because:

- Clay asks for a continuum QFT with specific analytic properties (existence, axioms, renormalization control);
- a discrete carrier model with a discrete spectrum does not automatically imply the existence of the corresponding continuum theory;
- identifying DOT defect sectors with Yang–Mills states is an additional bridge that must be made precise.

Therefore, the correct publishable claim is:

> **Within DOT’s discrete-carrier formalism, a positive gap is structurally natural and explicitly visible as a spectral/defect quantization.**  
> This is an internal explanation and reframing, not a proof of the Clay continuum problem.

## What would be needed for a genuine external bridge

To even attempt a “Clay-level” alignment one would need (at minimum):

- a mathematically explicit map from DOT’s carrier dynamics to a continuum Yang–Mills functional integral / Hamiltonian framework;
- a proof that the relevant continuum limit exists and preserves the gap (or a theorem that no such limit is needed because the discrete carrier is the fundamental object);
- a careful statement of what replaces standard axioms (Wightman/Osterwalder–Schrader) and how observables are recovered.

Until such bridges are written and checked, DOT should treat Yang–Mills as an **interpretive corollary** rather than a solved millennium problem.

