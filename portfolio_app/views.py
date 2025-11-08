from django.shortcuts import render

def home(request):
    projects = [
        { "name": "Restaurant Website", "url": "https://restaurant-website-coral.vercel.app/", "desc": "Live restaurant site" },
        { "name": "Portfolio App", "url": "https://portfolio-app-jet-seven.vercel.app/", "desc": "Your portfolio deployed on Vercel" },
        { "name": "Animation Example", "url": "https://great-animation.vercel.app/", "desc": "Animation project" },
        { "name": "Bird Game", "url": "https://bird-game-nu.vercel.app/", "desc": "Game deployed on Vercel" },
        { "name": "GitHub", "url": "https://github.com/Kegits", "desc": "My GitHub profile" },
    ]
    context = {
        "name": "Kelvin Gakuo",
        "title": "Data Analyst & Web Developer",
        "projects": projects,
        "links": {
            "github": "https://github.com/Kegits",
            "email": "https://mail.google.com/mail/?view=cm&fs=1&to=hansaxel192@gmail.com"
        }

    }
    return render(request, "portfolio_app/index.html", context)
