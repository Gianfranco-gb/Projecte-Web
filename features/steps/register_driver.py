from behave import *

use_step_matcher("parse")


@given('Exists driver registered by this "{user}"')
@when('I register a driver')
@then('I\'m viewing the details page for circuit by "{user}"')
@then("There's {count:n} driver registered")
@when('I edit the driver with name "{name}"')
@when('I edit the current driver')
