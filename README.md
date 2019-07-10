# CDU-Course-Support-System

This is website has the following two modes:
1. Student Mode: In this mode, students can make their own study plan for the commencing semester. 
2. Lecturer Mode: In this mode, lecturers can upload the student progress report to visualize the student's progress while suggesting student regarding the units to be taken.

## Why this project?
No such website exist for CDU to give the instant information of pre-requisite of the selected course. Due to this reason, it was given as the unit project. This website is mainly includes the following courses:
* Associate Degree of Engineering (XENG01 - 2019)
* Bachelor of Engineering Honours (VENG01 - 2019)
* Bachelor of Engineering Science (WENGS1 - 2019)
* Bachelor of Engineering Science/Master of Engineering (HENG01 - 2019)

## Features
#### This website eases the task of making a study plan with the following features:
1. Information of all the pre-requisite units required for a particular unit.
2. Consideration of the credit point allowed for a semester while creating a study plan.
3. Study plan available as the downloadable pdf.
#### This website is useful for lecturers with the following features:
1. Easy access to the database for an authenticated course-coordinator. 
2. Easy data recording about pre-requisite information for the course-coordinator.

## Using
### Server
```
Step 1: Open the terminal
Step 2: Go to the project directory with the following command
cd path_to_project_folder
    Example:  cd Desktop/CDU_course_support_system
Step 3: Start the server with the following command:
    python manage.py runserver
```

### Student Application
```
Step 1: After starting the server go to the address
http://128.0.0.1:8000/student
```
		

### Admin/Lecturer Application
```
Step 1: After starting the server go to the address
http://128.0.0.1:8000/lecturer
```

## Example
#### Instructions to make a Study Plan
```
Step 1: Enter the following field on the first page of the student app
        1. Course Code
        2. Field
        3. Semester
        4. Year
Step 2: Choose the units from the right side of the page
Step 3: Click “yes” on the pop-up for selecting the unit otherwise cancel it and repeat step 2
Step 4: Click “Add Unit” button 
Step 5: Go to either step 2 for adding more units or step 6 to modify the study plan, otherwise go to step 8
Step 6: select unit from the right side of the page 
Step 7: Click “Remove Unit” button to remove it otherwise step 5
Step 8: Click the “Final study plan” button 
Step 9: Click the “Export Study Plan” button to get the pdf
```

#### Instructions to upload Student Progress Report
```
Step 1: Enter the username and password to login
Step 2: Choose a student progress report file to upload
Step 3: After uploading click “Show Student Progress Report” to visualize the report
Step 4: The report should be displayed on the screen
```

## License
[MIT](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/LICENSE)
