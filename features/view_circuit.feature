Feature: View circuits
  In order to know about a circuit,
  As a user,
  I want to view the registered circuits including all its information.

  Background: There's 2 circuits registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists a circuit registered by "user1"
      | name       | country | circuit length | laps in race | first gp | lap record |
      | MonteCarlo | Monaco  | 3.337 km       | 78           | 1950     | 1:14:260   |
    And Exists a circuit registered by "user2"
      | name     | country | circuit length | laps in race | first gp | lap record |
      | Montmelo | Spain   | 4.675 km       | 66           | 1913     | 1:18:441   |


  Scenario: View details about an owned circuit
    Given I login as a user "user1" with password "password1"
    When I view the details of circuit "MonteCarlo"
    Then I'm viewing circuit details including
      | name       | country | circuit length | laps in race | first gp | lap record |
      | MonteCarlo | Monaco  | 3.337 km       | 78           | 1950     | 1:14:260   |
    And there's "edit" link available


  Scenario: View details about other user circuit
    Given I login as a user "user1" with password "password1"
    When I view the details of circuit "Montmelo"
    Then I'm viewing circuit details including
      | name     | country | circuit length | laps in race | first gp | lap record |
      | Montmelo | Spain   | 4.675 km       | 66           | 1913     | 1:18:441   |
    And there's no "edit" link available
