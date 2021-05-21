Feature: Register seasons
  In order to keep track of the seasons
  As a user
  I want to register a season together with their year, num_gp, num_scuderias and world_champion

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a Season with all elements defined before
    Given I login as a user "user" with password "password"
    When I register a season
      | year    |num_gp   | num_scuderias | world_champion   | scuderia_champion |
      | 2010    |19       | 12            | Sebastian Vettel |  Alpine           |
    Then I'm viewing the details page for season by "user"
      | year    |num_gp   | num_scuderias | world_champion   | scuderia_champion |
      | 2010    |19       | 12            | Sebastian Vettel |  Alpine           |
    And There is 1 season