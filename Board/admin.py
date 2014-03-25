from django.contrib import admin

from Board.models import BoardCategory
from Board.models import BoardEntry
from Board.models import BoardComment

# Register your models here.
admin.autodiscover()

admin.site.register(BoardCategory)
admin.site.register(BoardEntry)
admin.site.register(BoardComment)