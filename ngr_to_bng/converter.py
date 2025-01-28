
from ngr_to_bng.ngr_lookup import ngr_lookup
from ngr_to_bng.validation import validate_ngr_input, NGRCodeError, NGRCoordLengthError
import re
import csv
from ngr_to_bng.utils import get_logger

logger = get_logger(name=__name__)
 
def convert_ngr_to_bng(ngr: str) -> tuple[int]:
    """ Takes National Grid Reference (NGR) and splits it into an Easting and Northing tuple."""
    ngr = re.sub(r"\s", '', ngr)
    validate_ngr_input(ngr) #treturns valid ngr

    prefix = ngr[:2]
    coords = ngr[2:]
    
    #left hand side is easting always and will always be reflected by equal right hand side legnth - error handled in validate method
    divider = int(len(coords)/2)
    easting_value = (coords[:divider])
    northing_value = (coords[divider:])
    
    prefix_values: dict = ngr_lookup.get(prefix)

    easting_pref_value = prefix_values.get('east') # number of m the bottom left of 100km grid square is east of SV bottom left
    northing_pref_value = prefix_values.get('north') # number of m the bottom left 100km grid square is north of SV bottom left
    
    #handle easting
    easting = str(easting_pref_value) + easting_value

    if len(easting) < 6:
        for _ in range(6-len(easting)):
            easting += '0'
            
    # handle northing
    northing = str(northing_pref_value) + northing_value
    if len(northing) < 6:
        for _ in range(6-len(northing)):
            northing += '0'
    
    return int(easting), int(northing)

def csv_converter(fp: str, col_name: str):
    """ Handles the writing of data to new csv file for the NGR to BNG coordinate conversion """
    if fp.endswith(".csv"):
        with open(fp) as csvfile:
            orig_data = csv.reader(csvfile)
            col_names = []
            for row in orig_data:
                col_names.extend(row)
                break
            if not col_names:
                return logger.error(f"No data in the csv")
            #match column name to find ngr
            matched_idx = 0 # default 0
            for i, col in enumerate(col_names):
                if col.lower() == col_name:
                    matched_idx = i
            if not matched_idx:
                logger.error(f"No columns matching the ngr or 2nd input variable found in the csv.")
                return 
            
            fp_name = f"{fp.split('.csv')[0]}_converted.csv"
            with open(fp_name, mode = 'w', newline = '') as newcsv:
                writer = csv.writer(newcsv)
                col_names.extend(['easting', 'northing'])
                writer.writerow(col_names)
                for i, row in enumerate(orig_data):
                    try:
                        easting, northing = convert_ngr_to_bng(row[matched_idx])
                        row.extend([easting, northing])
                    except (NGRCodeError, NGRCoordLengthError, TypeError) as e:
                        logger.error(f"Error at index {i} - skipping this row: {e}")
                    writer.writerow(row)
            logger.info(f"Eastings and Northings successfully added to {fp_name}")