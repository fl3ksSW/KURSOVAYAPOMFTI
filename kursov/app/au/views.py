from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@require_GET
def index(request: HttpRequest) -> HttpResponse:
    """
    Render the index page.
    """
    return render(request, 'au/index.html')

@csrf_exempt
@login_required
def custom_view_with_csrf(request: HttpRequest) -> HttpResponse:
    """
    Custom view that requires CSRF protection and authentication.
    """
    if request.method == 'POST':
        from django.middleware.csrf import get_token
        csrf_token = get_token(request)
        return HttpResponse(f"CSRF token: {csrf_token}")
    else:
        return HttpResponse("This view only accepts POST requests with CSRF protection.", status=405)
    
@csrf_exempt
@login_required
def custom_view_with_authentication(request: HttpRequest) -> HttpResponse:
    """
    Custom view that requires authentication.
    """
    return HttpResponse("This is a protected view. You are authenticated.")

@csrf_exempt
def custom_view_with_params(request: HttpRequest, param1: str, param2: int) -> HttpResponse:
    """
    Custom view that accepts parameters.
    """
    return HttpResponse(f"Custom view with parameters: {param1}, {param2}")

@csrf_exempt
def custom_view_with_query(request: HttpRequest) -> HttpResponse:
    """
    Custom view that accepts query parameters.
    """
    query_param = request.GET.get('query', 'default')
    return HttpResponse(f"Custom view with query parameter: {query_param}")

@csrf_exempt
def custom_view_with_post(request: HttpRequest) -> HttpResponse:
    """
    Custom view that accepts POST requests.
    """
    if request.method == 'POST':
        data = request.POST.get('data', 'No data provided')
        return HttpResponse(f"Custom view with POST data: {data}")
    else:
        return HttpResponse("This view only accepts POST requests.", status=405)
    
@csrf_exempt
def custom_view_with_json(request: HttpRequest) -> HttpResponse:
    """
    Custom view that accepts JSON data in POST requests.
    """
    import json
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return HttpResponse(f"Custom view with JSON data: {data}")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data.", status=400)
    else:
        return HttpResponse("This view only accepts POST requests with JSON data.", status=405)
    
@csrf_exempt
def custom_view_with_file_upload(request: HttpRequest) -> HttpResponse:
    """
    Custom view that accepts file uploads in POST requests.
    """
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        return HttpResponse(f"File '{file.name}' uploaded successfully.")
    else:
        return HttpResponse("This view only accepts POST requests with file uploads.", status=405)
    
@csrf_exempt
def custom_view_with_session(request: HttpRequest) -> HttpResponse:
    """
    Custom view that interacts with session data.
    """
    if request.method == 'POST':
        request.session['key'] = request.POST.get('value', 'default')
        return HttpResponse(f"Session value set: {request.session['key']}")
    else:
        return HttpResponse(f"Current session value: {request.session.get('key', 'not set')}")
    
@csrf_exempt
def custom_view_with_pagination(request: HttpRequest) -> HttpResponse:
    """
    Custom view that demonstrates pagination.
    """
    from django.core.paginator import Paginator
    items = list(range(1, 101))

    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return HttpResponse(f"Page {page_number}: {list(page_obj.object_list)}")

@csrf_exempt
def custom_view_with_custom_response(request: HttpRequest) -> HttpResponse:
    """
    Custom view that returns a custom response.
    """
    response = HttpResponse("This is a custom response.")
    response['Custom-Header'] = 'CustomValue'
    return response

@csrf_exempt
def custom_view_with_caching(request: HttpRequest) -> HttpResponse:
    """
    Custom view that demonstrates caching.
    """
    from django.views.decorators.cache import cache_page
    @cache_page(60 * 15)  # Cache for 15 minutes
    def cached_view(request: HttpRequest) -> HttpResponse:
        return HttpResponse("This response is cached for 15 minutes.")
    
    return cached_view(request)

