from django.http import JsonResponse


def chat(request):
    return JsonResponse({
        "reply": "Hello! I am your AI chatbot 🤖"
    })