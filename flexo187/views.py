from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .forms import PictureForm
from .models import Picture

def get_pictures_list(request):
	pictures = Picture.objects.order_by("-UPLOADED_DATE")
	return render(request, 'flexo187/post_list.html', {'pictures': pictures})
	
def get_picture_comment(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    return render(request, 'flexo187/post_detail.html', {'picture': picture})
	
def upload_picture(request):
    if request.method == "POST":
        form = PictureForm(request.POST,request.FILES)
        if form.is_valid():
            picture=Picture(IMAGE=request.FILES.get('IMAGE'))
            picture=form.save(commit=False)
            picture.UPLOADED_DATE=timezone.now()
            form.save()
            picture.save()
            return redirect('post_list')
    else:
        form = PictureForm()
    return render(request, 'flexo187/post_edit.html', {'form': form})
	
def edit_comment(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    if request.method == "POST":
        form = PictureForm(request.POST,request.FILES)
        if form.is_valid():
            picture=Picture(IMAGE=request.FILES.get('IMAGE'))
            picture=form.save(commit=False)
            picture.UPLOADED_DATE=timezone.now()
            form.save()
            picture.save()
            return redirect('post_list')
    else:
        form = PictureForm(instance=picture)
    return render(request, 'flexo187/post_edit.html', {'form': form})