Feature: Register stats
  In order to keep track of the statistics of the drivers
  As a user
  I want to register a stats together with their nameDriver, num_of_championships and num_dif_teams

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a stat with all elements defined before
    Given I login as a user "user" with password "password"
    When I register a stat
      | name Driver    |num of championships  | num dif teams |
      | Max Verstappen | 0                    | 2             |
    Then I'm viewing the details page for stats by "user"
      | name Driver    |num of championships  | num dif teams |
      | Max Verstappen | 0                    | 2             |
    And there's 1 stat registered