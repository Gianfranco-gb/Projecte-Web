from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@given(u'Exists scuderia registered by this "{user}"')
def step_impl(context, user):
    from django.contrib.auth.models import User
    user = User.objects.get(user=user)
    from Pages.models import Scuderia
    for row in context.table:
        scuderia = Scuderia(user=user)
        for h in row.headings:
            setattr(scuderia, h, row[h])
        scuderia.save()


@when(u'I register a scuderia')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('scuderia_create'))
        if context.browser.url == context.get_url('scuderia_create'):
            form = context.browser.find_by_tag('form').first
            for h in row.headings:
                context.browser.fill(h, row[h])
            form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for scuderia by "{user}"')
def step_impl(context, user):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(user=user))))
    from Pages.models import Scuderia
    scuderia = Scuderia.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(scuderia)


@then(u"There's {count:n} scuderia registered")
def step_impl(context, count):
    from Pages.models import Scuderia
    assert count == Scuderia.objects.count()


@when(u'I edit the scuderia with name "{name}"')
def step_impl(context, name):
    from Pages.models import Scuderia
    scuderia = Scuderia.objects.get(name=name)
    context.browser.visit(context.get_url('scuderia_edit', scuderia.pk))
    if context.browser.url == context.get_url('scuderia_edit', scuderia.pk) and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first()
        for h in context.table.headings:
            context.browser.fill(h, context.table[0][h])
        form.find_by_value('Submit').first.click()


@when(u'I edit current scuderia')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    context.browser.visit(context.get_url('scuderia_edit'))
    form = context.browser.find_by_tag('form').first
    for h in context.table.headings:
        context.browser.fill(h, context.table[0][h])
    form.find_by_value('Submit').first.click()
