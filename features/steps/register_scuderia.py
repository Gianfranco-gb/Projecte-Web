from behave import *

use_step_matcher("parse")


@given('Exists scuderia registered by this "{user}"')
@when('I register a scuderia')
@then('I\'m viewing the details page for scuderia by "{user}"')
@then("There's {count:n} scuderia registered")
@when('I edit the scuderia with name "{name}"')
@when('I edit the current scuderia')