# Garden_app
## Description
My garden app will allow a user to add vegetables or fruits to a list that tracks what they would want to plant.

## Apis
- Flora Codex https://floracodex.com/
  - Original plan was to use Trefle API, unfortunately that API is no longer online. Flora codex is an alternative one to possibly use.

- Quote API (many different options)
  -   Zen Quotes (Will probably use this one since they have a quote of the day) https://zenquotes.io/ 
  -   Forismatic https://forismatic.com/en/api/
  -   Inspiration https://api.goprogram.ai/inspiration/docs/

## Layout
1. Homepage

The homepage will display a random plant and image of it from the Trefle api, along with a quote of the day from a Quote api. It will also have options to sign up or sign in.

2. Plant tracker Page

Once a user logs in they'll be redirected to their plant tracker and it'll display all they plants they've add their list. A user would also be able to delete plants off their list if they want. If there's none, it'll suggest the option for the user to check out the plant list page

3. Search Page

Add some static info on difference between a fruit and vegetable and have a search bar to search a plant with some suggestions of fruits or veggies on the bottom.

3a. The search bar will query the Flora Codex api using the input value and return a list of names and images of related plants. Then there will be an option to add that plant to the plant tracker list.

## Stretch
-Have a user set what season they're in for and possibly filter

-Implementing the the Weather API https://openweathermap.org/api

When Users sign up, they can set the city they live in. Then in the navbar add a check today's weather page which would display the current day's weather using user's city as query for the weather API
