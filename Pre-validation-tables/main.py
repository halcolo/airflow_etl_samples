from src.models.yaml import Yaml
from src.utils.rdd import create_spark
from src.utils.read_file import read_csv

if __name__ == '__main__':

    yaml = Yaml(source='Local', yaml_route='sample.yml')
    yaml = yaml.get_yaml_decoded()
    df = read_csv(yaml['source'])
    spark_df = create_spark(df, 'Test_Spark_rdd')
    spark_df.show() 
