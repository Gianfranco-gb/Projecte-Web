from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@given(u'Exists stats registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from Pages.models import StatisticsDriver
    for row in context.table:
        stats = StatisticsDriver(user=user)
        for h in row.headings:
            setattr(stats, h, row[h])
        stats.save()


@when(u'I register a stats')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('stats_create'))
        if context.browser.url == context.get_url('stats_create'):
            form = context.browser.find_by_tag('form').first
            for h in row.headings:
                context.browser.fill(h, row[h])
            form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for stats by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from Pages.models import StatisticsDriver
    stats = StatisticsDriver.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(stats)


@then(u"There is {count:n} stats")
def step_impl(context, count):
    from Pages.models import StatisticsDriver
    assert count == StatisticsDriver.objects.count()


@when(u'I edit the stats with name "{name}"')
def step_impl(context, name):
    from Pages.models import StatisticsDriver
    stats = StatisticsDriver.objects.get(name=name)
    context.browser.visit(context.get_url('stats_edit', stats.pk))
    if context.browser.url == context.get_url('stats_edit', stats.pk) and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for h in context.table.headings:
            context.browser.fill(h, context.table[0][h])
        form.find_by_value('Submit').first.click()


