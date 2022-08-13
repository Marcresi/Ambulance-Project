# Ambulance-Project

##About Project

## Inspiration
This project is inspired by the difficulties faced in booking an Ambulance during an Emergency Situation.

## What it does
Our Web Application allows the user to book an ambulance according to his/her convenience. This Web application **fetches the user location through the user's IP address and displays the nearby hospitals with ambulance facility at hand**.

## How we built it
- The front end is developed using **HTML, CSS and JavaScript.**
- Database is created and connected to **MongoDB Atlas** for accessing our data through the cloud.
- **Folium library** is imported to access  the user location and display it on the map.
- Python Library - **PyMongo** is used for accessing databases in MongoDB Atlas and fetching the information of users and hospitals.
- A function is created to filter the nearby hospital locations and display them as a list as well as on the map.
- Rest API is built with a python framework **Fast API** to execute the above function (mentioned in the point above).
- The user can select a hospital from the list or he/she can also search for his/her preferred hospital.
- On confirming the booking , the user is directed to a confirmation page **displaying the traveler and driver details** along with **the user and hospital location**.

## Challenges we ran into
- Time constraint was one of the major challenges we faced.
- Connecting our front-end components to the map and list components.

## What we learned
- Displaying specified locations on map on a web application
- Using different libraries, APIs and frameworks
- Hosting and managing our database in MongoDB Atlas

