## Search space and sampling

The docking search space was defined to encompass the full PmrB cytosolic domain:

- Centre (Å):
  - x = -31.14
  - y = -0.60
  - z = 22.68

- Box size (Å):
  - x = 70
  - y = 30
  - z = 50

- Sampling:
  - exhaustiveness = 16
  - num_modes = 10
  - energy_range = 4 kcal/mol

These parameters were chosen to allow full exploration of the PmrB cytosolic region while maintaining feasible runtimes on the Glasgow HPC cluster.
