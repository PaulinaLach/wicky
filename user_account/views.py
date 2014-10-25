from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.shortcuts import render
from user_account.models import UserAccount
from main.models import Photograph

@receiver(user_signed_up)
def set_gender(sender, **kwargs):
    user = kwargs.pop('user')
    # extra_data = user.socialaccount_set.filter(provider='facebook')[0].extra_data
    # gender = extra_data['gender']

    # if gender == 'male':  # because the default is female.
    #     user.gender = 'male'

    user.save()

def user_show(request, username):
    user = UserAccount.objects.filter(username=username)
    photographs = Photograph.objects.filter(user=user).order_by('-creation_date')[:5]
    print(photographs.first().url)
    return render(request, 'user_account/show.html', {user: user, photographs: photographs})

