from regex_query_tool.actions.response.check_string_match_response import StringMatchCheckResponse

class StringMatchCheckResponseSerializer:
    
    def __init__(self, detail_response: StringMatchCheckResponse):
        self._detail_response = detail_response


    @property
    def data(self) -> dict:
        response_string_matches = self._detail_response.string_query_matches
        return {
            "data" : {
                "string_query_matches" : response_string_matches
            }
        }
