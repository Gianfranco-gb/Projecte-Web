Feature: View drivers
  In order to know about a driver,
  As a user,
  I want to view the drivers details including all its details.

  Background: There's 2 drivers registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists a driver registered by "user1"
      | name            | age | nationality | scuderia | height | weight |
      | Fernando Alonso | 39  | Spain       | Alpine   | 1.71   | 68     |
    And Exists a driver registered by "user2"
      | name            | age | nationality | scuderia | height | weight |
      | Charles Leclerc | 23  | Monaco      | Ferrari  | 1.80   | 70     |

  Scenario: View details about an owned driver
    Given I login as a user "user1" with password "password1"
    When I view the details of driver "Fernando Alonso"
    Then I'm viewing driver details including
      | name            | age | nationality | scuderia | height | weight |
      | Fernando Alonso | 39  | Spain       | Alpine   | 1.71   | 68     |
    And there's "edit" link available


  Scenario: View details about other user driver
    Given I login as a user "user1" with password "password1"
    When I view the details of driver "Charles Leclerc"
    Then I'm viewing driver details including
      | name            | age | nationality | scuderia | height | weight |
      | Charles Leclerc | 23  | Monaco      | Ferrari  | 1.80   | 70     |
    And there's no "edit" link available