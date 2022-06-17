# Model equilibrium case.

This is just a simple tokamak equilibrium with no external heating and current
drive.

## Running

In the `ips.ml_train.config`, `MSR_NNODES` should match the number of requested
nodes in the `submitjob` script. To fully utilize the available cores 
`BATCH_SIZE` should be the number of nodes times 32.

The batch script will delete the working directory on `$SCRATCH` so change the
`$WORK_DIRECTORY` variable if you want to save the data.
