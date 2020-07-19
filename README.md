# flask-blog

## Summary
This site was developed using [Corey Schafer's Flask Series](https://www.youtube.com/watch?v=MwZwr5Tvyxo) on his and then built upon. My goal with the site was to learn more about Flask, SQLAlchemy, and deploying a web app. I am using this site as my personal blog and my intention is for it to be a demo for others to see the functionality.

### Methods Used
* Python
* Flask
* SQLAlchemy
* HTML/CSS

### Notes
* Guest Users: The application will allow you to register, create a login and post. Once you logoff, you data will be purged from the Database. 
* Deployment: This web application is hosted on PythonAnywhere. There is a script that runs once per day to clean the database if a guest user does not log out.  

### Areas for Continued Work
* Auto logout for users
* Tagging posts
* Displaying common tags
* Displaying posts with a certain tag
* UI improvements