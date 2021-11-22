from pytest_bdd import parsers
from behave import *
from pytest import raises
import fullretirement


@given("that the application system is working properly")
def program_running_properly():
    pass


@then(parsers.parse('Year'))
@when('year is prompted to be input, end-user should enter a year between 1900 to 2999')
def year_test(year):
    with raises(OSError):
        fullretirement.validate_year(year)


@then(parsers.parse('Month'))
@when('month is prompted to be input, end-user should enter a month between 1 to 12')
def month_test(month):
    with raises(OSError):
        fullretirement.validate_month(month)


@then(parsers.parse('Ouput is calculated'))
@then('the output is shown according to the month and year the end-user suggested to the system')
def valid_calc(output, month, year):
    assert str(fullretirement.calculate_nra(year, month)) == str(output)


@when('"1899" is entered for year')
def year_test():
    with raises(OSError):
        fullretirement.validate_year(1899)


@when('"3050" is entered for year')
def year_test():
    with raises(OSError):
        fullretirement.validate_year(3050)

@when('1945 year and 6 month is entered')
def year_and_month_test_one():
    #the program should tell the user he will retire in January 2002
    pass

@when('year is 1945 and month is 6')
def year_and_month_test_two():
    #the program should tell year = 2010 and month is June. Since only creates a 66 y/o retirement
    pass

@when('"-1980" is entered for year')
def negative_year_test():
    with raises(OSError):
        fullretirement.validate_year(-1980)

@when('"-5" is entered for month')
def negative_month_test():
    with raises(OSError):
        fullretirement.validate_month(-5)

@when('"3050" is entered for year')
def month_greater_than_twelve():
    with raises(OSError):
        fullretirement.validate_year(15)

