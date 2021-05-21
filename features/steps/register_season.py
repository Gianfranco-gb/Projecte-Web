from functools import reduce
import operator
from behave import *
from django.db.models import Q

use_step_matcher("parse")


@given(u'Exists season registered by "{user}"')
def step_impl(context, user):
    from django.contrib.auth.models import User
    user = User.objects.get(username=user)
    from Pages.models import Season
    for row in context.table:
        season = Season(user=user)
        for h in row.headings:
            setattr(season, h, row[h])
        season.save()


@when(u'I register a season')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('season_create'))
        if context.browser.url == context.get_url('season_create'):
            form = context.browser.find_by_tag('form').first
            for h in row.headings:
                context.browser.fill(h, row[h])
            form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for season by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from Pages.models import Season
    seasons = Season.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(seasons)


@then(u"There is {count:n} season")
def step_impl(context, count):
    from Pages.models import Season
    assert count == Season.objects.count()


@when(u'I edit the season with year "{year}"')
def step_impl(context, year):
    from Pages.models import Season
    season = Season.objects.get(year=year)
    context.browser.visit(context.get_url('season_edit', season.pk))
    if context.browser.url == context.get_url('season_edit', season.pk) and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for h in context.table.headings:
            context.browser.fill(h, context.table[0][h])
        form.find_by_value('Submit').first.click()


