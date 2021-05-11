Feature: List driver
  In order to keep myself up to date about registered drivers,
  As a user,
  I want to list the last 2 registered drivers.

  Background: There are 3 registered drivers by the same user
    Given Exists a user "user" with password "password"
    And Exists drivers registered by this "user"
      | name            | age | nationality | scuderia        | height | weight |
      | Fernando Alonso | 39  | Spain       | Alpine          | 1.71 m | 68 kg  |
      | Lance Stroll    | 22  | Canada      | Aston Martin    | 1.82 m | 70 kg  |
      | George Russell  | 23  | UK          | Williams        | 1.85 m | 70kg   |

  Scenario: List the last 2 drivers
    When I list drivers
    Then I'm viewing a list containing last 2 drivers
      | name            |
      | George Russell  |
      | Lance Stroll    |
    And The list contains 2 drivers


  Scenario: List the last 2 drivers
    Given Exist a driver registered by "user"
      | name            | age | nationality  | scuderia        | height | weight |
      | Charles Leclerc | 23  | Monaco       | Ferrari         | 1.80 m | 70 kg  |
    When I list drivers
    Then I'm viewing a list containing last 2 drivers
      | name            |
      | Charles Leclerc |
      | George Russell  |
    And The list contains 2 drivers