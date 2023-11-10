# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse,FileResponse
from .models import Student, ReferenceFace
from django.conf import settings
import pathlib
import face_recognition
import pickle
import csv
import os


def boot(request):
    if request.method == 'POST':
        year = request.POST.get('SelectYear')
        department = request.POST.get('SelectDepartment')
        course = request.POST.get('select_course')
        selected_date = request.POST.get('select_date')
        group_photos = request.FILES.getlist('photo')
        print(course)
        with open(str(f'{course}.pkl'), "rb") as f:
            ref_face_enc = pickle.load(f)

        roll_list = []
        attendance={}
        
        for i in range(220001001,220001083):
            if i==220001030:
                continue
            if i==220001072:
                continue
            roll_list.append(i)
        roll_list.append(220002018)
        roll_list.append(220002029)
        roll_list.append(220002063)
        roll_list.append(220002081)

        for roll_no in roll_list:
            attendance[str(roll_no)]="Absent"

        for pic in request.FILES.getlist('photo'):
            pic_load=face_recognition.load_image_file(pic)
            class_face_enc= face_recognition.face_encodings(pic_load)
            for enc in class_face_enc:
                dist=[]
                for rollno in roll_list:
                    dist.append(face_recognition.face_distance([enc],ref_face_enc[str(rollno)][0]))
                min_dist=min(dist)
                for rollno in roll_list:
                    if face_recognition.face_distance([enc],ref_face_enc[str(rollno)][0])==min_dist:
                        attendance[str(rollno)]="Present"
                        break 

        csv_file_name = "attendance.csv"

        with open(csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            csv_writer.writerow(["Roll No", selected_date])
            for student, is_present in attendance.items():
                csv_writer.writerow([student, is_present])
        return redirect('output', csv_file_name=csv_file_name)
        
    return render(request,'boot.html')

def download(request,csv_file_name):       
        file_path = os.path.join(settings.BASE_DIR, csv_file_name)         
        with open(csv_file_name, mode='r') as csv_file: 
              response = HttpResponse(csv_file.read(), content_type='text/csv')
              response['Content-Disposition'] = f'attachment; filename="attendance.csv"'
              return response
def output(request, csv_file_name):
    return render(request, 'output.html', {'csv_file_name': csv_file_name})

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        year = request.POST.get('year')
        department = request.POST.get('department')
        image = request.FILES['photo']
        image_ = face_recognition.load_image_file(image)
        image_encodings=face_recognition.face_encodings(image_)

        # Create and save the student instance
        student = Student(name=name, roll_no=roll_no, year=year, department=department)
        student.save()

        # Create and save the reference face associated with the student
        reference_face = ReferenceFace(student=student, image=image)
        reference_face.save()

        with open(str('CS 201.pkl'), "rb") as f:
            ref_face_enc = pickle.load(f)
        
        ref_face_enc[str(roll_no)]=image_encodings

        with open(str('CS 201.pkl'),'wb') as f:
            pickle.dump(ref_face_enc,f)

        with open(str('CS 203.pkl'), "rb") as f:
            ref_face_enc = pickle.load(f)
        
        ref_face_enc[str(roll_no)]=image_encodings

        with open(str('CS 203.pkl'),'wb') as f:
            pickle.dump(ref_face_enc,f)

        with open(str('CS 207.pkl'), "rb") as f:
            ref_face_enc = pickle.load(f)
        
        ref_face_enc[str(roll_no)]=image_encodings

        with open(str('CS 207.pkl'),'wb') as f:
            pickle.dump(ref_face_enc,f)

        return HttpResponse("New student added")

    return render(request, 'login.html')
