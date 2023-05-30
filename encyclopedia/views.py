from django.shortcuts import render

from . import util

from markdown2 import Markdown
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    content, title = "", "Error 404"

    if entry:
        content = markdowner.convert(entry)
        title = content.split("<h1>")[1].split("</h1>")[0]
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry,
        "content": content
    })
