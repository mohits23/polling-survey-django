from django import template


#  Registering New Django Template Tags And Functions Here.

register = template.Library()


@register.filter
def add_ques_mark(string_value):

    chk = 0
    if string_value[len(string_value)-1:] != '?':

        string = string_value.split(' ')
        question_words = ['what', 'which', 'where', 'when', 'who', 'whom', 'whose', 'how', 'do', 'does', 'did']

        for s in string:
            if question_words.count( s.lower() ) > 0:
                chk = 1
                break

    if chk == 1:
        return string_value + ' ?'
    else:
        if string_value[len(string_value)-1 : len(string_value)] == '?':
            return string_value[:len(string_value)-1] + ' ?'
        else:
            return string_value



@register.filter
def upper_first_letter(string_value):

    string_value = str(string_value)

    if string_value[:1].islower():
        temp1 = string_value[1:]
        temp2 = string_value[:1].upper()

        # print('\nFirst Letter Question :', temp2+temp1, end='\n\n\n')
        return temp2 + temp1
    
    else:
        return string_value