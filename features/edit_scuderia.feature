Feature: Edit scuderia
  In order to keep updated my previous registers about scuderias,
  As a user,
  I want to edit a scuderia register I created.

  Background: There are registered 2 users but only 1 scuderia registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists scuderia registered by "user1"
      | name    | main color | principal Driver | secondary Driver | num championships |
      | Ferrari | Red        | Charles Leclerc  | Carlos Sainz     | 16                |
    And Exists scuderia registered by "user1"


  Scenario: Edit owned scuderia (have to edit all fields)
    Given I login as a user "user1" with password "password1"
    When  I view the details for scuderia "Ferrari"
    And I edit current scuderia
      | name    | main color | principal Driver | secondary Driver | num championships |
      | Ferrari | Red        | Charles Leclerc  | Carlos Sainz     | 17                |
    Then I'm viewing the details page for scuderia "Ferrari" by "user1"
      | name    | main color | principal Driver | secondary Driver | num championships |
      | Ferrari | Red        | Charles Leclerc  | Carlos Sainz     | 17                |
    And there's 1 scuderia

  Scenario: Try to edit not owned scuderia
    Given I login as a user "user2" with password "password2"
    When  I view the details for scuderia "Ferrari"
    Then ther's no "edit" link available


  Scenario: Force edit scuderia but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the scuderia with name "Ferrari"
      | name    | main color | principal Driver | secondary Driver | num championships |
      | Ferrari | Red        | Charles Leclerc  | Carlos Sainz     | 17                |
    Then Server responds with page containing "403 Forbidden"