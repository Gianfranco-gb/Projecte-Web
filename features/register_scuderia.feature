Feature: Register scuderia
  In order to keep track of the scuderies
  As a user
  I want to register a scuderia together with their name, main_color, principalDriver, secondaryDriver and num_championships

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a scuderia with all elements defined before
    Given I login as a user "user" with password "password"
    When I register a scuderia
      | name     | main color | principal Driver | secondary Driver | num championships |
      | Mercedes | Black      | Lewis Hamilton   | Valtteri Bottas  | 7                 |
    Then I'm viewing the details page for scuderia by "user"
      | name     | main color | principal Driver | secondary Driver | num championships |
      | Mercedes | Black      | Lewis Hamilton   | Valtteri Bottas  | 7                 |
    And there's 1 scuderia registered
