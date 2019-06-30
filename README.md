# CDU-Course-Support-System

This is website has the following two modes:
1. Student Mode: In this mode, students can make their own study plan for the commencing semester. 
2. Lecturer Mode: In this mode, lecturers can upload the student progress report to visualize the student's progress while suggesting student regarding the units to be taken.


### Features offered by this website:
#### This website eases the task of making a study plan with the following features:
1. Information of all the pre-requisite units required for a particular unit.
2. Consideration of the credit point allowed for a semester while creating a study plan.
3. Study plan available as the downloadable pdf.
#### This website is useful for lecturers with the following features:
1. Easy access to the database for an authenticated course-coordinator. 
2. Easy data recording about pre-requisite information for the course-coordinator.

## Student Mode
On the very first page, the student needs to select the course code(in which they are studying), field(their major), semester(for which they want to make a study plan), year(in which the semester is being taken). All this information can be selected with the following interface.
![create_study_plan_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Student%20Mode%20Screenshots/Create_Study_Plan_page.png)

After entering all the required information you get a list of offered units.
![unit_list_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Student%20Mode%20Screenshots/List_of_Units.png)

You can filter units to narrow down the unit offered.
![flitered_unit_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Student%20Mode%20Screenshots/Filtered_Unit.png)

A pop-up will be generated when you check the radio button to select the unit. This pop-up will give you information regarding the pre-requisite required. This radio button will be checked only if you click on "Okay" button otherwise not.
![pre-requisite_pop_up_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Student%20Mode%20Screenshots/Pre-Requisite_info_pop_up.png)

All the units with no pre-requisite will be shown in green color. Whereas the units with pre-requisite will be shown with red color. 
![selected_unit_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Student%20Mode%20Screenshots/Units_in_red_green_color.png)

Final study plan will give the information shwon on the figure below. 
![final_study_plan_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Student%20Mode%20Screenshots/Final_Study_Plan.png)

This study plan can be printed after clicking on the "Export Study Plan button"

## Lecturer Mode
### Login Page
![login_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Lecturer%20Mode%20Screenshots/Login_Page.png)

After login, they can upload the "Student Progress Report" to visualize the student progress while suggesting the allowed units to be taken in student mode.
![Upload_Report_Page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Lecturer%20Mode%20Screenshots/Upload_Student_Progress_Report_Page.png)

### Logout Page
![logout_page](https://github.com/Neetu111/CDU-Course-Support-System/blob/master/Lecturer%20Mode%20Screenshots/After_Logout.png)
Lecturers who are authorized to update the database (Course-Coordinator) can access the database with the following path:
Account<-Hello, "Lecturer_Name"
