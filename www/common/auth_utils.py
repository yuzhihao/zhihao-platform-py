from apis import APIPermissionError


def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()