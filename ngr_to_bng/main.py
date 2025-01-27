from ngr_to_bng.converter import csv_converter
from logging import getLogger
import sys
from ngr_to_bng.utils import get_logger

logger = get_logger(name=__name__)

def main():
    """ Handles csvs only right now """

    arg_len = len(sys.argv)
    fp = sys.argv[1] if arg_len > 1 else 'data.csv' # could use input() or even just statically assign this path
    valid_file_types = ['csv']
    if not fp.endswith(tuple(file_type for file_type in valid_file_types)):
        logger.error(f"This file type is current not supported. Current input file types supported include:\n{", ".join(valid_file_types)}")
        return   
    col_name = 'ngr' 
    
    if arg_len > 2:
        col_name = sys.argv[2]
    else:
        col_name = 'ngr'
        logger.warning("You have not defined the column name for National Grid Ref. Default assumption of 'ngr' taken")
    csv_converter(fp = fp, col_name = col_name)

if __name__ == "__main__":
    main()

