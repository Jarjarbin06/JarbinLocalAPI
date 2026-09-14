from os.path import join

from jarbinlocalapi.templates.main import TEMPLATES


template_overview = TEMPLATES.get_template(join("system", "overview.html"))
template_cpu = TEMPLATES.get_template(join("system", "cpu.html"))
template_memory = TEMPLATES.get_template(join("system", "memory.html"))
template_battery = TEMPLATES.get_template(join("system", "battery.html"))
template_disk = TEMPLATES.get_template(join("system", "disk.html"))
template_network = TEMPLATES.get_template(join("system", "network.html"))
template_processes = TEMPLATES.get_template(join("system", "processes.html"))
template_system = TEMPLATES.get_template(join("system", "system.html"))
template_temperatures = TEMPLATES.get_template(join("system", "temperatures.html"))
template_top_processes = TEMPLATES.get_template(join("system", "top_processes.html"))
