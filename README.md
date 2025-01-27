# NGR to BNG Converter

This project provides a simple Python script to convert National Grid References (NGR) into British National Grid (BNG) Easting and Northing coordinates. It reads data from a CSV file and performs the conversion on a specified column containing NGR values.

## Overview

National Grid References (NGRs) are a common system used in the UK to represent geographic locations. This script will convert NGR values (e.g., `SP123456`) into their corresponding British National Grid (BNG) Easting and Northing coordinates. 

## Features

- **Input**: Accepts a CSV file containing National Grid References.
- **Automatic Column Detection**: If no column name is provided, the script will automatically search for a column named `ngr` in the CSV file.
- **Output**: Converts NGR values to BNG Easting and Northing values, which are suitable for mapping or spatial analysis.
  
## Usage

### Running the Script

To run the script, use the following command:

file_name will default to `data.csv` and column name to `ngr`
```bash
python ngr_to_bng/main.py <file_name.csv> <column_name>
