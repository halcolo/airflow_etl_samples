import pandas as pd

def read_csv(filepath, encoding="utf-8"):
    # Open file stream
    with open(filepath) as fp:
        # Reading CSV in pandas
        df = pd.read_csv (filepath)
        # Return created DataFrame
        return df


def read_avro(filepath, encoding="utf-8"):
    import fastavro
    # Open file stream
    with open(filepath, encoding) as fp:
        # Configure Avro reader
        reader = fastavro.reader(fp)
        # Load records in memory
        records = [r for r in reader]
        # Populate pandas.DataFrame with records
        df = pd.DataFrame.from_records(records)
        # Return created DataFrame
        return df