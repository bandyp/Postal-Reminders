# Postal Reminders
Last year alone over 2500 postal workers suffered from dog bites. That, and other hazards are avoidable 
with the right process in place.

Currently, if there is a hazard on the route (loose dog or animal attacking on delivery) the PW must 
fill out a hazard card, this is then used to enter into a route reminder folder which is then read by any new PW to that route. 
A yellow sticker is placed on the route and a warning is written on post going to that address.

This process is difficult and timely. In reality it is haphazard at best as it requires the PW to fill out a 
special card, which they might not have on them or have the time to do. They might remember the reminder themselves in future deliveries, 
but this information may not passed on. 

Also, a PW with a regular route knows the best houses to deliver parcels when the right address is not home. 
They also know the many requests that customers they see on their route might have. 

What happens on their day off or if a new posty takes over their area? All that information
is lost. So here is a simple app to help log all the hazards, access issues and customer requests 
to help maintain consistency and minimise the risk to the postal worker.

## UX
This needed to be very simple and quick to use, otherwise it would not be utilised. All postal workers 
carry a PDA to help log parcel deliveries. They also track where the posty is through GPS positioning. This 
guarantees the post made it to its destination. This app is designed to work on the PDA. This means 
that no extra equipment is required to the already overloaded postal worker.

It is designed to be clear and as few button presses as possible. The Posty simply makes a quick log of the 
reminder as they walk between houses and can then be edited when they get back the van. It is vital 
to make the initial log just after the incident so that the postal worker does not forget.

The main screen then shows the basic information that is needed to remind the Postal worker 
the next time they are in the area. A search bar helps narrow the field.

The app is designed to be on a mobile size screen similar to the PDA. It can also be easily viewed 
by a manager back in the office on a laptop. Hense, it is fully responsive on all size screens.

The colours chosen are those of Royal Mail.

## Users

The predominent user is the Postman or women, especially those new to the route. Also, experienced 
Posties can edit the information and add new reminders. The Managers can also check to see
if adequate reporting of hazzards, access issues and customer requests are being logged.

### User Stories
* A new Postal worker is doing a route for the first time. At a glance they can see the potential hazards in the area. Particularly dogs who lie in wait to bite the fingers of the Posty as they deliver throuigh the door.
* A Postal worker is delivering to a house with new tenants. As they deliver the tenent asks them to put parcels behind the bin if they are out. The Posty logs this on their PDA.
* A manager checks through the database and sees alot of conmplaints about a loose dog in the area. He can inform the council about the possible homeless dog.
* A Postal worker sees that the elderly resident who they have delivered to every day for years, is now not answering for their deliveries. Prompting a call to local health workers.

## Features
Each main heading brings you to a form with mainly select options. This allows the user to quickly enter information.
They can enter in more comments if needed when they get back to the van where they are out of the elements and not carrying a heavy bag.

There is a condensed table which shows the basic information - Address, reminder and comments. One extra click
brings them to the full table, where they can delete or edit. 

A stylish button in the bottom corner (nearest the thumb, as the PDA is usually carried in the right hand) allows 
the user to log information via a form.

In future, I'd like to incorporate the GPS on the PDA to alert a Postal Worker when they were approaching an address with a reminder.

Also, I would like to use the Royal Mail database for all routes, not just one. So that it could be used across the country.

As the friendly local PW is the eyes and ears of any cummunity, this app could be extended to check in on the elderly or those with disabilities. There could also be an incentive introduced for those PW's who use the app the most.

## Technology Used
* HTML - for the structure of the content of the page
* Materialize - the framwork used to deliver the style and responsiveness
* CSS3 - for making small adjustments to the materialize framework
* Javascript - to initialise some components on the Materialize framework
* Balsamiq - for the wireframe
* Git - for version control
* GitHub - to host the repository
* GitHup Pages - Website hosting.
* Heroku
* MondoDB
* Flask-Pymongo
* Bson
* Python

## Testing

### Manual Tests
I tested myself to ensure the moving from one page to another was seemless and that information
was correctly logged to MondoDB.
I also gave it to some Postal workers for valualble input on the main hazards

### Automated Tests
* Chrome Developer Tools - to ensure all screen sizes responded correctly
* W3C HTML & CSS Validation - used to test HTML and CSS
* JSHint - used to test Javascript

## Deployment
* 

## Credits
