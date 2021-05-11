from behave import *

use_step_matcher("parse")


@given('Exists circuit registered by this "{user}"')
@when('I register a circuit')
@then('I\'m viewing the details page for circuit by "{user}"')
@then("There's {count:n} circuit registered")
@when('I edit the circuit with name "{name}"')
@when('I edit the current circuit')