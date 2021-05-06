Feature: Edit stats
  In order to keep updated my previous registers about statistics,
  As a user,
  I want to edit a stats register I created.

  Background: There are registered 2 users but only 1 stat registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists stat registered by "user1"
      | name Driver    | num of championships | num dif teams |
      | Max Verstappen | 0                    | 2             |
    And Exists stat registered by "user1"


  Scenario: Edit owned stat (have to edit all fields)
    Given I login as a user "user1" with password "password1"
    When  I view the details for stat "Max Verstappen"
    And I edit current stat
      | name Driver    | num of championships | num dif teams |
      | Max Verstappen | 1                    | 2             |
    Then I'm viewing the details page for stat "Max Verstappen" by "user1"
      | name Driver    | num of championships | num dif teams |
      | Max Verstappen | 1                    | 2             |
    And there's 1 stat

  Scenario: Try to edit not owned stat
    Given I login as a user "user2" with password "password2"
    When  I view the details for stat "Max Versatppen"
    Then ther's no "edit" link available