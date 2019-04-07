from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from. models import Board,Topic,Post


from. forms import NewTopicForm

# Create your views here.

def home(request):
	''' Returns all the Board object in the homepage '''

	boards = Board.objects.all()
	return render(request,'index.html', context={'boards':boards})


def board_topics(request, pk):
	b_detail=get_object_or_404(Board, pk=pk)
	return render(request,'topics.html',context={'b_detail':b_detail})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit =False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk) 
    else:
        form = NewTopicForm()
    return render(request,'new_topic.html',context={'board':board,'form':form})