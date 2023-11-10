from django.shortcuts import render
from .models import Video


def videos(request):
    videos_list = Video.objects.all()
    context = {"videos_list": videos_list}
    return render(request, 'videos.html', context)

def video(request, id):
    # 7
    # SELECT * FROM video_video WHERE id = 7;
    video_object = Video.objects.get(id=id)
    return render(request, 'video.html', {"video": video_object})