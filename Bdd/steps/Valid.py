
#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from behave import *

from ..Conversion import century


@given('i have an year {year}')
def step_impl(context, year):
    context.year = year

@when('i convert it')
def step_impl(context):
    context.result = century(context.year)

@then('i should get {result}')
def step_impl(context, result):
    assert str ( context.result ) == result, '{} Should be {}'.format(context.year, result)