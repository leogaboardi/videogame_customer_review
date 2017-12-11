from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    games = Game.objects.all()
    template = loader.get_template('games/index.html')
    context = {'games': games}
    return HttpResponse(template.render(context,request))

def game(request,game_id):
	review_count = Review.objects.filter(game=game_id).count()
	if review_count > 0:
		approval_rate = str(int(Review.objects.filter(game=game_id).filter(vote=1).count() / review_count * 100))+'%'
	else:
		approval_rate = None
	context = {'game': Game.objects.get(id=game_id),
				'reviews': Review.objects.filter(game=game_id),
				'review_count': review_count,
				'approval_rate': approval_rate,
				}

	return render(request, 'games/detail_page.html',context)

def review(request,review_id):
	context = {'review': Review.objects.get(id=review_id)}
	return render(request, 'games/review.html',context)

#    return HttpResponse("Review.")
