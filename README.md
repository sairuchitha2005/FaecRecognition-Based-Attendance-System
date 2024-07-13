# FaecRecognition-Based-Attendance-System
Introducing the state-of-the-art solution for safe and effective attendance tracking: the FaceRecognition Attendance System. This solution makes the attendance process more efficient and accurate by using cutting-edge facial recognition technology. Written in Python, HTML, and CSS, this Django application is an attendance system that uses facial recognition.


Features :
There will be two different pages in our website 

1.It is open to existing students and the faculty 
    --> After filling all the required details and uploading group photograph,attendance file is generated.
    --> They will be directed to webpage,where they can download the attendance file, once the files have been uploaded and the attendance marking has been completed through backend. 

2.It is restricted to faculty
    --> It is introduced for justifying newly registered students.
    --> It is managed by faculty to add details and uploading individual images.
    --> These uploaded images in the form of encodings are directed to pickle file, which can be further used for marking attendance. 


Files and Directories :

   attendance.csv   --> Attendance file in csv format
   index.html       --> Home Page (for uploading group photograph)
   login.html       --> Login Page (for Adding details of new students)
   output.html      --> Download Page (for downloading attendance file)
   pickle.pkl       --> File used for storing encodings of individual student
   admin.py         --> Contains some models
   apps.py          --> Contains some apps from Django
   forms.py         --> Contains some forms from Django
   models.py        --> Models are created here
   urls.py          --> File used for handling URLs
   views.py         --> File containing all application views
   asgi.py`         --> Gives ASGI config for Face Recognition Project
   settings.py      --> Contains Settings for Face Recognition Project
   wsgi.py          --> Gives WSGI config for Face Recognition Project
   imgs             --> Dataset in image format
   media            --> Stored dataset of images
   db.sqlite3       --> Database for storing data
   manage.py        --> Used for deploying, debugging, or running our website
   attendance.ipynb --> Was initially used to generate pickle file, before making the website



To use the Project :


• Install Python 3.9 manually by going to official website

• Install the necessary librries to use the project

• To access the folder, open a new terminal and use the command `cd Face_recognition.

• To create and apply migrations, run the programs `py manage.py makemigrations` and `py manage.py migrate' in the project directory.

• To start the web server, type `py manage.py runserver`.

• Then open the server, you will find a page to upload a group image.

• You can upload a/many group images and you will get a single csv file with the marked attendance of the students present in the image.

• If you want to add a student of a particular department, you can click the add new registration button and give a photo of yours

# Team Members

• B Rithvik

• K Sai Ruchita
