# Docking pipeline (AutoDock Vina)

This document describes the command-line workflow used to prepare PmrB and peptide structures for docking and to run AutoDock Vina on the University of Glasgow HPC cluster (“Mars”).

## Inputs
- Receptor structure: PmrB cytosolic domain (PDB format; cleaned prior to docking)
- Peptide structures: ColabFold outputs (5 models per peptide), with the highest-confidence model selected by pLDDT
- Output format: PDBQT for both receptor and ligand

## Overview of steps
1. Select highest-confidence peptide model from ColabFold outputs
2. Clean/standardise PDBs (e.g., with pdbfixer where required)
3. Convert receptor and ligand PDB → PDBQT
4. Run AutoDock Vina with a defined search space and exhaustiveness
5. Parse Vina outputs and extract best binding affinity

## Notes on use in dissertation
AutoDock Vina was implemented as a benchmarking docking pipeline alongside HADDOCK. Vina produced stable results for all ARPs and a subset of DCRs, but convergence failures for several DCR peptides led HADDOCK to be used for final reported binding affinities.
