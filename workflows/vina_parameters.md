# AutoDock Vina parameters

Vina was run using a shared configuration file (`config.txt`) specifying the search space and sampling settings.

## Receptor
- `pdbqts/PmrB_receptor.pdbqt`

## Ligands
- `pdbqts/*_chainB.pdbqt`

## Search space and sampling
Populate this section from `config.txt`:
- centre (x, y, z):
- box size (x, y, z):
- exhaustiveness:
- num_modes (if set):
- energy_range (if set):

## Output
- Docked poses: `results/<ligand>_out.pdbqt`
- Logs: `results/<ligand>.log`
