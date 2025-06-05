from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


async def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')

async def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is the about page.")

async def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is the contact page.")

async def services(request: HttpRequest) -> HttpResponse:
    return HttpResponse("These are our services.")

async def blog(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to our blog.")

async def blog_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    return HttpResponse(f"This is the detail page for blog post {post_id}.")

async def portfolio(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to our portfolio.")

async def portfolio_detail(request: HttpRequest, project_id: int) -> HttpResponse:
    return HttpResponse(f"This is the detail page for portfolio project {project_id}.")

async def faq(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Frequently Asked Questions.")

async def terms(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Terms and Conditions.")

async def privacy(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Privacy Policy.")

async def sitemap(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Sitemap of the website.")

async def error_404(request: HttpRequest, exception=None) -> HttpResponse:
    return HttpResponse("404 Not Found", status=404)

async def error_500(request: HttpRequest) -> HttpResponse:
    return HttpResponse("500 Internal Server Error", status=500)

async def error_403(request: HttpRequest, exception=None) -> HttpResponse:
    return HttpResponse("403 Forbidden", status=403)

async def error_400(request: HttpRequest, exception=None) -> HttpResponse:
    return HttpResponse("400 Bad Request", status=400)

async def maintenance(request: HttpRequest) -> HttpResponse:
    return HttpResponse("The site is currently under maintenance. Please check back later.", status=503)

async def custom_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("This is a custom view for demonstration purposes.")

async def custom_view_with_params(request: HttpRequest, param1: str, param2: int) -> HttpResponse:
    return HttpResponse(f"Custom view with parameters: {param1}, {param2}")

async def custom_view_with_query(request: HttpRequest) -> HttpResponse:
    query_param = request.GET.get('query', 'default')
    return HttpResponse(f"Custom view with query parameter: {query_param}")

async def custom_view_with_post(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = request.POST.get('data', 'No data provided')
        return HttpResponse(f"Custom view with POST data: {data}")
    else:
        return HttpResponse("This view only accepts POST requests.", status=405)
    
async def custom_view_with_json(request: HttpRequest) -> HttpResponse:
    import json
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return HttpResponse(f"Custom view with JSON data: {data}")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data.", status=400)
    else:
        return HttpResponse("This view only accepts POST requests with JSON data.", status=405)
    
async def custom_view_with_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST' and request.FILES:
        file = request.FILES['file']
        return HttpResponse(f"File '{file.name}' uploaded successfully.")
    else:
        return HttpResponse("This view only accepts POST requests with file uploads.", status=405)
    
async def custom_view_with_session(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        request.session['key'] = request.POST.get('value', 'default')
        return HttpResponse(f"Session value set: {request.session['key']}")
    else:
        return HttpResponse(f"Current session value: {request.session.get('key', 'not set')}")
    
async def custom_view_with_csrf(request: HttpRequest) -> HttpResponse:
    from django.middleware.csrf import get_token
    if request.method == 'POST':
        csrf_token = get_token(request)
        return HttpResponse(f"CSRF token: {csrf_token}")
    else:
        return HttpResponse("This view only accepts POST requests with CSRF protection.", status=405)
    
async def custom_view_with_authentication(request: HttpRequest) -> HttpResponse:
    from django.contrib.auth.decorators import login_required
    from django.utils.decorators import method_decorator

    @login_required
    async def authenticated_view(request: HttpRequest) -> HttpResponse:
        return HttpResponse("This is a protected view. You are authenticated.")

    return await authenticated_view(request)

async def custom_view_with_pagination(request: HttpRequest) -> HttpResponse:

    from django.core.paginator import Paginator
    items = list(range(1, 101))  # Example data
    paginator = Paginator(items, 10)  # Show 10 items per page

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    response_content = f"Page {page_obj.number} of {paginator.num_pages}: " + ", ".join(map(str, page_obj.object_list))
    return HttpResponse(response_content)

async def custom_view_with_caching(request: HttpRequest) -> HttpResponse:
    from django.views.decorators.cache import cache_page

    @cache_page(60 * 15)  # Cache this view for 15 minutes
    async def cached_view(request: HttpRequest) -> HttpResponse:
        return HttpResponse("This view is cached for 15 minutes.")

    return await cached_view(request)

async def custom_view_with_static_files(request: HttpRequest) -> HttpResponse:
    from django.conf import settings
    from django.templatetags.static import static

    static_file_url = static('css/style.css')  # Example static file
    return HttpResponse(f"Static file URL: {static_file_url}")

async def custom_view_with_media_files(request: HttpRequest) -> HttpResponse:
    from django.conf import settings
    from django.templatetags.static import static

    media_file_url = static('media/example.jpg')  # Example media file
    return HttpResponse(f"Media file URL: {media_file_url}")

async def custom_view_with_template(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/custom_template.html', {'message': 'This is a custom template view.'})

async def custom_view_with_template_and_context(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'Custom Template View',
        'message': 'This view uses a custom template with context data.',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'main/custom_template_with_context.html', context)
