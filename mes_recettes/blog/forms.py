from socket import fromshare
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from . import models

class InscriptionForm(forms.Form):
    nom = forms.CharField(max_length=100,
                          label='Nom',
                          widget=forms.TextInput(attrs={'placeholder' : 'Votre nom',
                                                        'class' : 'inputChamp'}))
    pseudo = forms.CharField(max_length=100,
                             label='Pseudo',
                             widget=forms.TextInput(attrs={'placeholder' : 'Votre pseudo',
                                                        'class' : 'inputChamp'}))
    email = forms.CharField(max_length=100,
                            label='Adresse mail', validators=[validators.validate_email],
                            widget=forms.EmailInput(attrs={'placeholder' : 'Votre email',
                                                         'class' : 'inputChamp'}))
    mdp = forms.CharField(label='Mot de passe',
                          widget=forms.PasswordInput(attrs={'placeholder' : 'Votre mot de passe',
                                                            'class' : 'inputChamp'}))
    
    conf_mdp = forms.CharField(label='Confirmation de mot de passe',
                          widget=forms.PasswordInput(attrs={'placeholder' : 'Confirmation de mot de passe',
                                                            'class' : 'inputChamp'}))

    def clean_email(self):#clean_{name_field}
        data = self.cleaned_data['email']
        
        
        try:
            models.Member.objects.get(email=data)
        except:
            return data
        else:
            raise ValidationError("Your email is already used, hohoho !!!")
        
    def clean_pseudo(self):
        data = self.cleaned_data['pseudo']
        
        try:
            models.Member.objects.get(pseudo=data)
        except:
            return data
        else:
            raise ValidationError("Pseudo already used, hohoho !!!")
    
    def clean(self):
        cleaned_data = super().clean()
        
        if (len(cleaned_data)):
            clean_mdp = cleaned_data['mdp']
            clean_conf_mdp = cleaned_data['conf_mdp']
            
            if (clean_conf_mdp != clean_mdp):
                raise ValidationError("hahahaha, try again !!")
        
        return cleaned_data

class CommentaireForm(forms.Form):
    auteur = forms.CharField(max_length=100,
                          label='Nom',
                          widget=forms.TextInput(attrs={'placeholder' : 'Votre nom',
                                                        'class' : 'inputChamp'}))
    commentaire = forms.CharField(max_length=100,
                            label='Commentaire',
                            widget=forms.Textarea(attrs={'rows' : 4,
                                                         'placeholder' : 'Votre commentaire',
                                                         'class' : 'inputTextArea'}))
    note = forms.ChoiceField(label='Note',
                             choices=((x, x) for x in range(1, 6)))

class ConnexionForm(forms.Form):
    pseudo = forms.CharField(max_length=100,
                             label='Pseudo',
                             widget=forms.TextInput(attrs={'placeholder' : 'Votre pseudo',
                                                        'class' : 'inputChamp'}))
    mdp = forms.CharField(label='Mot de passe',
                          widget=forms.PasswordInput(attrs={'placeholder' : 'Votre mot de passe',
                                                            'class' : 'inputChamp'}))