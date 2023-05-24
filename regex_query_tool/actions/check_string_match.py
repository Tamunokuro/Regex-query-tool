import re
from regex_query_tool.actions.requests.check_string_match_requests import StringMatchCheck
from regex_query_tool.actions.response.check_string_match_response import StringMatchCheckResponse

def execute(request: StringMatchCheck):
    string_matches = get_string_matches(request)
    return StringMatchCheckResponse(string_matches)


def get_string_matches(request: StringMatchCheck) -> list:
    matches = []

    if request.full_match:
        pattern = re.compile(request.query_regex)
        if re.search(pattern, request.match_string):
            matches.append(request.match_string)
    elif request.first_match:
        pattern = re.compile(request.query_regex)
        match = re.match(pattern, request.match_string)
        if match:
            matches.append(match.group(0))
    else:
        pattern = re.compile(request.query_regex)
        matches = re.findall(pattern, request.match_string)
    
    return matches
