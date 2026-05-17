# Verification Layer

This folder contains verification scripts for the current DOT package.

## Main finite-core verification

```bash
python3 01_Verification/DOT_Core_verifier.py
```

Checks:

- the pre-core binary layer;
- the minimal six-state carrier;
- \(U_3\), \(R_1,R_2,R_3\);
- \(C_6\), \(K_3\sqcup K_3\), \(3K_2\), \(K_{2,2,2}\);
- chambers, transport, and holonomy;
- shell laws of higher ranks;
- part of the operator-combinatorial interface.

This script is a useful regression check for the finite core. It checks
finite combinatorial claims; the conceptual reading of scene, observer,
reductions, and active boundary is fixed in the text volumes.

## AMR verification

```bash
python3 01_Verification/DOT_AMR_verifier.py self-test
python3 01_Verification/DOT_AMR_verifier.py core-check
```

AMR belongs to a future arithmetic branch. In the current Volumes 0-6 it
is not part of the main proof path.

## Algebraic bridge \(A_2/\mathfrak{sl}_3/\mathfrak{su}(3)\)

```bash
python3 01_Verification/verify_six_state_a2_sl3_su3.py
```

Standalone verification of the six-state bridge through \(A_2\),
\(\mathfrak{sl}_3\), and \(\mathfrak{su}(3)\).

## Cryptographic spectral block

```bash
python3 01_Verification/verify_cryptographic_spectral_block.py
```

Checks a separate spectral-cryptographic theorem package. This block is
kept as an appendix, not as part of the main corpus.

## Dependencies

```bash
python3 -m pip install -r requirements.txt
```

Current dependency:

```text
numpy
```