@csrf_exempt
def custom_view_with_static_files(request: HttpRequest) -> HttpResponse:
    """
    Custom view that serves static files.
    """
    from django.conf import settings
    from django.templatetags.static import static
    static_file_url = static('css/style.css')

    return HttpResponse(f"Static file URL: {static_file_url}")

@csrf_exempt
def custom_view_with_media_files(request: HttpRequest) -> HttpResponse:
    """
    Custom view that serves media files.
    """
    from django.conf import settings
    from django.templatetags.static import static
    media_file_url = static('media/example.jpg')

    return HttpResponse(f"Media file URL: {media_file_url}")

@csrf_exempt
def custom_view_with_template(request: HttpRequest) -> HttpResponse:
    """
    Custom view that renders a template.
    """
    context = {'message': 'Hello, this is a custom view with a template!'}
    return render(request, 'au/custom_template.html', context)

@csrf_exempt
def custom_view_with_template_and_context(request: HttpRequest) -> HttpResponse:
    """
    Custom view that renders a template with additional context.
    """
    context = {
        'title': 'Custom Template View',
        'message': 'This is a custom template view with additional context.',
    }
    return render(request, 'au/custom_template_with_context.html', context)

@csrf_exempt
def custom_view_with_template_and_static(request: HttpRequest) -> HttpResponse:
    """
    Custom view that renders a template with static files.
    """
    from django.templatetags.static import static
    context = {
        'title': 'Custom Template with Static Files',
        'static_file': static('css/style.css'),
    }
    return render(request, 'au/custom_template_with_static.html', context)

@csrf_exempt
def custom_view_with_template_and_media(request: HttpRequest) -> HttpResponse:
    """
    Custom view that renders a template with media files.
    """
    from django.templatetags.static import static
    context = {
        'title': 'Custom Template with Media Files',
        'media_file': static('media/example.jpg'),
    }
    return render(request, 'au/custom_template_with_media.html', context)

@csrf_exempt
def custom_view_with_template_and_csrf(request: HttpRequest) -> HttpResponse:
    """
    Custom view that renders a template with CSRF protection.
    """
    from django.middleware.csrf import get_token
    csrf_token = get_token(request)
    context = {
        'title': 'Custom Template with CSRF',
        'csrf_token': csrf_token,
    }
    return render(request, 'au/custom_template_with_csrf.html', context)

@csrf_exempt
def login_view(request: HttpRequest) -> HttpResponse:
    """
    Custom login view.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Here you would typically authenticate the user
        return HttpResponse(f"Logged in as {username}")
    else:
        return render(request, 'au/login.html')
    
@csrf_exempt
def logout_view(request: HttpRequest) -> HttpResponse:
    """
    Custom logout view.
    """
    # Here you would typically log out the user
    return HttpResponse("Logged out successfully.")

@csrf_exempt
def register(request: HttpRequest) -> HttpResponse:
    """
    Custom registration view.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Here you would typically create a new user
        return HttpResponse(f"Registered user: {username}")
    else:
        return render(request, 'au/register.html')
    
@csrf_exempt
def profile(request: HttpRequest) -> HttpResponse:
    """
    Custom profile view.
    """
    # Here you would typically retrieve the user's profile information
    return render(request, 'au/profile.html', {'username': 'example_user'})

@csrf_exempt
def edit_profile(request: HttpRequest) -> HttpResponse:
    """
    Custom view to edit user profile.
    """
    if request.method == 'POST':
        # Here you would typically update the user's profile information
        return HttpResponse("Profile updated successfully.")
    else:
        return render(request, 'au/edit_profile.html', {'username': 'example_user'})
    
@csrf_exempt
def password_change(request: HttpRequest) -> HttpResponse:
    """
    Custom view to change user password.
    """
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        # Here you would typically change the user's password
        return HttpResponse("Password changed successfully.")
    else:
        return render(request, 'au/password_change.html')
