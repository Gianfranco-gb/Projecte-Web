Feature: List stats
  In order to keep myself up to date about registered statistics,
  As a user,
  I want to list the last 2 registered statistics.

  Background: There are 3 registered stats by the same user
    Given Exists a user "user" with password "password"
    And Exists stats registered by this "user"
      | name           | num_of_championships | num_dif_teams |
      | Max Verstappen | 0                    | 2             |
      | Carlos Sainz   | 0                    | 4             |
      | Yuki Tsunoda   | 0                    | 1             |

  Scenario: List the last 2 stats
    When I list stats
    Then I'm viewing a list containing last 2 stats
      | name         |
      | Yuki Tsunoda |
      | Carlos Sainz |
    And The list contains 2 stats


  Scenario: List the last 2 stats
    Given Exist a stat registered by "user"
      | name           | num_of_championships | num_dif_teams |
      | Lewis Hamilton | 7                    | 2             |
    When I list stats
    Then I'm viewing a list containing last 2 stats
      | name           |
      | Lewis Hamilton |
      | Yuki Tsunoda   |
    And The list contains 2 stats