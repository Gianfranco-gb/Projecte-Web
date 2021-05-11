from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@given(u'Exists circuit registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from Pages.models import Circuit
    for row in context.table:
        circuit = Circuit(user=user)
        for heading in row.headings:
            setattr(circuit, heading, row[heading])
        circuit.save()


@when(u'I register a circuit')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('circuit_create'))
        if context.browser.url == context.get_url('circuit_create'):
            form = context.browser.find_by_tag('form').first
            for h in row.headings:
                context.browser.fill(h, row[h])
            form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for circuit by "{user}"')
def step_impl(context, user):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(user=user))))
    from Pages.models import Circuit
    circuit = Circuit.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(circuit)


@then(u'There is {count:n} circuit')
def step_impl(context, count):
    from Pages.models import Circuit
    assert count == Circuit.objects.count()


@when(u'I edit the circuit with name "{name}"')
def step_impl(context, name):
    from Pages.models import Circuit
    circuit = Circuit.objects.get(name=name)
    context.browser.visit(context.get_url('circuit_edit'), circuit.pk)
    if context.browser.url == context.get_url('circuit_edit', circuit.pk) and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first()
        for h in context.table.headings:
            context.browser.fill(h, context.table[0][h])
        form.find_by_value('Submit').first.click()


@when(u'I edit current circuit')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    context.browser.visit(context.get_url('circuit_edit'))
    form = context.browser.find_by_tag('form').first
    for h in context.table.headings:
        context.browser.fill(h, context.table[0][h])
    form.find_by_value('Submit').first.click()
