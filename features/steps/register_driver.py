from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@given('Exists driver registered by this "{user}"')
def step_impl(context, user):
    from django.contrib.auth.models import User
    user = User.objects.get(user=user)
    from Pages.models import Driver
    for row in context.table:
        driver = Driver(user=user)
        for h in row.headings:
            setattr(driver, h, row[h])
        driver.save()


@when('I register a driver')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('driver_create'))
        if context.browser.url == context.get_url('driver_create'):
            form = context.browser.find_by_tag('form').first
            for h in row.headings:
                context.browser.fill(h, row[h])
            form.find_by_value('Submit').first.click()


@then('I\'m viewing the details page for driver by "{user}"')
def step_impl(context, user):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(user=user))))
    from Pages.models import Driver
    driver = Driver.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(driver)


@then("There's {count:n} driver registered")
def step_impl(context, count):
    from Pages.models import Driver
    assert count == Driver.objects.count()


@when('I edit the driver with name "{name}"')
def step_impl(context, name):
    from Pages.models import Driver
    driver = Driver.objects.get(name=name)
    context.browser.visit(context.get_url('driver_edit', driver.pk))
    if context.browser.url == context.get_url('driver_edit',driver.pk) and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first()
        for h in context.table.headings:
            context.browser.fill(h, context.table[0][h])
        form.find_by_value('Submit').first.click()


@when('I edit current driver')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    context.browser.visit(context.get_url('driver_edit'))
    form = context.browser.find_by_tag('form').first
    for h in context.table.headings:
        context.browser.fill(h, context.table[0][h])
    form.find_by_value('Submit').first.click()
