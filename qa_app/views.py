from django.shortcuts import render
from .core.answer import QuestionAnswer

# Create your views here.
def index(request):
    template_name = "index.html"
    answer = ""
    if request.method == "POST":
        user_question = request.POST.get("question_input")
        print("***********")
        print("Question is: ", user_question)

        answer = QuestionAnswer.answer(user_question)
        print("***********")
        print("Answer is: ", answer)

    context = {
        "answer": answer,
    }
    return render(request, template_name, context) 