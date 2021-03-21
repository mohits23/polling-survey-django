from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import QuizModel

# Create your views here.

def quiz_home(request): 
    if request.user.is_authenticated:   
        # context = { 'chk_user': request.user.is_authenticated }
        return render(request, 'quiz/quiz_home.html')
    else:
        return redirect('login')


def set_quiz_title(request):

    # if 'quiz_title' in request.session:
    #     del request.session['quiz_title']

    if request.user.is_authenticated:   
        if request.method == 'POST':
            print('\nQuiz Title :', request.POST.get('quiz_title'), end='\n\n') 
            request.session['quiz_title'] = str(request.POST.get('quiz_title'))
            request.session['page_count'] = 1
            return redirect('create_quiz')         
        return render(request, 'quiz/set_quiz_title.html')
    else:
        return redirect('login')



def create_quiz(request):    

    # print('\nQuiz Title :', request.session['quiz_title'], end='\n\n')      
    
    if request.user.is_authenticated:   
            
        qtitle = ''
        total_questions = ''
        if request.method == 'POST' or request.method == 'FILES':                        
                                    
            print('\nQuestion :', request.POST.get('question'), end='\n\n')

            # title = request.POST.get('quiz_title')
            # question = request.POST.get('question')
            # image = request.FILES['image']            

            # upload_to_model = QuizModel(user_id=request.user.id, quiz_title=title, question=question, image=image)
            # upload_to_model.save()

            # image = request.FILES['image']

            # correct_option = 'correct_option_' + str(request.session['page_count'])
            # print('\nCorrect Option :', correct_option, end='\n\n')      

            quiz = QuizModel()

            quiz.quiz_title = request.POST.get('quiz_title')
            quiz.poller = request.POST.get('quiz_title')
            quiz.question = request.POST.get('question')            
            quiz.image = request.FILES.get('image')  ## To make ("ImageField / FileField") 'Optional' then add [ blank=True, null=True ] in "models.py" and use ["request.FILES.get('image_field_name')"] while manually catching and saving the value of "image_field_name" from HTML Form in "views.py".
            quiz.user = request.user      


            if request.session['page_count'] == 1:
                quiz.correct_option_1 = request.POST.get('correct_answer')
            elif request.session['page_count'] == 2:
                quiz.correct_option_2 = request.POST.get('correct_answer')
            elif request.session['page_count'] == 3:
                quiz.correct_option_3 = request.POST.get('correct_answer')
            elif request.session['page_count'] == 4:
                quiz.correct_option_4 = request.POST.get('correct_answer')
            elif request.session['page_count'] == 5:
                quiz.correct_option_5 = request.POST.get('correct_answer')
            elif request.session['page_count'] == 6:
                quiz.correct_option_6 = request.POST.get('correct_answer')
            


            if request.POST.get('option_one'):
                quiz.option_one = request.POST.get('option_one')      
            if request.POST.get('option_two'):
                quiz.option_two = request.POST.get('option_two')      
            if request.POST.get('option_three'):
                quiz.option_three = request.POST.get('option_three')      
            if request.POST.get('option_four'):
                quiz.option_four = request.POST.get('option_four')      
            if request.POST.get('option_five'):
                quiz.option_five = request.POST.get('option_five')      
            if request.POST.get('option_six'):
                quiz.option_six = request.POST.get('option_six')      
            
            quiz.save()  ## Committing Inserted Data

            if request.POST.get('session_state') == '1': 
                request.session['page_count'] = request.session['page_count'] + 1
                return redirect('create_quiz')
            else:
                qtitle = request.session['quiz_title']                            
                total_questions = request.session['page_count']

                if 'quiz_title' in request.session:
                    del request.session['quiz_title']                            

                if 'page_count' in request.session:
                    del request.session['page_count']
                messages.success(request, 'Q&A Form Created Succesfully!!')
            
        context = { 'qtitle': qtitle, 'total_questions': total_questions }
        return render(request, 'quiz/create_quiz.html', context)

    else:
        return redirect('login')





def get_titles(request):
    if request.user.is_authenticated: 

        print('\n\nCurrent Username :', request.user, end='\n\n')

        request_id = str(request.user.id)          
        titles_quiz = QuizModel.objects.filter(user_id__exact=request_id).values('quiz_title').distinct()  ## This will fetch all distinct values of "quiz_title" [ values('quiz_title).distinct() ]  where the "user_id" is the equal to the "Current User ID"(request.user.id).
        print('\n\nGet Titles Object :', titles_quiz, end='\n\n')

        context = { 'titles_quiz': titles_quiz }
        return render(request, 'quiz/show_titles.html', context)

    else:
        return redirect('login')

        



def show_quiz(request, quiz_title):
    if request.user.is_authenticated: 

        show_quiz = QuizModel.objects.filter(quiz_title__exact=quiz_title)        
        print('\n\nShow Quiz Object :', show_quiz, end='\n\n')        
        
        collect_id = []    ## This will store all the required id(s) as all options are passed as their (id) names in the Template.        
        
        for s in show_quiz:
            print('\n\nFor Loop Object :', s)
            s = str(s)            
            # print('Loop Object (str) :', s, end='\n\n')            
            # print('Loop Object (str type) :', type(s), end='\n\n')
            temp = ''
            for ch in s:   
                if ch.isdigit():
                    temp = temp + ch
            collect_id.append(temp)

        print('\n\nCollect ID(s) :', collect_id, end='\n\n')
        
        count_questions = []
        for i in range(1, len(collect_id)):
            count_questions.append(i)

        if request.method == 'POST':            

            for c_id in collect_id:               
                response = request.POST.get(c_id)
                quiz = QuizModel.objects.get(pk=c_id)
                
                email = User.objects.filter(id__exact=request.user.id).values('email')  ## Retrieving current user e-mail id from "User" Model
                print('\nCurrent User Email :', email[0]['email'], end='\n')               
                quiz.poller = email[0]['email']  ## Storing current user e-mail id to Model

               
                if 'option' in response:                
                    print('\n\nMCQ Response', c_id, ':', response, end='\n\n')

                    if response == 'option1':                        
                        quiz.option_one_count += 1
                    if response == 'option2':
                        quiz.option_two_count += 1
                    if response == 'option3':
                        quiz.option_three_count += 1
                    if response == 'option4':
                        quiz.option_four_count += 1                                                
                    if response == 'option5':
                        quiz.option_five_count += 1
                    if response == 'option6':
                        quiz.option_six_count += 1
                else:
                    print('\n\nText Response', c_id, ':', response, end='\n\n')
                    quiz.text_response = str(response)

                quiz.save()

        first_count = collect_id[0]
        context = { 'show_quiz': show_quiz, 'title': quiz_title, 'f_count': first_count }
        return render(request, 'quiz/show_quiz.html', context)

    else:
        return redirect('login')





def delete_quiz(request, quiz_title):
    if request.user.is_authenticated:

        quiz = QuizModel.objects.filter(quiz_title__exact = quiz_title)
        quiz.delete()

        return redirect('/quiz/get_titles/')

    else:
        return redirect('login')    