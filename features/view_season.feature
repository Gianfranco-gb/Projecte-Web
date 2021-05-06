Feature: View season
  In order to know about a season,
  As a user,
  I want to view the season details including all its information.

  Background: There's 2 seasons registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists a season registered by "user1"
      | year | num GP | num scuderias | world champion   |
      | 2010 | 19     | 12            | Sebastian Vettel |
    And Exists a season registered by "user2"
      | year | num GP | num scuderias | world champion     |
      | 2001 | 17     | 11            | Michael Schumacher |

  Scenario: View details about an owned season
    Given I login as a user "user1" with password "password1"
    When I view the details of season "2010"
    Then I'm viewing season details including
      | year | num GP | num scuderias | world champion   |
      | 2010 | 19     | 12            | Sebastian Vettel |
    And there's "edit" link available


  Scenario: View details about other user season
    Given I login as a user "user1" with password "password1"
    When I view the details of season "2001"
    Then I'm viewing season details including
      | year | num GP | num scuderias | world champion     |
      | 2001 | 17     | 11            | Michael Schumacher |
    And there's no "edit" link available