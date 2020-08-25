from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect #import the Response for Http
from django.http import HttpRequest #import the Request for Http
from .models import register #import the class from the models in the app
from django.utils import timezone

# Create your views here.
# def topviews(responst):
    
#     return HttpResponse("This the Home Page")

#********** Global Variable ********************
errocode = 0 #for control according to cituation

#********** Function *********************
def topviews(request):
    # all_reg_items = register.objects.all() #the record all the content in the class register
    global errocode #global variable to control the which template to display   

    # #if there is no error, then display normally    
    if errocode == 0:
        return render(request,'account/login.html')
    #if error code is one display the error message, then reset the error code     
    elif errocode == 1:
        errocode = 0 
        return render(request,'account/login_with_error.html')
    else:
        errocode = 0
        return render(request,'account/login.html')
    # return render(request,'Account/login.html')

        

def addmessage(request):
    #create a new register all_items
    #save
    #redirect the browser to the '/greeting/'

    #** This is the one expression to save all the attribution method*****************
    # new_reg = register(first_name = request.POST['first_name'])
    #
    # new_reg = register(first_name = request.POST['first_name'], last_name = request.POST['last_name'],
    #     wish_rrp = request.POST['rrp'], user_msg = request.POST['umsg'], 
    #     user_email = request.POST['uemail'], post_date = timezone.now() )
    # #     #save all attribute to database.
    #
    # new_reg.save()
    #*************************************** End ***************************
    global errocode


    #The equivelent express for save all attribute to database. This method could fitting a checking statement.
    new_fn  = request.POST['first_name']
    new_ln  = request.POST['last_name']
    new_rrp = request.POST['rrp']
    new_msg = request.POST['umsg']
    new_eml = request.POST['uemail']

    #** set the check method, if the user had enter all the information **
    if(not(new_fn and new_ln and new_eml)): #check if speciific field is empty.

        errocode = 1 #
        return HttpResponseRedirect('/login_with_error/')
    else:
        #if all require field is filled, then save to database.
        new_reg = register(first_name = new_fn, last_name = new_ln, 
                        wish_rrp = new_rrp, user_email = new_eml,
                        user_msg = new_msg )
        
        new_reg.save()
        
        errocode = 0

        return HttpResponseRedirect('/greeting/')


def greeting(request):
    return render(request,'Account/greeting.html') #display a thank you messsage after all the information is saved

def testing(request):
    return render(request,'Home/bootstrap.html') #display a testing html, deleting before deploy