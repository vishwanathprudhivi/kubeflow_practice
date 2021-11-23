from kfp.v2 import compiler
from kfp.v2 import dsl
from kfp.v2.dsl import Input, InputPath, Output, OutputPath, Dataset, Model, component


@component
def load_data(

)

@component
def transform_and_save()

# The main pipleine responsible for orchestrating individual steps
@dsl.pipeline(pipeline_root='', name='example_kfp_pipeline')
def pipeline():
    # Read data set from GCS
    load_data()
    # Apply data transformations
    transform_and_save()
    # Save the data to GCS
    


if __name__ == '__main__':
    compiler.Compiler().compile(
        pipeline_func=pipeline, package_path=__file__.replace('.py', '.yaml'))
