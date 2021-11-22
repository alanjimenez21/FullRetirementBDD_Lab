Feature: FullRetirementAge
  As an end-user, I want to know the exact date of my retirement in the United States.
  The application should show me the exact year and date according to the website dates.

  Scenario Outline: The calculations will have to follow certain rules in order to show proper results.
    Given that the application system is working properly
    When year is prompted to be input, end-user should enter a year between 1900 to 2999
    When month is prompted to be input, end-user should enter a month between 1 to 12
    Then the output is shown according to the month and year the end-user suggested to the system.



  Scenario: Input a number less than the year 1900
    Given that the application system is working properly
    When the user inputs 1899
    Then the program should tell the user that the input number is not valid.

  Scenario: As an end-user, I want to see what would happen if I input a number greater than 3000
    Given that the application system is working properly
    When the user inputs 3050
    Then the program should tell the user that the input number is not valid as it is not in the range of 1900 - 2999.

  Scenario: As an end-user, I want to see what would happen if I input a number that will give me a retirement age of 65 y/o
    Given that the application system is working properly
    When  Input a number less than the year 1937 and Input 1 as a month
    Then the program should tell the user he will retire in January 2002.

    Scenario: As an end-user, I want to see what would happen if I input a number between the ranges of 1943 and 1954
    Given that the application system is working properly
    When  the user inputs 1945 and 6 as a month
    Then the program should tell year = 2010 and month is June. Since only creates a 66 y/o retirement

    Scenario:  As an end-user, I want to see what would happen if I input a negative number year
    Given that the application system is working properly
    When the user inputs -1980 and month 5
    Then the program should prompt the error that there should not be negative values

    Scenario: As an end-user, I want to see what would happen if I input a negative number month
    Given that the application system is working properly
    When the user inputs 1980 and month -5
    Then the program should prompt the error that there should not be negative values

    Scenario: As an end-user, I want to see what would happen if I input a number greater than twelve in months
    Given that the application system is working properly
    When the user inputs 1980 and month 15
    Then the program should prompt the error that there are no values greater than 12 in months.
