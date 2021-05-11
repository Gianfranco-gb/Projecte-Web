from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@given('Exists circuit registered by this "{user}"')
def step_impl(context, user):
    from django.contrib.auth.models import User
    user = User.objects.get(user=user)
    from Pages.models import Circuit
    for row in context.table:
        circuit = Circuit(user=user)
        for h in row.headings:
            setattr(circuit, h, row[h])
        circuit.save()


@when('I register a circuit')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('circuit_create'))
        if context.browser.url == context.get_url('circuit_create'):
            form = context.browser.find_by_tag('form').first
            for h in row.headings:
                context.browser.fill(h, row[h])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for circuit by "{user}"')
def step_impl(context, user):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(user=user))))
    from Pages.models import Circuit
    circuit = Circuit.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(circuit)


@then("There's {count:n} circuit registered")
def step_impl(context, count):
    from Pages.models import Circuit
    assert count == Circuit.objects.count()


@when('I edit the circuit with name "{name}"')
def step_impl(context, name):
    from Pages.models import Circuit
    circuit = Circuit.objects.get(name=name)
    context.browser.visit(context.get_url('circuit_edit'), circuit.pk)
    if context.browser.url == context.get_url('circuit_edit', circuit.pk) and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first()
        for h in context.table.headings:
            context.browser.fill(h, context.table[0][h])
        form.find_by_value('Submit').first.click()


@when('I edit current circuit')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    context.browser.visit(context.get_url('circuit_edit'))
    form = context.browser.find_by_tag('form').first
    for h in context.table.headings:
        context.browser.fill(h, context.table[0][h])
    form.find_by_value('Submit').first.click()
