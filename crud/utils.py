from django.shortcuts import redirect

def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('/layout/login') 
        return view_func(request, *args, **kwargs)
    return wrapper