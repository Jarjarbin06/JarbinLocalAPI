from os.path import join

from jarbinlocalapi.templates.main import TEMPLATES


template_overview = TEMPLATES.get_template(join("app", "system", "overview.html"))
template_cpu = TEMPLATES.get_template(join("app", "system", "cpu.html"))
template_memory = TEMPLATES.get_template(join("app", "system", "memory.html"))
template_battery = TEMPLATES.get_template(join("app", "system", "battery.html"))
template_disk = TEMPLATES.get_template(join("app", "system", "disk.html"))
template_network = TEMPLATES.get_template(join("app", "system", "network.html"))
template_processes = TEMPLATES.get_template(join("app", "system", "processes.html"))
template_system = TEMPLATES.get_template(join("app", "system", "system.html"))
template_temperatures = TEMPLATES.get_template(join("app", "system", "temperatures.html"))
template_top_processes = TEMPLATES.get_template(join("app", "system", "top_processes.html"))
