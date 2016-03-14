import json
import os
import random

import cv2
from toytask.settings import STATICFILES_DIRS
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from . import modules


def imagepath(imagename):
    static_dir = STATICFILES_DIRS[0]
    return os.path.join(static_dir, 'images', imagename)


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
        for i, module_handle in enumerate(pipeline):
            form_class = form_dict[module_handle]
            info = info_dict[module_handle]
            form_list.append({
                'form': form_class(prefix='form_'+str(i)),
                'name': info['Name'],}
            )
    elif request.method == 'POST':
        for i, module_handle in enumerate(pipeline):
            form_class = form_dict[module_handle]
            info = info_dict[module_handle]
            form_list.append({
                'form': form_class(request.POST, prefix='form_'+str(i)),
                'name': info['Name'],}
            )

        for form in form_list:
            if not form['form'].is_valid():
                break
        else:
            image_list = []
            for i, form in enumerate(form_list):
                model = form['form'].save(commit=False)

                imgpath = imagepath('lena.png')
                img = cv2.imread(imgpath)

                dst = model.module_func(img)

                dstname = 'lena_{0}.png'.format(random.randrange(1, 100))
                cv2.imwrite(imagepath(dstname), dst)
                image_list.append(dstname)

            return render(request, 'result.html', {
                'image_list': image_list,}
            )

    return render(request, 'params.html', {
        'form_list': form_list,}
    )
