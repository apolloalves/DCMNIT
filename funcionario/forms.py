from django import forms  
from funcionario.models import Funcionario  
class FuncionarioForm(forms.ModelForm):  
    class Meta:  
        model = Funcionario  
        fields = "__all__"  