from django import forms 

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        max_length=100,
        required=True,
                widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Jõao Silva',
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Digite sua senha',
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadatro',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: João Silva',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: joaosilva@email.com',
            }    
        )
    )

    senha_1= forms.CharField(
        label='Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Digite sua senha',
            }
        )
    )

    senha_2= forms.CharField(
        label='Senha',
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Digite sua senha Novamente',
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError('O nome não pode conter espaços')
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')    

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas não conferem')
            else:
                return senha_2    