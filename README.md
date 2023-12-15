# Human Resource Information System Project
 
 *Project submission for Baruch College's CIS 5800 Course*

 End-to-end web application to schedule, manage tasks, and bridge communication between HR Officers, Managers, and Employees.

 ## How to access
 *Pre-req - Install python, pip, Git*
 1. Clone this repository `git clone link_here`

 2. Enter the HRIS_CIS-5800 directory
    
 3. install packages `pip install -r requirements.txt`

 4. Run `python manage.py runserver`

    *Ensure django and django-widget-tweaks is installed with `pip install django-widget-tweaks` or `pip install django`*

## Credentials 
| Usernames| admin | 001 | 002 | 003 | 004 | 005 | 007 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Passwords | root1234 | testing001 | testing002 | testing003 | testing004 | testing005 | testing007 |
| Roles | Admin | Manager | Employee | Temp Manager | Human Resource Officer | Employee | Employee |

## Role Functionality
*Features not implemented are italicized*

All Users - Access to the calendar, change user info, view list of events, login, create an employee account, submit feedback, *send messages*  

Managers - Can create/edit events(shifts), Promote users, create users with any role, view requests, view every event

Temp-manager - Can create/edit events, view every event

Human Resource Officer - Can create/edit events(meetings), Terminate users, create users with any role, view requests 

Employee - Submit a request, view events directed towards them
