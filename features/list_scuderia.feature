Feature: List scuderia
  In order to keep myself up to date about registered scuderias,
  As a user,
  I want to list the last 2 registered scuderias.

  Background: There are 3 registered scuderias by the same user
    Given Exists a user "user" with password "password"
    And Exists drivers registered by this "user"
      | name     | main color | principal Driver | secondary Driver   | num championships |
      | Mercedes | Black      | Lewis Hamilton   | Valtteri Bottas    | 7                 |
      | RedBull  | Navy Blue  | Max Verstappen   | Sergio Perez       | 4                 |
      | AlfaRomeo| White      | Kimi Raikkonen   | Antonio Giovinazzi | 0                 |

  Scenario: List the last 2 scuderias
    When I list scuderias (only name)
    Then I'm viewing a list containing
      | name      |
      | AlfaRomeo |
      | RedBull   |
    And The list contains 2 scuderias


  Scenario: List the last 2 scuderias
    Given Exist a scuderias registered by "user"
      | name     | main color | principal Driver | secondary Driver   | num championships |
      | Haas     | White      | Mick Schumacher  | Nikita Mazepin     | 0                 |
    When I list scuderias (only name, age and nationality)
    Then I'm viewing a list containing
      | name      |
      | Haas      |
      | AlfaRomeo |
    And The list contains 2 scuderias