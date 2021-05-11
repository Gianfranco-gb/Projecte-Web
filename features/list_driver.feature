Feature: List driver
  In order to keep myself up to date about registered drivers,
  As a user,
  I want to list the last 2 registered drivers.

  Background: There are 3 registered drivers by the same user
    Given Exists a user "user" with password "password"
    And Exists driver registered by "user"
      | name            | age | nationality | scuderia        | height | weight |
      | Fernando Alonso | 39  | Spain       | Alpine          | 1.71   | 68     |
      | Lance Stroll    | 22  | Canada      | Aston Martin    | 1.82   | 70     |
      | George Russell  | 23  | UK          | Williams        | 1.85   | 70     |

  Scenario: List the last 2 drivers
    When I list drivers
    Then I'm viewing a list containing last 2 drivers
      | name            |
      | George Russell  |
      | Lance Stroll    |
    And The list contains 2 drivers


  Scenario: List the last 2 drivers
    Given Exist driver registered by "user"
      | name            | age | nationality  | scuderia        | height | weight |
      | Charles Leclerc | 23  | Monaco       | Ferrari         | 1.80   | 70     |
    When I list drivers
    Then I'm viewing a list containing last 2 drivers
      | name            |
      | Charles Leclerc |
      | George Russell  |
    And The list contains 2 drivers