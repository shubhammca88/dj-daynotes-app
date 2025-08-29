from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Note

def dashboard(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'daynotes/dashboard.html', context)

def note_detail(request, pk):
    note = get_object_or_404(Note, id=pk)
    context = {'note': note}
    return render(request, 'daynotes/note_detail.html', context)

def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Untitled')
        body = request.POST.get('body', '')
        Note.objects.create(title=title, body=body)
        messages.success(request, 'Note created successfully!')
        return redirect('dashboard')
    return render(request, 'daynotes/create_note.html')

def edit_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    if request.method == 'POST':
        note.title = request.POST.get('title', note.title)
        note.body = request.POST.get('body', note.body)
        note.save()
        messages.success(request, 'Note updated successfully!')
        return redirect('note_detail', pk=note.id)
    context = {'note': note}
    return render(request, 'daynotes/edit_note.html', context)

def delete_note(request, pk):
    note = get_object_or_404(Note, id=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('dashboard')
    context = {'note': note}
    return render(request, 'daynotes/delete_note.html', context)