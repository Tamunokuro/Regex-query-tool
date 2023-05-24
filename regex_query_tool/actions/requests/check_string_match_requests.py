
class StringMatchCheck:
    match_string: str
    query_regex: str
    full_match: bool
    first_match: bool

    def __init__(self, match_string: str, query_regex: str, full_match: bool, first_match: bool):
        self.match_string = match_string
        self.query_regex = query_regex
        self.full_match = full_match
        self.first_match = first_match

    
        
        