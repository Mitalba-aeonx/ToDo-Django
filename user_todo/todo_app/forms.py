from django.forms import ModelForm
from todo_app.models import TODO

class TodoForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title','priority','is_completed','description']