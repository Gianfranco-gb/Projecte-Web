from behave import *

use_step_matcher("parse")


@when('I list seasons')
def step_impl(context):
    context.browser.visit(context.get_url('season'))


@then('I\'m viewing a list containing last 2 seasons')
def step_impl(context):
    circuit_links = context.browser.find_by_css('')
    for i, row in enumerate(context.table):
        assert row['name'] == circuit_links[i].text


@step("The list contains {count:n} seasons")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css(''))
