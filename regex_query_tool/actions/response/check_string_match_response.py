from typing import List

class StringMatchCheckResponse:
    string_query_matches: List

    def __init__(self, string_query_matches: List):
        self.string_query_matches = string_query_matches