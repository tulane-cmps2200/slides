import glob
import re

def get_header(fname):
	try:
		return re.sub('#', '', open(fname).readlines()[0]).strip()
	except Exception as e:
		return 'name'

for module in sorted(glob.glob("module*")):
	module_title = '**%s**' % get_header('%s/README.md' % module)
	print('|[%50s](https://github.com/tulane-cmps2200/slides/tree/master/%s)|' % (module_title, module))
	for lecture in sorted(glob.glob('%s/0*' % module)):
		lecture_title = '&nbsp;&nbsp;%s' % get_header('%s/README.md' % (lecture))
		ipynb = 'n/a'
		try:
			ipynb = glob.glob('%s/*ipynb' % lecture)[0]
			ipynb = '[static](https://nbviewer.jupyter.org/github/tulane-cmps2200/slides/blob/master/%s?flush_cache=True)' % ipynb
		except:
			pass
		live = ' '
		try:
			live = glob.glob('%s/*ipynb' % lecture)[0]
			live = '[live](https://mybinder.org/v2/gh/tulane-cmps2200/slides/master?filepath=%s)' % live
		except:
			pass
		# pdf = ' '
		# try:
		# 	pdf = glob.glob('%s/*pdf' % lecture)[0]
		# 	pdf = '[pdf](https://github.com/tulane-cmps2200/slides/blob/master/%s)' % pdf
		# except:
		# 	pass

		print('|%50s %s/%s|' % 
			(lecture_title,  live, ipynb ))