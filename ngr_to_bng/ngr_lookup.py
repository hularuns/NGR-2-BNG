from pprint import pprint
""" Distance in 100km or the most southwestern point of each grid square from the 0,0 of bottom-left of SV """
ngr_lookup = {
    'HP': {'east': 0, 'north': 10},
    'HQ': {'east': 1, 'north': 10},
    'HT': {'east': 2, 'north': 10},
    'HU': {'east': 3, 'north': 10},
    'HW': {'east': 4, 'north': 10},
    'NA': {'east': 0, 'north': 9},
    'NB': {'east': 1, 'north': 9},
    'NC': {'east': 2, 'north': 9},
    'ND': {'east': 3, 'north': 9},
    'NE': {'east': 4, 'north': 9},
    'NF': {'east': 0, 'north': 8},
    'NG': {'east': 1, 'north': 8},
    'NH': {'east': 2, 'north': 8},
    'NJ': {'east': 3, 'north': 8},
    'NK': {'east': 4, 'north': 8},
    'NL': {'east': 0, 'north': 7},
    'NM': {'east': 1, 'north': 7},
    'NN': {'east': 2, 'north': 7},
    'NO': {'east': 3, 'north': 7},
    'NP': {'east': 4, 'north': 7},
    'NQ': {'east': 0, 'north': 6},
    'NR': {'east': 1, 'north': 6},
    'NS': {'east': 2, 'north': 6},
    'NT': {'east': 3, 'north': 6},
    'NU': {'east': 4, 'north': 6},
    'NV': {'east': 0, 'north': 5},
    'NW': {'east': 1, 'north': 5},
    'NX': {'east': 2, 'north': 5},
    'NY': {'east': 3, 'north': 5},
    'NZ': {'east': 4, 'north': 5},
    'OA': {'east': 5, 'north': 9},
    'OF': {'east': 5, 'north': 8},
    'OL': {'east': 5, 'north': 7},
    'OQ': {'east': 5, 'north': 6},
    'OV': {'east': 5, 'north': 5},
    'SA': {'east': 0, 'north': 4},
    'SB': {'east': 1, 'north': 4},
    'SC': {'east': 2, 'north': 4},
    'SD': {'east': 3, 'north': 4},
    'SE': {'east': 4, 'north': 4},
    'SF': {'east': 0, 'north': 3},
    'SG': {'east': 1, 'north': 3},
    'SH': {'east': 2, 'north': 3},
    'SJ': {'east': 3, 'north': 3},
    'SK': {'east': 4, 'north': 3},
    'SL': {'east': 0, 'north': 2},
    'SM': {'east': 1, 'north': 2},
    'SN': {'east': 2, 'north': 2},
    'SO': {'east': 3, 'north': 2},
    'SP': {'east': 4, 'north': 2},
    'SQ': {'east': 0, 'north': 1},
    'SR': {'east': 1, 'north': 1},
    'SS': {'east': 2, 'north': 1},
    'ST': {'east': 3, 'north': 1},
    'SU': {'east': 4, 'north': 1},
    'SV': {'east': 0, 'north': 0},
    'SW': {'east': 1, 'north': 0},
    'SX': {'east': 2, 'north': 0},
    'SY': {'east': 3, 'north': 0},
    'SZ': {'east': 4, 'north': 0},
    'TA': {'east': 5, 'north': 4},
    'TF': {'east': 5, 'north': 3},
    'TL': {'east': 5, 'north': 2},
    'TQ': {'east': 5, 'north': 1},
    'TV': {'east': 5, 'north': 0}
}

if __name__ == "__main__":
    for ngr, coords in ngr_lookup.items():
        #get the 100km prefix
        east = coords.get('east')/100
        north = coords.get('north')/100
        ngr_lookup[ngr].update({
            "east": int(east), "north": int(north)
        })
    pprint(ngr_lookup)    
