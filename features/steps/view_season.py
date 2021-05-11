from behave import *

use_step_matcher("parse")


@when('I see the details of season "{name}"')
@then('I\'m viewing season details including')
