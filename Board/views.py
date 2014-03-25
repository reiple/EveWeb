from django.shortcuts import render
from django.http import HttpResponse

from Board.models import BoardCategory
from Board.models import BoardEntry
from Board.models import BoardComment

# Create your views here.

def ViewBoardList(request):
    listCategory = BoardCategory.objects.all()
    
    strText = ""
    for strCategory in listCategory:
        strText = str(strText) + str(strCategory) + "<br />"
        
    return HttpResponse(strText)
    