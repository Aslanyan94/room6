from django import forms


class RegisterForm(forms.ModelForm):
    username = forms.CharField(min_length=7, max_length=15)
    password_1 = forms.PasswordInput()
    password_2 = forms.PasswordInput()

    def save(self, *args, **kwargs):
        if self.password_1 == self.password_2:
            super().__init__(self).save(*args, **kwargs)
        else:
            raise ValueError