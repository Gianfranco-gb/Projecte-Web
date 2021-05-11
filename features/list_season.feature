Feature: List season
  In order to keep myself up to date about registered seasons,
  As a user,
  I want to list the last 2 registered seasons.

  Background: There are 3 registered seasons by the same user
    Given Exists a user "user" with password "password"
    And Exists seasons registered by this "user"
      | year    | num GP  | num scuderias | world champion   |
      | 2010    | 19      | 12            | Sebastian Vettel |
      | 2015    | 19      | 10            | Lewis Hamilton   |
      | 2005    | 19      | 10            | Fernando Alonso  |
  Scenario: List the last 2 drivers
    When I list seasons
    Then I'm viewing a list containing last 2 seasons
      | year    |
      | 2005    |
      | 2015    |
    And The list contains 2 season


  Scenario: List the last 2 seasons
    Given Exist a season registered by "user"
      | year    | num GP  | num scuderias | world champion   |
      | 2009    | 17      | 10            | Jenson Button    |
    When I list seasons
    Then I'm viewing a list containing last 2 seasons
      | year    |
      | 2009    |
      | 2005    |

    And The list contains 2 seasons