from django.shortcuts import render

from django.http import HttpResponse, Http404
from random import randint

from page.fake_db.pages import FAKE_DB_PAGES

# FAKE_DB_PROJECTS = [
#     f"https://picsum.photos/id/{id}/100/80" for id in range (21, 29)
# ]

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range (24, 28)
]

def home_view(request):
    # print("request:::", request.META)
    # print("request:::", request.HEADERS)
    # return HttpResponse('Ana sayfaya hosgeldiniz..')
    # context = {"platform": f"Django platformu kullanildi ve randint ile dönen veri: {randint(1,100)}"}
    context = dict(
        # FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL=FAKE_DB_CAROUSEL,
    )
    return render(request, "page/home_page.html", context)

def about_us_view (request):
    page_title = 'Hakkimizda'
    hero_content = 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vitae optio laboriosam consequuntur id quisquam, sed culpa. Temporibus animi neque incidunt.'
    context = {
        'page_title': page_title,
    }
    context['hero_content'] = hero_content
    # context['FAKE_DB_PROJECTS'] = FAKE_DB_PROJECTS
    return render(request,"page/about_us.html", context )

def vision_view (request):
    page_title = 'Vizyonumuz'
    context = dict(
        page_title=page_title,
        # FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request,"page/vision.html", context )
    
def contact_us_view (request):
    page_title = 'iletisim'
    hero_content = 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vitae optio laboriosam consequuntur id quisquam, sed culpa. Temporibus animi neque incidunt.'
    context = dict(
        page_title=page_title,
        hero_content = hero_content,
        # FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request,"page/contact_us.html", context )

def page_view (request, slug):
    result = list(filter (lambda x: (x['url'] == slug), FAKE_DB_PAGES))
    if result:
        context = dict(
            page_title=result[0]['title'],
            # FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
            detail = result[0]['detail'],
        )
        # print(context)
        return render(request,"page/page_detail.html", context )
    raise Http404

