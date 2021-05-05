Feature: Register seasons
  In order to keep track of the seasons
  As a user
  I want to register a season together with their year, num_gp, num_scuderias and world_champion

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a Season with all elements defined before
    Given I login as a user "user" with password "password"
    When I register a Season
      | year    |num GP   | num scuderias | world champion   |
      | 2010    |19       | 12            | Sebastian Vettel |
    Then I'm viewing the details page for Season by "user"
      | year    |num GP   | num scuderias | world champion   |
      | 2010    |19       | 12            | Sebastian Vettel |
    And there's 1 Season registered