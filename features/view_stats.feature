Feature: View stats
  In order to know about a statistic,
  As a user,
  I want to view the stats details including all of its information.

  Background: There's 2 stats registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists a stat registered by "user1"
      | name           | num_of_championships | num_dif_teams |
      | Max Verstappen | 0                    | 2             |
    And Exists a stat registered by "user2"
      | name          | num_of_championships | num_dif_teams |
      | Jenson Button | 1                    | 7             |

  Scenario: View details about an owned stat
    Given I login as a user "user1" with password "password1"
    When I view the details of stat "Max Verstappen"
    Then I'm viewing stat details including
      | name           | num_of_championships | num_dif_teams |
      | Max Verstappen | 0                    | 2             |
    And there's "edit" link available


  Scenario: View details about other user stat
    Given I login as a user "user1" with password "password1"
    When I view the details of stat "Jenson Button"
    Then I'm viewing stat details including
      | name          | num_of_championships | num_dif_teams |
      | Jenson Button | 1                    | 7             |
    And there's no "edit" link available