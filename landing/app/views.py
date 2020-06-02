from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter({'quantity':0})
counter_click = Counter({'original': 0, 'test': 0})


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    if request.GET['from-landing'] == 'original':
        counter_click ['original'] +=1
    elif request.GET['from-landing'] == 'test':
        counter_click ['test'] +=1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    counter_show['quantity']+=1
    if request.GET['ab-test-arg'] == 'original':
        return render_to_response('landing.html')
    elif request.GET['ab-test-arg'] == 'test':
        return render_to_response('landing_alternate.html')



def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    test_converstion = counter_click['test']/counter_show['quantity']
    original_converstion = counter_click['original']/counter_show['quantity']

    return render_to_response('stats.html', context={
        'test_conversion': test_converstion,
        'original_conversion': original_converstion,
    })
