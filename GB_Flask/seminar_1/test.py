#
# poem = [
#         'Вот не думал, не гадал,',
#         'Программистом взял и стал.'
#         'Хитрый знает он язык,',
#         'Он к другому не привык.',
#     ]
# d ='<br/>'.join(poem)
# print(d)


from jinja2 import Template

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 5, 'city': 'Тверь'},
          {'id': 7, 'city': 'Минск'},
          {'id': 8, 'city': 'Смоленск'},
          {'id': 11, 'city': 'Калуга'}]

link = '''<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{%else -%}
    {{c['city']}}
{% endif -%}
{% endfor -%}
</select>'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)