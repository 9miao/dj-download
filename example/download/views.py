#-*- encoding:UTF-8 -*-


import os.path

from django.core.servers.basehttp import FileWrapper
from django.http import Http404
from django.http import HttpResponse


FILE_FOLDER = '/tmp/'


def tarball(request, release):

	file_name = 'dj-download-%s.tar.gz' % release
	file_path = os.path.join(FILE_FOLDER, file_name)
	try:
		tarball_file = open(file_path)
	except IOError:
		raise Http404
	wrapper = FileWrapper(tarball_file)
	response = HttpResponse(wrapper, content_type='application/zip')
	response['Content-Encoding'] = 'utf-8'  # 设置该值gzip中间件就会直接返回而不进行后续操作
	response['Content-Disposition'] = 'attachment; filename=%s' % file_name
	return response
