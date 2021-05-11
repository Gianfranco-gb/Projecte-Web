from behave import *

use_step_matcher("parse")


@when('I list circuits')
def step_impl(context):
    context.browser.visit(context.get_url('circuit'))


@then('I\'m viewing a list containing last 2 circuits')
def step_impl(context):
    circuit_links = context.browser.find_by_css('div#content ul li')
    for i, row in enumerate(context.table):
        assert row['name'] == circuit_links[i].text
        assert row['country'] == circuit_links[i].text


@step("The list contains {count:n} circuits")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li'))
