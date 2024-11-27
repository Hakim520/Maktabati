from .views import getCartCount

def counter_calculator(request):
    if 'admin' in request.path:
        return {}
    elif request.user.is_authenticated:
        d = dict(cart_count=getCartCount(request),username=request.user.username.split("@")[0])

        if request.COOKIES.get("cart_succes"):
            d.update({"CartSuccess":True})
        return d
    else:
        return {}