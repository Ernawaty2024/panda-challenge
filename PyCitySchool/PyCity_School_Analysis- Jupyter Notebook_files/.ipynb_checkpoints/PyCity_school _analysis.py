# -*- coding: utf-8 -*-
"""
#Created on Mon May 13 22:05:12 2024

#@author: Ernie
"""

# Dependencies and setup

import pandas as pd
from pathlib import Path

# File to Load

students_data_to_load = Path(r"C:\Users\Ernie\Documents\GitHub\panda-challenge\PyCitySchool\Resources\students_complete.csv")
school_data_to_load = Path(r"C:\Users\Ernie\Documents\GitHub\panda-challenge\PyCitySchool\Resources\school_complete.csv")

# Read School and Student Data file and store into Pandas DataFrames
students_data = pd.read_csv(students_data_to_load)
school_data = pd.read_csv(school_data_to_load)

# Combine the data into a single dataset.
school_data_complete = pd.merge(students_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete.head()