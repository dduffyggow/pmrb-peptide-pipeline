Notebook workflow (structure generation → docking)

These notebooks implement the preprocessing pipeline that feeds into ColabFold and AutoDock Vina.

1. Generate random peptide sequences

01_generate_randseq.ipynb

This notebook queries the ExPASy RandSeq server to generate random amino-acid sequences with user-defined length and composition.
It outputs a multi-FASTA file (randseq_merged.fasta) suitable for direct input into ColabFold.

Alternatively, users may skip this step and provide their own peptide FASTA sequences.

2. Structure prediction (ColabFold)

Structures were generated using LocalColabFold (Mirdita et al., 2022; Jumper et al., 2021):

https://github.com/YoshitakaMo/localcolabfold

ColabFold takes the peptide FASTA file and produces multiple structural models per sequence in JSON and PDB format.

3. Select the highest-confidence ColabFold models

02_select_colabfold_models.ipynb

ColabFold produces multiple candidate models for each sequence.
This notebook parses the ColabFold JSON output and selects the highest-confidence model (based on predicted confidence scores such as pLDDT / ranking_confidence), exporting the chosen structures as PDB files for docking.

4. Convert structures for AutoDock Vina

03_convert_pdb_to_pdbqt.ipynb

AutoDock Vina requires receptor and ligand structures in PDBQT format.
This notebook uses Open Babel to convert ColabFold-generated PDB files into PDBQT files prior to docking.

The resulting PDBQT files are then used by the AutoDock Vina pipeline (scripts/).
