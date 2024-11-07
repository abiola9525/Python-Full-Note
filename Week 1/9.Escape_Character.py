'''
    Escape Character
To insert characters that are not accepted in a string,we use an escape character.

An escape character is a backwardslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
'''

# By running this code we will be getting an error

# comment = "Hello the boy named "Kola" is a good programmer"
# print(comment)

# To fix a problem like this, we use the escape character \":

comment = "Hello the boy named \"Kola\" is a good programmer"
print(comment)


# Code	                    Result
# \'	                        Single Quote
# \\	                        Backslash
# \n	                        New Line
# \r	                        Carriage Return
# \t	                        Tab
# \b	                        Backspace
# \f	                        Form Feed
# \ooo	                        Octal value
# \xhh	                        Hex value







def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user =authenticate(request,
                username = cd['username'],
                password = cd['password'])

            if user is not None:
                login(request, user)
                return HttpResponse('Authentication Successful')
            else:
                return HttpResponse('Authentication Failed...')
        else:
            form = LoginForm
        return render(request, 'login.html', {'form' : form})



from django.shortcuts import render
from django.contrib.auth import authenticate, login
from . forms import LoginForm  ## changed '. form' to '. forms'
from django.http import HttpResponse

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data #cd means clean data
            user = authenticate(request, 
                                username = cd['username'],   ## changed "cd('username')" to "cd['username']"
                                password = cd['password'])   ## changed "cd('password')" to "cd['password']"
            
            if user is not None:
                login(request, user)
                return HttpResponse('Authentication Successful')
            
            else:
                return HttpResponse('Authentication failed, please try again')
    
    else:
        form = LoginForm()    ## added () after the LoginForm
    
    return render(request, 'login.html', {'form':form})