from django.contrib import admin

# Register your models here.
from watchlist_app.models import WatchList,StreamPlatform
admin.site.register(StreamPlatform)
admin.site.register(WatchList)