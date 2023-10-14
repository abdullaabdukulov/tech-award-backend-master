from django.http import JsonResponse
import openai

openai.api_key = "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"


def chatbot(request):
    message = request.GET.get("message", "")
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return JsonResponse({"response": response.choices[0].text})
