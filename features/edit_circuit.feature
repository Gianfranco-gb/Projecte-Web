Feature: Edit circuit
  In order to keep updated my previous registers about circuits,
  As a user,
  I want to edit a circuit register I created.

  Background: There are registered 2 users but only 1 circuit registered
    Given Exists a user "user" with password "password"
    And Exists a user "user2" with password "password"
    And Exists circuit registered by "user"
      | name     | country  | circuit_length | laps_in_race | first_gp | lap_record |
      | Portimao | Portugal | 4653           | 66           | 2020     | 1:18:750   |


  Scenario: Edit owned circuit
    Given I login as a user "user" with password "password"
    When  I edit the circuit with name "Portimao"
      | name     | country  | circuit_length | laps_in_race | first_gp | lap_record |
      | Portimao | Portugal | 4653           | 66           | 2020     | 1:17:000   |
    Then I'm viewing the details page for circuit by "user"
      | name     | country  | circuit_length | laps_in_race | first_gp | lap_record |
      | Portimao | Portugal | 4653           | 66           | 2020     | 1:17:000   |
    And There is 1 circuit




