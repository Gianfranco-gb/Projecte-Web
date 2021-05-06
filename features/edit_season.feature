Feature: Edit season
  In order to keep updated my previous registers about seasons,
  As a user,
  I want to edit a season register I created.

  Background: There are registered 2 users but only 1 season registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists season registered by "user1"
      | year | num GP | num scuderias | world champion |
      | 2008 | 18     | 11            | Lewis Hamilton |
    And Exists season registered by "user1"


  Scenario: Edit owned season (have to edit all fields)
    Given I login as a user "user1" with password "password1"
    When  I view the details for season "2008"
    And I edit current season
      | year | num GP | num scuderias | world champion |
      | 2008 | 19     | 11            | Lewis Hamilton |
    Then I'm viewing the details page for season "2008" by "user1"
      | year | num GP | num scuderias | world champion |
      | 2008 | 19     | 11            | Lewis Hamilton |
    And there's 1 season

  Scenario: Try to edit not owned season
    Given I login as a user "user2" with password "password2"
    When  I view the details for season "2008"
    Then ther's no "edit" link available