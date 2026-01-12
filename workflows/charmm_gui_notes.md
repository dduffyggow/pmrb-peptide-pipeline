# CHARMM-GUI membrane construction

Membrane systems were generated using **CHARMM-GUI Membrane Builder** and exported for GROMACS.

## System
- Protein: PmrB
- Lipid: POPE bilayer
- Water model: TIP3P
- Ions: K⁺ and Cl⁻ added to neutralise and approximate physiological ionic strength

## Workflow
1. Upload PmrB structure (AlphaFold/ColabFold)
2. Define transmembrane orientation
3. Build lipid bilayer around protein
4. Solvate and ionise
5. Export to GROMACS

CHARMM-GUI produced:
- `system.gro`
- `topol.top`
- `toppar/` with lipid and forcefield parameters
- `mdp/` templates for EM, NVT, NPT, and production MD

These files were used directly on the Glasgow HPC cluster.
