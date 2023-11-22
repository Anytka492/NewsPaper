from django import template
import re
register = template.Library()

cens = ['дурак','хрен', 'мат', 'дурака', 'конь', 'дурак', 'простофиля', 'дураком', 'fool', 'dumkopf', 'недалекий']

@register.filter()
def change_querry(value):
    if isinstance(value, str):
        text = []
        text1 = value.split(" ")
        for i in text1:
            g = i.lower()
            if g.isalpha():
                if g in cens:
                    g = "**" + g[2:]
            elif g[:-1] in cens:
                g = "**" + g[2:]
            text.append(g)
        return " ".join(text)
    else:
        raise ValueError("Ошибка! Введите строковое значение")
