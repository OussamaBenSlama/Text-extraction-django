from django.shortcuts import render
from .treatment import Display
# Create your views here.

def get_text(request):
    if request.method == 'POST':
        input_text = request.POST.get('input-text', '')
        if input_text != "" :
            values = {}
            
            values["verbs"] = Display.display_verbs('', input_text)
                
            
            values["nouns"] = Display.display_noun('', input_text)
                
            
            values["adj"] = Display.display_adj('', input_text)
            values["e-mail"] = Display.get_mail('', input_text)
            
            values["phone-number"] = Display.get_number('', input_text)
            return render(request, 'output.html',{
                'input_text': input_text ,
                'values' : values ,
            })
        else :
            return render(request, 'index.html', {})
    else :
        return render(request, 'index.html', {})
