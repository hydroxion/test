
Feature: convert year to century

Scenario Outline: convert year
    Given i have an year <year>
    When i convert it
    Then i should get <status>

Examples: test values of years
    | year          | status |
    | 1905          | 20     |
    | 1700          | 17     |
    | 200           | 2      |

