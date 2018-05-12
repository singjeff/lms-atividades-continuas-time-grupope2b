from core.models.sessaoAluno import SessaoAluno

class AutorizacaoMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith("/static/"):
            if 'PYSESSAO' in request.COOKIES:
                cookie = request.COOKIES['PYSESSAO']
                sessao = SessaoAluno.objects.get(id=cookie)
                request.sessao = sessao

        response = self.get_response(request)

        return response

        