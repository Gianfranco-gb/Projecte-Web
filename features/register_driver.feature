Feature: Register driver
  In order to keep track of the drivers
  As a user
  I want to register a driver together with their name, age, nationality, scuderia, height and weight

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a driver with all elements defined before
    Given I login as a user "user" with password "password"
    When I register a driver
      | name            | age | nationality | scuderia        | height | weight |
      | Fernando Alonso | 39  | Spain       | Alpine          | 1.71 m | 68 kg  |
    Then I'm viewing the details page for driver by "user"
      | name            | age | nationality | scuderia        | height | weight |
      | Fernando Alonso | 39  | Spain       | Alpine          | 1.71 m | 68 kg  |
    And there's 1 driver registered
