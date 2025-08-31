# i have created this file - Raghvendra
from django.http import HttpResponse
from django.shortcuts import render


def index(s):
    dic1 = {'name':'Raghvendra' , 'place':'Earth'}
    return render(s,"index.html",dic1)    

def about(s):
    return render(s,'about.html')
    # return HttpResponse('''
    #                     <style>
    #                     a {
    #                         font-size: 14;
    #                         padding:5px;
    #                         color:black;
    #                         text-decoration:none;
    #                     }
    #                     a:hover{
    #                         font-size: 18;
    #                         color:blue;
    #                         background-color:lightgrey;
    #                         border-radius:5px;
    #                     }
    #                     </style>
    #                     <a href = "/">index</a>
    #                     <a href = "/view">view</a><br>
                        # About Raghvendra''')

def view(s):
    file = "textuils/filename.txt"
    text_data_index = s.POST.get('test','default')
    
    with open (file)as f:
        contents = f.read()
    with open (file,'a')as f:
        if text_data_index != "default":
            f.write(text_data_index)
        else:
            f.close()
        
    dic2 = {'con':contents,'data':text_data_index}
    return render(s,'view.html',dic2)
    
def analyzer(s):
    text_data = s.POST.get('text','default')

    remove_punc = s.POST.get('removepunc','off')
    cap = s.POST.get('capitalize','off')
    rem_line = s.POST.get('newLine','off')
    rem_space = s.POST.get('space','off')
    char_count = s.POST.get('charcount','off')
    
    analyzed = ""
    dic3 = {'purpose':'Default','analyzed_text':text_data} 
    if (remove_punc == "on"):
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|\}~'''
        for char in text_data:
            if char not in punctuations:
                analyzed += char
            
        dic3 = {'purpose':'Removed Punctuation','analyzed_text':analyzed} 
    
    if (cap == "on"):
        if analyzed !="":
            analyzed = analyzed.upper()
            dic3 = {'purpose':'CONVERTED IN CAPITAL','analyzed_text':analyzed} 
        elif analyzed == "":
            analyzed = text_data.upper()
            dic3 = {'purpose':'CONVERTED IN CAPITAL','analyzed_text':analyzed} 
            
    if (rem_line == "on"):
        anal = ""
        if analyzed !="":
            for char in analyzed:
                if char != "\n" and char != "\r":
                    anal += char
            analyzed = anal
                
        elif analyzed == "": 
            for char in text_data:
                if char != "\n" and char != "\r":
                    analyzed += char
        dic3 = {'purpose':'New Line are Removed','analyzed_text':analyzed}
    
    if (rem_space == "on"):
        ana = ''
        if analyzed !="":
            try:
                for index,char in enumerate(analyzed):
                    if analyzed[index] == " " and analyzed[index + 1] == " ":
                        pass
                    else:
                        ana += char
                dic3 = {'purpose':'Extra spaces are Removed','analyzed_text':ana}
            except IndexError:
                pass
            finally:
                analyzed = ana
                
        elif analyzed == "":
            try:
                for index,char in enumerate(text_data):
                    if text_data[index] == " " and text_data[index + 1] == " ":
                        pass
                    else:
                        analyzed += char
                dic3 = {'purpose':'Spaces are Removed','analyzed_text':analyzed}
            except IndexError:
                pass

    if (char_count == "on"):
        count = 0
        if analyzed !="":
            for char in analyzed:
                if char in analyzed and char != ' ' and char != '\n':
                    count +=1
            analyzed += "\n"
            analyzed += str(count)
            dic3 = {'purpose':'This much character is used','analyzed_text':analyzed} 
        elif analyzed =="":
            for char in text_data:
                if char in text_data and char != ' ' and char != '\n':
                    count +=1
            analyzed += "\n"
            analyzed += str(count)
            dic3 = {'purpose':'This much character is used','analyzed_text':analyzed} 
    
    return render(s,'analyze.html',dic3)
