Feature: Register circuits
  In order to keep track of the circuits
  As a user
  I want to register a circuits together with their name, country, circuit_length, laps_in_race, first_gp and lap_record

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register a circuit with all elements defined before
    Given I login as a user "user" with password "password"
    When I register a circuit
      | name       | country | circuit length | laps in race | first gp | lap record |
      | MonteCarlo | Monaco  | 3.337 km       | 78           | 1950     | 1:14:260   |
    Then I'm viewing the details page for circuit by "user"
      | name       | country | circuit length | laps in race | first gp | lap record |
      | MonteCarlo | Monaco  | 3.337 km       | 78           | 1950     | 1:14:260   |
    And there's 1 circuit registered


