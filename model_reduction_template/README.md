# Introduction
This is a template case for running the adapative training to produce reduced machine learning models. This workflow consists of 3 workflows.

## `ips_ml_train`
This workflow trains the model and generates a new batch of model inputs to generate training data for.

### Input files
* `ips.ml_train.config` The ips config for the main workflow.
* `platform.conf` The ips config for the subworkflow.
* `model_config.json` Parameters to control the topology of the neural network model.
* `training_args.json` Command line arguments for the model training parameters.
* `constraints.py` Constraint plugin to filter out training data.
* `ips.massive_parallel_runner.config` The ips config for the model generation subworkflow.
* `current_msr_state.zip` State file for the data ganeration subworkflow.

#### `ips.ml_train.config`
Important parameters that must be set.
* `BATCH_SIZE` Number of elemets to make per batch.
* `MSR_NNODES` Number of available nodes.
* `MAX_ITERATIONS` Total number of adaptiations to take.
* `TRAINING_DATA` Name of the training data file.
* `NEW_DATA` Name of new data batch file.
* `PREDICTION_DATA` Name of the prediction data file.
* `NN_MODEL_CONFIG` Name should match the name of the model config input file.
* `NN_MODEL_MATRIX` Name of the parameter covariance matrix file.
* `NN_MODEL` Name of the saved model.
* `ML_TRAIN_ARGS` Name should match the name of the training command line arguments.
* `CURRENT_ML_TRAIN_STATE` Name of the workflow state file.
* `DATA_GEN_CONFIG` Should match the name of the ips config for the data generation subworkflow.
* `DATA_GEN_STATE` Should match the name of the data generation subworkflow file.
* `MODULE_PATH` Path to the constraints file.
* `MODULE_NAME` Should match the constraints file name without the `.py`.

#### `model_config.json`
This is a json file defining the inputs and outputs of the model.
<pre><code>{
  "inputs" : [
    {"name" : <i><b>"foo"</b></i>, "upper_range" : <i><b>high value</b></i>, "lower_range" : <i><b>lower value</b></i>},
    ...
  ],
  "outputs" : [
    {"name" : <i><b>"bar"</b></i>, "upper_range" : <i><b>high value</b></i>, "lower_range" : <i><b>lower value</b></i>},
    ...
  ]
}</code></pre>

#### `training_args.json`
<pre><code>{
  <i><b>"--arg"</b></i> : <i><b>value</b></i>,
  ...
}</code></pre>
* `--activation` The activation function of the neural network.
* `--iterations` Number of times to work through the epochs.
* `--epochs` Number of training epochs to run.
* `--num_layers` Number of layers in the neural network.
* `--layer_width` Number of neurons in a layer.
* `--l1_factor` l1 regularisation factor.
* `--l2_factor` l2 regularisation factor.
* `--validation_split` Percentage of training data to reserve for validation.
* `--locations` Number of areas to generate adpative data for.
* `--adaptive_percentage` Percentage of the input parameter range to sample new data.

#### `constraints.py`
This is a python module of constraint filering functions. The format of this module includes the functions and a manifest that defines how model parameters map to function inputs.
<pre><code>import tensorflow

def constraint(foo, bar):
  return tensorflow.math.logical_and(foo/bar >= <i><b>lower range</b></i>, foo/bar <= <i><b>upper range</b></i>)
    
...

manifest = [
  {'function' : constraint, 'args' : ['foo', 'bar']},
  ...
]</code></pre>

## `ips_massive_parallel_runner`
This workflow converts the between model training workflow and the data generation workflow.

### Input files
* `ips.massive_parallel_runner.config` The massive parallel runner config file.
* `current_msr_state.zip` The massive parallel runner state file.

#### `current_msr_state.zip`
The state file for data generation workflow.
* `sample.json` TokDesigner sampling config file.
* `makedb.json` TokDesigner make database.
* `ips_massive_parallel.config` Massive parallel ips config file.
* `massive_parallel_state.zip` State file of for the massive parallel state.

#### `ips.massive_parallel_runner.config`
This is the IPS config file for the data generation subworkflow.
* `MSR_GLOBAL_CONFIG` Needs to match the ips config file in the data generation state file.
* `MSR_SERIAL_STATE` Massive parallel state file.
* `DATABASE_CONFIG` Needs to match the database config in the data generation state file.
* `INSCAN_CONFIG` Needs to match the sample config in the data generation state file.
