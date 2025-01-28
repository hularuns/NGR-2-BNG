from ngr_to_bng.ngr_lookup import ngr_lookup

class NGRCodeError(Exception):
        def __init__(self, message):
            self.message = message
            if ngr_lookup:
                self.message += f" Valid prefixes: {', '.join(ngr_lookup.keys())}"
            super().__init__(self.message)
            
class NGRCoordLengthError(Exception):
    pass

def validate_ngr_input(ngr: str) -> bool:
    """ Validate and return ngr_input for further parsing.
    can range from 2 to 8 numbers in coord from SP12345678 which would be a 10 digit BNG coord - down to 1m resolution. """
    try:   
        return handle_validation(ngr)
    except (NGRCodeError, NGRCoordLengthError, TypeError) as e:
        raise e # later handle putting these error types into an error dict/file, or simply retunr an enums.ErrorType ?
        
def handle_validation(ngr: str):
    
    prefix = ngr[:2]
    coords = ngr[2:]
    
    if prefix not in ngr_lookup:
        raise NGRCodeError(f"{prefix} was not a valid prefix for the UK. Valid coordinates are:")
    coord_len = len(coords)
    if len(ngr) < 4 or not 2 < coord_len < 11 or not coord_len % 2 == 0 :
        raise NGRCoordLengthError(f"Length of coordinates not within 2 - 10 coords - coords is {len(coords)} in length.")
    if not coords.isdigit() or not isinstance(ngr, str):
        raise TypeError(f"Coordinate was not a valid format - Format is two letters followed by integers: {coords}")
    return True

