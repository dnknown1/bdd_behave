from behave import given, when, then
@given(u'key')
def step_impl(ctx):
    ctx.key = 5


@when(u'io')
def step_impl(ctx):
    ctx.io = 5


@then(u'match')
def step_impl(ctx):
    assert ctx.key == ctx.io