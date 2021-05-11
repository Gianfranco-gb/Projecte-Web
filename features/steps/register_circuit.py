from behave import *

use_step_matcher("parse")


@given('Exists circuits registered by this "{user}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from Pages.models import Circuit
    for row in context.table:
        circuit = Circuit(user=user)
        for heading in row.headings:
            setattr(circuit, heading, row[heading])
        circuit.save()


@when('I register a circuit')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('myrestaurants:restaurant_create'))
        if context.browser.url == context.get_url('myrestaurants:restaurant_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()