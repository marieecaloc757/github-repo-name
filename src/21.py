import numpy as np
import pandas as pd

def process_data(input_data):
    # Process and analyze input data
    processed_data = input_data.apply(lambda x: "Processed_" + str(x) + "_data")
    return processed_data
