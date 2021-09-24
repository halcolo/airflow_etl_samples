import great_expectations as ge
from great_expectations.checkpoint import LegacyCheckpoint


# Create context
context = ge.data_context.DataContext()


# Define kargs and Checkpoint
batch_kwargs_2 = {
    'path': '/Users/juandiegoalfonsoocampo/Documents/code/data_engineering/data_validations/data/yellow_tripdata_sample_2019-02.csv',
    "datasource": "data__dir",
    "data_asset_name": "yellow_tripdata_sample_2019-02.csv",
}

checkpoint_name = "taxi_checkpoint"
my_checkpoint = LegacyCheckpoint(
    name=checkpoint_name,
    data_context=context,
    batches=[
        {
          "batch_kwargs": batch_kwargs_2,
          "expectation_suite_names": ["taxi.demo"]
        }
    ]
)

# And here we just run validation!
results = my_checkpoint.run()

# Save the Checkpoint to your Data Context
my_checkpoint_json = my_checkpoint.config.to_json_dict()
context.add_checkpoint(**my_checkpoint_json)

# And here's how you can load it from your Data Context again
my_loaded_checkpoint = context.get_checkpoint(checkpoint_name)

# And then run validation again if you'd like
my_loaded_checkpoint.run()

validation_result_identifier = results.list_validation_result_identifiers()[0]
context.build_data_docs()
context.open_data_docs(validation_result_identifier)