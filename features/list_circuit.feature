Feature: List circuit
  In order to keep myself up to date about registered circuits,
  As a user,
  I want to list the last 2 registered circuits.


  Background: There are 3 registered circuits by the same user
    Given Exists a user "user" with password "password"
    And Exists circuits registered by this "user"
      | name      | country    | circuit length | laps in race | first gp | lap record |
      | MonteCarlo| Monaco     | 3.337 km       | 78           | 1950     | 1:14:260   |
      | Barhain   | Barhain    | 5.412 km       | 57           | 2004     | 1.31.447   |
      | Baku City | Azerbaijan | 6.003 km       | 51           | 2016     | 1:43:009   |

  Scenario: List the last 2 circuits
    When I list circuits
    Then I'm viewing a list containing last 2 circuits
      | name      |
      | Baku City |
      | Barhain   |
    And The list contains 2 circuits

  Scenario: List the last 2 circuits
    Given Exist a circuit registered by "user"
      | name     | country | circuit length | laps in race | first gp | lap record |
      | Montmelo | Spain   | 4.675 km       | 66           | 1913     | 1:18:441   |
    When I list circuits
    Then I'm viewing a list containing last 2 circuits
      | name      |
      | Montmelo  |
      | Baku City |
    And The list contains 2 circuits