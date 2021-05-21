Feature: Register stats
  In order to keep track of the statistics of the drivers
  As a user
  I want to register a stats together with their nameDriver, num_of_championships and num_dif_teams

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a stat with all elements defined before
    Given I login as a user "user" with password "password"
    When I register a stats
      | name           |num_of_championships  | num_dif_teams |
      | Max Verstappen | 0                    | 2             |
    Then I'm viewing the details page for stats by "user"
      | name           |num_of_championships  | num_dif_teams |
      | Max Verstappen | 0                    | 2             |
    And There is 1 stats