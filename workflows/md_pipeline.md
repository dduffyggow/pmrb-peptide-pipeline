# Molecular dynamics pipeline (CHARMM-GUI → GROMACS)

This document describes how peptide and membrane systems were prepared and simulated using GROMACS as part of the PmrB–peptide interaction study.

Two physically distinct simulation regimes were used:

1. **Peptide in water** – baseline peptide stability and binding physics  
2. **Membrane-embedded PmrB** – biologically relevant lipid-bilayer environment  

---

## 1. Peptide in water (DCR1 example)

A fully reproducible example is provided in:

data/example_md/example_md_water_dcr1.tar.gz


This archive contains:
- ColabFold structure (`Dcr1_colabfold.pdb`)
- GROMACS coordinate files (`dcr1_processed.gro`, `dcr1_newbox.gro`, `dcr1_solv_ions.gro`)
- `topol.top` and position-restraint files
- `.mdp` files for energy minimisation, NVT, NPT, and production MD

### Typical workflow

```bash
tar -xzf example_md_water_dcr1.tar.gz
cd export_md_water_dcr1

gmx grompp -f mdp/em.mdp  -c dcr1_solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -deffnm em

gmx grompp -f mdp/nvt.mdp -c em.gro -p topol.top -o nvt.tpr
gmx mdrun -deffnm nvt

gmx grompp -f mdp/npt.mdp -c nvt.gro -p topol.top -o npt.tpr
gmx mdrun -deffnm npt

gmx grompp -f mdp/md.mdp  -c npt.gro -p topol.top -o md.tpr
gmx mdrun -deffnm md


2. Membrane-embedded PmrB

A CHARMM-GUI–generated membrane system was used to simulate PmrB in a lipid bilayer.

Reproducible inputs are provided in:

data/example_md/example_md_membrane_small_bilayer.tar.gz

This archive contains:

system.gro (protein + bilayer + solvent)

topol.top

index.ndx

mdp/ (em, nvt, npt, md)

toppar/ (CHARMM-GUI forcefield and lipid parameters)

Typical workflow
tar -xzf example_md_membrane_small_bilayer.tar.gz
cd export_md_membrane_small_bilayer

gmx grompp -f mdp/em.mdp  -c system.gro -p topol.top -o em.tpr
gmx mdrun -deffnm em

gmx grompp -f mdp/nvt.mdp -c em.gro -p topol.top -o nvt.tpr
gmx mdrun -deffnm nvt

gmx grompp -f mdp/npt.mdp -c nvt.gro -p topol.top -o npt.tpr
gmx mdrun -deffnm npt

gmx grompp -f mdp/md.mdp  -c npt.gro -p topol.top -o md.tpr
gmx mdrun -deffnm md


---

## Step 4 — commit
Scroll down to the commit box and use:

- **Commit message:** `Add molecular dynamics workflow`
- Leave the option as **Commit directly to the main branch**
- Click **Commit changes**

---

## Step 5 — then we add the CHARMM-GUI notes file
Once `md_pipeline.md` appears in this `workflows/` list, tell me and I’ll give the next exact steps for `charmm_gui_notes.md`.
