Feature: Edit circuit
  In order to keep updated my previous registers about circuits,
  As a user,
  I want to edit a circuit register I created.

  Background: There are registered 2 users but only 1 circuit registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists circuit registered by "user1"
      | name     | country  | circuit length | laps in race | first gp | lap record |
      | Portimao | Portugal | 4.653 km       | 66           | 2020     | 1:18:750   |
    And Exists circuit registered by "user1"


  Scenario: Edit owned circuit (have to edit all fields)
    Given I login as a user "user1" with password "password1"
    When  I view the details for circuit "Portimao"
    And I edit current circuit
      | name     | country  | circuit length | laps in race | first gp | lap record |
      | Portimao | Portugal | 4.653 km       | 66           | 2020     | 1:17:000   |
    Then I'm viewing the details page for circuit "Portimao" by "user1"
      | name     | country  | circuit length | laps in race | first gp | lap record |
      | Portimao | Portugal | 4.653 km       | 66           | 2020     | 1:17:000   |
    And there's 1 circuit

  Scenario: Try to edit not owned circuit
    Given I login as a user "user2" with password "password2"
    When  I view the details for circuit "Portimao"
    Then there's no "edit" link available


  Scenario: Force edit circuit but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the circuit with name "Portimao"
      | name     | country  | circuit length | laps in race | first gp | lap record |
      | Portimao | Portugal | 4.653 km       | 80           | 2020     | 1:18:750   |
    Then Server responds with page containing "403 Forbidden"


