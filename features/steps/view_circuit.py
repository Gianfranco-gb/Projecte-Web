from behave import *

use_step_matcher("parse")


@when('I see the details of circuit "{name}"')
@then('I\'m viewing circuit details including')
