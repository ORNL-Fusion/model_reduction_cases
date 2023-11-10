# Introduction

This is a model reduction case for ecrh heading power and position.

## Inputs
* ec_freq ECRH Frequency.
* ec_thet 
* ec_phai
* ec_theta
* r Major Radius
* bt Toroidal Magnetic Field
* ip Plasma current
* h98 Confinement factor
* ec_pinj Injected ecrh power
* kappa 
* nepeak Peak Density
* aratio Aspect Ratio

## Outputs
* irf Bootsrtap Fraction
* prfe ECRH Heating power

## Files

* constrints.py Filtering constraint plugin.
* current_msr_state.zip State file for the massive parallel runner.
* ips.massive_parallel_runner.config IPS config for the massive parallel runner.
* ips.ml_train.config IPS config for the machine learning workflow.
* model_config.json Specification of model inputs and outputs and their input ranges.
* platform.config IPS config for the perlmutter.
* submitjob Batch file to submit the job.
* training_args.json The arguments for the ml model and training.

# Control parameters

## ips.ml_train.config

* OUTPUT_LEVEL Show or hide diagnostic information.
* BATCH_SIZE Maximum number of entries in a new training batch.
* MSR_NNODES Number of nodes used. Must match value in the submitjob file.
* MAX_ITERATIONS Number of adapative steps to run.
* SAVE_LOGS Save task log files for debuging.

## submitjob

* --qos NERSC Job queue.
* --nodes Number of nodes to use.
* -t Maximum allowed run time.
* -J Job name.
* -e Error output.
* -o Stadard output.
* WORK_DIRECTORY Directory on SCRATCH to run the workflow.

# Constraints

Filtering constraints can be added in the constraints.py file. Constraints take
the form of a python function and manifest entry. Constraints can be applied to 
any combination of the model input and outputs.

```
import tensorflow

def example(arg1, arg2):
    return tensorflow.math.logical_and(arg1/arg2 >= 0.0, arg1/arg2 <= 0.0)

manifest = [
    {'function' : example,  'args' : ['input1', 'input2']}
]
```
