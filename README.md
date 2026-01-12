# PmrB Peptide Interaction Pipeline

This repository contains the computational pipeline developed for the MSci dissertation of **Derbhla Duffy (University of Glasgow, 2026)**, modelling the interaction of de novo random peptides (DCRs/ARPs) with the **PmrB sensor kinase**.

The project investigates whether short, randomly generated peptides can bind to and modulate PmrB, a two-component regulatory sensor implicated in antimicrobial resistance. The pipeline integrates **structure prediction, molecular docking, and molecular dynamics** to evaluate peptide–PmrB interactions.

---

## Pipeline documentation

This repository is organised as a reproducible computational workflow:

1. **Structure prediction**
   - ColabFold was used to predict peptide and PmrB structures
   - Highest-confidence models were selected by pLDDT

2. **Docking (AutoDock Vina)**
   - Workflow: `workflows/docking_pipeline.md`
   - Parameters: `workflows/vina_parameters.md`

3. **Molecular dynamics (CHARMM-GUI → GROMACS)**
   - Workflow: `workflows/md_pipeline.md`
   - Membrane system preparation: `workflows/charmm_gui_notes.md`

4. **Example data**
   - Docking inputs: `example_inputs_pdbqt.tar.gz`
   - Peptide-in-water MD: `example_md_water_dcr1.tar.gz`
   - Membrane MD: `example_md_membrane_small_bilayer.tar.gz`

---

## Scientific Context

De novo random peptides (DCRs) and adaptive random peptides (ARPs) have been shown experimentally to alter bacterial phenotypes, including antibiotic resistance, through poorly understood molecular mechanisms. This project tests the hypothesis that a subset of these peptides directly interact with the PmrB cytosolic domain, potentially altering signalling in the PmrA/B two-component system.

---

## Pipeline Overview

The pipeline consists of the following stages:

1. **Peptide generation**  
   Random peptide sequences are generated using a custom Python script.

2. **Structure prediction**  
   Peptide and receptor structures are predicted using **AlphaFold / ColabFold**.

3. **Model selection**  
   For each peptide, the highest-confidence structure (by pLDDT) is automatically selected from ColabFold outputs.

4. **Structure preparation**  
   Structures are cleaned and converted to AutoDock-compatible formats (PDB → PDBQT).

5. **Molecular docking**  
   Peptides are docked against PmrB using **AutoDock Vina**.

6. **Molecular dynamics (MD)**  
   Selected complexes are prepared and simulated using **GROMACS**, including both water and membrane-embedded systems.

---

## Vina vs HADDOCK

AutoDock Vina was implemented as an independent docking pipeline to benchmark against **HADDOCK** predictions.  
While Vina produced stable results for all ARPs and a subset of DCR peptides, convergence failures for several DCRs led **HADDOCK** to be used for the final reported binding affinities in the dissertation.

The Vina pipeline is included here to ensure full methodological transparency and reproducibility.

---

## Repository Structure




---

## Reproducibility

All docking, structure processing, and molecular dynamics preparation were performed using this pipeline on the University of Glasgow HPC cluster (“Mars”).  
Exact command lines, configuration files, and software versions are provided in this repository.

---

## Citation

If you use or reference this pipeline, please cite:

> Duffy, D. (2026). *Computational modelling of de novo peptide interactions with the PmrB sensor kinase*. MSci Dissertation, University of Glasgow.


---

## Reproducibility and computational workflows

This repository provides fully reproducible computational pipelines and example input systems for the docking and molecular dynamics analyses used in this dissertation.

### Docking (AutoDock Vina)
- Workflow: `workflows/docking_pipeline.md`
- Parameters: `workflows/vina_parameters.md`
- Example inputs: `example_inputs_pdbqt.tar.gz`

### Molecular dynamics (CHARMM-GUI → GROMACS)
- Workflow: `workflows/md_pipeline.md`
- CHARMM-GUI membrane setup: `workflows/charmm_gui_notes.md`
- Example systems:
  - Peptide in water: `data/example_md/example_md_water_dcr1.tar.gz`
  - PmrB in membrane: `data/example_md/example_md_membrane_small_bilayer.tar.gz`

These archives allow the docking and MD workflows to be reproduced from raw structures using the same parameters applied in the MSci project.

---

## Contact

For questions about this repository or the associated research, please contact  
**Derbhla Duffy** — University of Glasgow.
