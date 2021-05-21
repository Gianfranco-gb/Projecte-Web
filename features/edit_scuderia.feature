Feature: Edit scuderia
  In order to keep updated my previous registers about scuderias,
  As a user,
  I want to edit a scuderia register I created.

  Background: There are registered 2 users but only 1 scuderia registered
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists scuderia registered by "user1"
      | name    | main_color | principalDriver | secondaryDriver | num_championships |
      | Ferrari | Red        | Charles Leclerc | Carlos Sainz    | 16                |


  Scenario: Edit owned scuderia
    Given I login as a user "user1" with password "password1"
    When I edit the scuderia with name "Ferrari"
      | name    | main_color | principalDriver | secondaryDriver | num_championships |
      | Ferrari | Red        | Charles Leclerc | Carlos Sainz    | 17                |
    Then I'm viewing the details page for scuderia by "user1"
      | name    | main_color | principalDriver | secondaryDriver | num_championships |
      | Ferrari | Red        | Charles Leclerc | Carlos Sainz    | 17                |
    And There is 1 scuderia
