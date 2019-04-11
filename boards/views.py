from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

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

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user 
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user  
            )
            return redirect('board_topics', pk=board.pk) 
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})
