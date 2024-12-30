import requests
from django.http import JsonResponse

def get_weather(request):
    city = request.GET.get('city', 'Casablanca')  # Default city is Casablanca
    api_key = "450f4ca1f0b460b0507e0c1197cdc090"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({'error': 'Unable to fetch weather data'}, status=500)

