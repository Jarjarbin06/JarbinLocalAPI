from os.path import join

from jarbinlocalapi.app.templates.main import TEMPLATES


template_overview = TEMPLATES.get_template(join("system", "overview.html"))
template_cpu = TEMPLATES.get_template(join("system", "cpu.html"))
template_memory = TEMPLATES.get_template(join("system", "memory.html"))
