from django .htttp import HttpResponse
from django.shortcuts import redirect

#decoarator definition
def allowed_user(allowed_roles = []):
    def decoarators(view_func):
        def wrapper_func (request, *args, **kwargs):

        #checking if the group exist
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        #method to be executed if the user is allowed
        if group in allowed_roles:
            return view_func(request, *args, **kwargs)
        else:
            #message to be displayed if the user is not allowed
            return HttpResponse ('U dont Have Permission to perform thi function')

        return view_func(request, *args, **kwargs)
    return wrapper_func
return decoarator