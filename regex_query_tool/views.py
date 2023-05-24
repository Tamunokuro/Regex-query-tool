import re
from regex_query_tool.actions import check_string_match
from regex_query_tool.actions.requests.check_string_match_requests import StringMatchCheck
from regex_query_tool.serializers.check_string_match_serializer import StringMatchCheckResponseSerializer
from django.shortcuts import render, redirect
from django.contrib import messages



def home(request):
    if request.method == "POST":
        match_string = request.POST.get("match_string")
        query_regex = request.POST.get("query_regex")
        full_match = bool(request.POST.get("full_match"))
        first_match = bool(request.POST.get("first_match"))
        
        try:
            string_match_check_request = StringMatchCheck(match_string, query_regex, full_match, first_match)
            string_match_check_result = check_string_match.execute(string_match_check_request)
            context = StringMatchCheckResponseSerializer(string_match_check_result).data
            return render(request, "regex_tool/home.html", context)
        except re.error as e:
            messages.add_message(request, messages.ERROR, str(e))
            return redirect("regex_query_tool:home")

    return render(request, "regex_tool/home.html")
