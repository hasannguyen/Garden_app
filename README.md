# Garden_app
## Description
My garden app will allow a user to add vegetables or fruits to a list that tracks what they would want to plant.

## Apis
- Trefle API https://docs.trefle.io/
- Quote API (many different options)
  -   Zen Quotes (Will probably use this one since they have a quote of the day) https://zenquotes.io/ 
  -   Forismatic https://forismatic.com/en/api/
  -   Inspiration https://api.goprogram.ai/inspiration/docs/

## Layout
1. Homepage

The homepage will display a random plant and image of it from the Trefle api, along with a quote of the day from a Quote api. It will also have options to sign up or sign in.

2. Plant tracker Page

Once a user logs in they'll be redirected to their plant tracker and it'll display all they plants they've add their list. A user would also be able to delete plants off their list if they want. If there's none, it'll suggest the option for the user to check out the plant list page

3. Plant list Page

Add some static info on difference between a fruit and vegetable and then separate into two different categories: Fruits and Vegetables

 4. Fruits or Vegetables page

Each page would use the Trefle API to filter if it's a fruit or vegetable and then return a list of plants that fit that category and a pictures of every plant. When a user clicks on that specific plant they will then have an option of adding it to their plant tracker list.

-Side note the Trefle Api has a limit of 120 request per minute, so might have to manually filter the fruits and veggies to the most commons one to not exceed rate limit

## Stretch
-Have a user set what season they're in for and possibly filter

-Implementing the the Weather API https://openweathermap.org/api

When Users sign up, they can set the city they live in. Then in the navbar add a check today's weather page which would display the current day's weather using user's city as query for the weather API
