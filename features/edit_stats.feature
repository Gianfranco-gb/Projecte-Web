Feature: Edit stats
  In order to keep updated my previous registers about statistics,
  As a user,
  I want to edit a stats register I created.

  Background: There are registered 2 users but only 1 stat registered
    Given Exists a user "user" with password "password"
    And Exists a user "user2" with password "password"
    And Exists stats registered by "user"
      | name           |num_of_championships  | num_dif_teams |
      | Max Verstappen | 0                    | 2             |


  Scenario: Edit owned stat
    Given I login as a user "user" with password "password"
    When I edit the stats with name "Max Verstappen"
      | name           |num_of_championships  | num_dif_teams |
      | Max Verstappen | 1                    | 2             |
    Then I'm viewing the details page for stats by "user"
      | name           |num_of_championships  | num_dif_teams |
      | Max Verstappen | 1                    | 2             |
    And There is 1 stats

