Feature: Edit circuit
  In order to keep updated my previous registers about circuits,
  As a user,
  I want to edit a circuit register I created.

  Background: There are registered 2 users but only 1 circuit registered
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists circuit registered by "user1"
      | name     | country  | circuit_length | laps_in_race | first_gp | lap_record |
      | Portimao | Portugal | 4653           | 66           | 2020     | 1:18:750   |


  Scenario: Edit owned circuit
    Given I login as a user "user1" with password "password"
    When  I edit the circuit with name "Portimao"
      | name     | country  | circuit_length | laps_in_race | first_gp | lap_record |
      | Portimao | Portugal | 4653           | 66           | 2020     | 1:17:000   |
    Then I'm viewing the details page for circuit by "user1"
      | name     | country  | circuit_length | laps_in_race | first_gp | lap_record |
      | Portimao | Portugal | 4653           | 66           | 2020     | 1:17:000   |
    And There is 1 circuit

  Scenario: Try to edit not owned circuit
    Given I login as a user "user2" with password "password"
    When  I view the details for circuit "Portimao"
    Then There is no "edit" link available


  Scenario: Force edit circuit but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the circuit with name "Portimao"
      | name     | country  | circuit_length | laps_in_race | first_gp | lap_record |
      | Portimao | Portugal | 4653           | 80           | 2020     | 1:18:750   |
    Then Server responds with page containing "403 Forbidden"


