from django.shortcuts import render
from django.views import View

# Create your views here.

class AlbumView(View):
    def get(self, request):
        range1 = range(5187,5199)
        return render(
            request,
            'album/london.html',
            {'range1': range1}
            )
