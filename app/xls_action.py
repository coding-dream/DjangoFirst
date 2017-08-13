from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

address = [
    ('张三', '地址一'),
    ('李四', '地址二')
    ]
@csrf_exempt
def download(request, filename):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % filename

    template = loader.get_template('xls.html')
    dist = {'data': address}
    response.write(template.render(dist))
    return response