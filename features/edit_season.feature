Feature: Edit season
  In order to keep updated my previous registers about seasons,
  As a user,
  I want to edit a season register I created.

  Background: There are registered 2 users but only 1 season registered
    Given Exists a user "user1" with password "password1"
    And Exists a user "user2" with password "password2"
    And Exists season registered by "user1"
      | year |num_gp  | num_scuderias | world_champion | scuderia_champion |
      | 2008 | 18     | 11            | Lewis Hamilton | Ferrari           |


  Scenario: Edit owned season
    Given I login as a user "user1" with password "password1"
    When  I edit the season with year "2008"
      | year |num_gp  | num_scuderias | world_champion | scuderia_champion |
      | 2008 | 19     | 11            | Lewis Hamilton | Ferrari           |
    Then I'm viewing the details page for season by "user1"
      | year |num_GP  | num_scuderias | world_champion | scuderia_champion |
      | 2008 | 19     | 11            | Lewis Hamilton | Ferrari           |
    And There is 1 season
