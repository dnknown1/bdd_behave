
from behave import *

@given(u'a sample text loaded into the frobulator')
def step_impl(context):
    context.c = context.text.strip()


@when(u'we activate the frobulator')
def step_impl(context):
    print(context.c)


@then(u'we will find Hi')
def step_impl(context):
    assert context.c == 'Hi'
