from django.shortcuts import render
import re
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == "POST":
        string = request.POST.get("string")
        query_regex = request.POST.get("query_regex")
        full_match = bool(request.POST.get("full_match"))
        first_match = bool(request.POST.get("first_match"))

        matches = []
        if full_match:
            pattern = re.compile(r"^{}$".format(query_regex))
            if re.match(pattern, string):
                matches.append(string)
        elif first_match:
            pattern = re.compile(query_regex)
            match = re.search(pattern, string)
            if match:
                matches.append(match.group(0))
        else:
            pattern = re.compile(query_regex)
            matches = re.findall(pattern, string)

        return render(request, "regex_tool/home.html", {"matches": matches})

    return render(request, "regex_tool/home.html")
