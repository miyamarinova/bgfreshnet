from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden


def admin_group_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='BigBossAdmins').exists() or request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            # Redirect or return an error pagex
            return HttpResponseForbidden("You don't have permission to access this page.")
    return _wrapped_view

def has_delete_permission(user):
    return user.has_perm('freshnet_products.delete_product')