Feature: List stats
  In order to keep myself up to date about registered statistics,
  As a user,
  I want to list the last 2 registered statistics.

  Background: There are 3 registered stats by the same user
    Given Exists a user "user" with password "password"
    And Exists stats registered by this "user"
      | name Driver    | num of championships  | num dif teams |
      | Max Verstappen | 0                     | 2             |
      | Carlos Sainz   | 0                     | 4             |
      | Yuki Tsunoda   | 0                     | 1             |

  Scenario: List the last 2 stats
    When I list stats (only name driver)
    Then I'm viewing a list containing
      | name Driver    |
      | Yuki Tsunoda   |
      | Carlos Sainz   |
    And The list contains 2 stats


  Scenario: List the last 2 stats
    Given Exist a stat registered by "user"
      | name Driver    | num of championships  | num dif teams |
      | Lewis Hamilton | 7                     | 2             |
    When I list stats (only name, age and nationality)
    Then I'm viewing a list containing
      | name Driver    |
      | Lewis Hamilton |
      | Yuki Tsunoda   |
    And The list contains 2 stats