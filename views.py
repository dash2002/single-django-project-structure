
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.html import escape
import asyncio

# 1
def topic1(request):
    return HttpResponse("Hello from the server! (Web & Client–Server)")

# 2
def topic2(request):
    return JsonResponse({"message": "Welcome to Django!"})

# 3
def topic3(request):
    return HttpResponse("Development environment setup complete!")

# 4
def topic4(request):
    return HttpResponse("Project and application configured.")

# 5
def topic5(request):
    return HttpResponse("Django project structure example shown.")

# 6
def topic6(request, name):
    return HttpResponse(f"Hello {name}!")

# 7
def topic7(request):
    return HttpResponse("Function-Based View example.")

# 8
def topic8(request):
    return HttpResponse("Django project flow: Request → URL → View → Template → Response")

# 9
def topic9(request):
    return HttpResponse("<h2>Templates and Static Files example</h2>")

# 10
def topic10(request):
    return HttpResponse("Database and models example (run migrations to test).")

# 11
def topic11(request):
    return HttpResponse("ORM basic operations executed.")

# 12
def topic12(request):
    return HttpResponse("Django Admin Interface available at /admin.")

# 13
def topic13(request):
    return HttpResponse("Form example rendered here.")

# 14 - cookies
def topic14_set_cookie(request):
    resp = HttpResponse("Cookie set!")
    resp.set_cookie("theme", "light")
    return resp

def topic14_get_cookie(request):
    return HttpResponse(f"Theme cookie: {request.COOKIES.get('theme', 'not set')}")

# 15
def topic15(request):
    return HttpResponse("User authentication required for this page.")

# 16
def topic16(request):
    return HttpResponse(f"Advanced template feature demo: {'django'.upper()}")

# 17
def topic17(request):
    return HttpResponse("Advanced ORM query example.")

# 18
def topic18(request):
    return HttpResponse("Middleware added attribute here.")

# 19
def topic19(request):
    return HttpResponse("Messages framework example output.")

# 20
def topic20(request):
    return HttpResponse("Signal executed after model save.")

# 21
def topic21(request):
    return HttpResponse("Performance optimization example.")

# 22
def topic22(request):
    return HttpResponse("Database index example.")

# 23
def topic23(request):
    return HttpResponse("Django Channels setup example.")

# 24
def topic24(request):
    return HttpResponse("Custom authentication / OAuth example.")

# 25
def topic25(request):
    return HttpResponse(f"Safe text: {escape('<script>alert(1)</script>')}")

# 26 (async)
async def topic26(request):
    await asyncio.sleep(1)
    return JsonResponse({"async": True})

# 27
def topic27(request):
    return HttpResponse("Custom admin interface example.")

# 28
def topic28(request):
    return HttpResponse("Custom Django admin command executed in terminal.")

# 29
def topic29(request):
    return HttpResponse("Internationalization and localization example.")