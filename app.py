from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import db,credentials,storage
app = Flask(__name__,template_folder="template",static_url_path="/static")

creds = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(creds,{"databaseURL":"https://student-database-c8e65-default-rtdb.asia-southeast1.firebasedatabase.app/",
                                     "storageBucket":"student-database-c8e65.appspot.com"})

ref = db.reference("/data")
second = db.reference("/data2")
third = db.reference("/data3")
fourth = db.reference("/data4")
bucket = storage.bucket()

@app.route('/')
def index():
    return render_template('index.html',students=None)

@app.route('/add_student', methods=['POST'])
def add_student():
    form_data = {
        "email": request.form.get("email"),
        "hsc_register_number": request.form.get("hsc_register_number"),
        "subjects_studied": request.form.get("subjects_studied"),
        "college_register_number": request.form.get("college_register_number"),
        "name": request.form.get("name"),
        "personal_email": request.form.get("personal_email"),
        "programme": request.form.get("programme"),
        "date_of_birth": request.form.get("date_of_birth"),
        "gender": request.form.get("gender"),
        "aadhar_card": request.form.get("aadhar_card"),
        "nationality": request.form.get("nationality"),
        "religion": request.form.get("religion"),
        "community": request.form.get("community"),
        "caste": request.form.get("caste"),
        "blood_group": request.form.get("blood_group"),
        "languages_known": request.form.get("languages_known"),
        "allergic_problem": request.form.get("allergic_problem"),
        "mother_tongue": request.form.get("mother_tongue"),
        "father_name": request.form.get("father_name"),
        "father_occupation": request.form.get("father_occupation"),
        "father_department": request.form.get("father_department"),
        "father_designation": request.form.get("father_designation"),
        "father_organization": request.form.get("father_organization"),
        "mother_name": request.form.get("mother_name"),
        "mother_mobile": request.form.get("mother_mobile"),
        "mother_occupation": request.form.get("mother_occupation"),
        "mother_department": request.form.get("mother_department"),
        "mother_designation": request.form.get("mother_designation"),
        "mother_organization_details": request.form.get("mother_organization_details"),
        "family_income": request.form.get("family_income"),
        "local_guardian_name": request.form.get("local_guardian_name"),
        "local_guardian_relationship": request.form.get("local_guardian_relationship"),
        "guardian_mobile": request.form.get("guardian_mobile"),
        "alternate_mobile": request.form.get("alternate_mobile"),
        "admission_quota": request.form.get("admission_quota"),
        "first_graduate": request.form.get("first_graduate"),
        "nst_scholarship": request.form.get("nst_scholarship"),
        "single_parent_scholarship": request.form.get("single_parent_scholarship"),
        "sports_scholarship": request.form.get("sports_scholarship"),
        "merit_scholarship": request.form.get("merit_scholarship"),
         "merit_scholarship_10th": request.form.get("merit_scholarship_10th"),
        "cm_scholarship": request.form.get("cm_scholarship"),
        "other_scholarship_details": request.form.get("other_scholarship_details"),
        "physically_challenged": request.form.get("physically_challenged"),
        "number_of_siblings": request.form.get("number_of_siblings"),
        "siblings_position": request.form.get("siblings_position"),
        "siblings_working_position": request.form.get("siblings_working_position"),
        "door_number": request.form.get("door_number"),
        "street_name": request.form.get("street_name"),
        "village_town": request.form.get("village_town"),
        "district_taluk": request.form.get("district_taluk"),
        "pincode": request.form.get("pincode"),
        "state": request.form.get("state"),
        "same_address": request.form.get("same_address"),
         "10th_school_name": request.form.get("10th_school_name"),
        "10th_school_type": request.form.get("10th_school_type"),
        "10th_board_of_study": request.form.get("10th_board_of_study"),
        "10th_medium_of_study": request.form.get("10th_medium_of_study"),
        "10th_total_mark": request.form.get("10th_total_mark"),
        "10th_school_address": request.form.get("10th_school_address"),
        "10th_school_district": request.form.get("10th_school_district"),
        "10th_year_of_pass": request.form.get("10th_year_of_pass"),
        "12th_marks": request.form.get("12th_marks"),
        "12th_percentage": request.form.get("12th_percentage"),
        "12th_school_name": request.form.get("12th_school_name"),
        "12th_school_type": request.form.get("12th_school_type"),
        "12th_board_of_study": request.form.get("12th_board_of_study"),
        "12th_medium_of_study": request.form.get("12th_medium_of_study"),
        "12th_school_address": request.form.get("12th_school_address"),
        "12th_school_district": request.form.get("12th_school_district"),
        "12th_year_of_pass": request.form.get("12th_year_of_pass"),
        "12th_mathematics_mark": request.form.get("12th_mathematics_mark"),
        "12th_physics_mark": request.form.get("12th_physics_mark"),
        "12th_chemistry_mark": request.form.get("12th_chemistry_mark"),
        "12th_tnea_cut_off": request.form.get("12th_tnea_cut_off"),
        "Academic_gap": request.form.get("academic_gap"),
         "achievements": request.form.get("achievements"),
        "hostel_days_scholar": request.form.get("hostel_days_scholar"),
        "hostel_room_number": request.form.get("hostel_room_number"),
        "mode_of_travel": request.form.get("mode_of_travel"),
        "aspiration": request.form.get("aspiration"),
        "vaccination_completed": request.form.get("vaccination_completed"),
        "vaccination_dose1_date": request.form.get("vaccination_dose1_date"),
        "vaccination_dose2_date": request.form.get("vaccination_dose2_date"),
        "strength": request.form.get("strength"),
        "weakness": request.form.get("weakness"),
        "hobbies": request.form.get("hobbies"),
        "has_bank_account": request.form.get("has_bank_account"),
        "bank_account_number": request.form.get("bank_account_number"),
        "account_holder_name": request.form.get("account_holder_name"),
        "bank_name": request.form.get("bank_name"),
        "branch_name": request.form.get("branch_name"),
        "ifsc_code": request.form.get("ifsc_code"),
        "has_net_banking": request.form.get("has_net_banking"),
        "has_smartphone": request.form.get("has_smartphone"),
        "has_laptop": request.form.get("has_laptop"),
        "whatsapp_number": request.form.get("whatsapp_number"),
        "facebook_id": request.form.get("facebook_id"),
        "instagram_id": request.form.get("instagram_id"),
        "linkedin_id": request.form.get("linkedin_id"),
        "twitter_id": request.form.get("twitter_id"),
        "passport_number": request.form.get("passport_number"),
        "pan_card_number": request.form.get("pan_card_number"),
        "driving_license_number": request.form.get("driving_license_number"),
        "visited_nec_before": request.form.get("visited_nec_before"),
        "reasons_for_engineering_1": request.form.get("reasons_for_engineering_1"),
        "reasons_for_engineering_2": request.form.get("reasons_for_engineering_2"),
        "reasons_for_engineering_3": request.form.get("reasons_for_engineering_3"),
        "reasons_for_nec_1": request.form.get("reasons_for_nec_1"),
        "reasons_for_nec_2": request.form.get("reasons_for_nec_2"),
        "reasons_for_nec_3": request.form.get("reasons_for_nec_3"),
        "expectations_from_nec_1": request.form.get("expectations_from_nec_1"),
        "expectations_from_nec_2": request.form.get("expectations_from_nec_2"),
        "expectations_from_nec_3": request.form.get("expectations_from_nec_3"),
        "skills_to_gain_1": request.form.get("skills_to_gain_1"),
        "skills_to_gain_2": request.form.get("skills_to_gain_2"),
        "skills_to_gain_3": request.form.get("skills_to_gain_3"),
        "preferred_communication_parent_student": request.form.get("preferred_communication_parent_student"),
        "preferred_communication_student": request.form.get("preferred_communication_student"),
        "preferred_topics_of_discussion": request.form.get("preferred_topics_of_discussion"),
        "satisfaction_with_enrollment_easiness": request.form.get("satisfaction_with_enrollment_easiness"),
        "usefulness_of_provided_information": request.form.get("usefulness_of_provided_information")
    }
    ref.push(form_data)
    #second.push({"game":"Test"})
    return redirect("/")

@app.route('/student')
def student():
    students = ref.get()
    return render_template('index3.html', students=students)

@app.route('/search_student', methods=['POST'])
def search_student():
    search = request.form.get("search")
    student = ref.order_by_child("name").equal_to(search).get()
    if student=={}:
        return render_template("index3.html",students=None)
    return render_template("index3.html",students=student)
    
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf' in request.files:
        pdf_file = request.files['pdf']
        if pdf_file.filename != '':
            
            blob = bucket.blob(pdf_file.filename)
            blob.upload_from_file(pdf_file.stream, content_type=pdf_file.content_type)

           
            download_url = blob.public_url
            print(download_url)

            
            return f'File uploaded successfully! Download URL: {download_url}'
    return 'No file selected or invalid file format!'

if __name__ == "__main__":
    app.run(debug=True,)
