from django.shortcuts import redirect


class ScreenMiddleware(object):

    def process_request(self, request):

        if not request.session.get('screen', None):
            request.session['screen'] = 'normal'

        if request.GET.get('screen', None):
            request.session['screen'] = request.GET.get('screen')
            return redirect(request.META.get('HTTP_REFERER'))

