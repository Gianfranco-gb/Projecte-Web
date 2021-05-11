from behave import *

use_step_matcher("parse")


@when(u'I list stats')
def step_impl(context):
    context.browser.visit(context.get_url('stats'))


@then(u'I\'m viewing a list containing last 2 stats')
def step_impl(context):
    circuit_links = context.browser.find_by_css('')
    for i, row in enumerate(context.table):
        assert row['name'] == circuit_links[i].text


@step(u"The list contains {count:n} stats")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css(''))
