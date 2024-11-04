from jinja2 import Template
#
# msg = '''{%raw%} Мое дефолтное имя - {{ Всеволод }} {%endraw%}'''
# tm = Template(msg)
# rn = tm.render(name='Андрей')
# print(rn)
#
# msg = ''' Мое дефолтное имя - {{Всеволод}} '''
# tm = Template(msg)
# rn = tm.render(Всеволод='Андрей ')
# print(rn)
#
# msg = ''' Мое дефолтное имя - {{Всеволод}} '''
# tm = Template('{{ msg }}')
# rn = tm.render(msg=msg)
# print(rn)
#
# html_snippet = 'Ссылка: <a href="#">Ссылка</a>'
# tm = Template(html_snippet)
# rn = tm.render()
# print(rn)
#
# html_snippet = 'Ссылка: <a href="#">Ссылка</a>'
# tm = Template('{{ html_snippet | e }}')
# rn = tm.render(html_snippet = html_snippet)
# print(rn)

data = [
    {"Имя": "Алиса", "Возраст": 25, "Город": "Москва"},
    {"Имя": "Боб", "Возраст": 30, "Город": "Санкт-Петербург"},
    {"Имя": "Чарли", "Возраст": 35, "Город": "Новосибирск"}
]

msg = """
{%for item in  data -%}
    {% if item.Возраст > 25 -%}
        name = {{ item.Имя}}
    {%endif-%}       
{%endfor-%}           
"""
tm = Template(msg)
rn = tm.render(data = data)
print(rn)

