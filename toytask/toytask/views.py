import json

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from . import modules


@csrf_exempt
def home(request):
    if request.method == 'POST':
        pipeline_str = request.POST.get('pipeline', False)
        if pipeline_str:
            pipeline = json.loads(pipeline_str)
            request.session['pipeline'] = pipeline
            return HttpResponseRedirect(reverse('params'))

    return render(request, 'pipeline.html', {
        'module_list': json.dumps(modules.info_list()),}
    )


@csrf_exempt
def params(request):
    pipeline = request.session.get('pipeline', False)
    if not pipeline:
        return HttpResponseRedirect(reverse('home'))

    form_list = []
    form_dict = modules.form_dict()
    info_dict = modules.info_dict()

    if request.method == 'GET':
        for module_handle in pipeline:
            form_class = form_dict[module_handle]
            info = info_dict[module_handle]
            form_list.append({
                'form': form_class(),
                'name': info['Name'],
                'description': info['Description'],}
            )
    elif request.method == 'POST':
        for module_handle in pipeline:
            form_class = form_dict[module_handle]
            info = info_dict[module_handle]
            form_list.append({
                'form': form_class(request.POST),
                'name': info['Name'],
                'description': info['Description'],}
            )

    return render(request, 'params.html', {
        'form_list': form_list,}
    )
