Feature: View scuderia
  In order to know about a scuderia,
  As a user,
  I want to view the scuderia details including all its information.


  Background: There's 2 scuderias registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists a scuderia registered by "user1"
      | name     | main color | principal Driver | secondary Driver | num championships |
      | Mercedes | Black      | Lewis Hamilton   | Valtteri Bottas  | 7                 |
    And Exists a scuderia registered by "user2"
      | name         | main color | principal Driver | secondary Driver | num championships |
      | Aston Martin | Green      | Sebastian Vettel | Lance Stroll     | 0                 |

  Scenario: View details about an owned scuderia
    Given I login as a user "user1" with password "password1"
    When I view the details of scuderia "Mercedes"
    Then I'm viewing scuderia details including
      | name     | main color | principal Driver | secondary Driver | num championships |
      | Mercedes | Black      | Lewis Hamilton   | Valtteri Bottas  | 7                 |
    And there's "edit" link available


  Scenario: View details about other user scuderia
    Given I login as a user "user1" with password "password1"
    When I view the details of scuderia "Aston Martin"
    Then I'm viewing scuderia details including
      | name         | main color | principal Driver | secondary Driver | num championships |
      | Aston Martin | Green      | Sebastian Vettel | Lance Stroll     | 0                 |
    And there's no "edit" link available