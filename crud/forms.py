from django import forms
from django import forms

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, label='New Password')
    
class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'bg-white mb-2 px-3 py-2.5 border border-gray-380 text-black block text-sm rounded-sm w-full focus:outline-none focus:ring-blue-600 focus:border-blue-600',
            'placeholder': 'Enter new password'
        })
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'bg-white mb-2 px-3 py-2.5 border border-gray-380 text-black block text-sm rounded-sm w-full focus:outline-none focus:ring-blue-600 focus:border-blue-600',
            'placeholder': 'Confirm new password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data