from .list import List

def list(request):
    return {'list': List(request)}