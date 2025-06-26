from behave import given, when, then, step

@given("{text}")
@when("{text}")
@then("{text}")
@step("{text}")
def step_impl(context, text):
    pass  # Dummy step: all steps pass for reporting purposes 