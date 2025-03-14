import requests


"""
Файл для взаимодействия настольного приложения с апи на сервере
"""

def delete_employee_education_by_name_and_date(name: str, date: str):
    url = f"http://127.0.0.1:8000/api/v1/event?employee={name}&date={date}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        return True
    return False

def add_event_by_employee(event_title: str, employee_name: str, date_since: str, date_until: str):
    url = f"http://127.0.0.1:8000/api/v1/event?event_title={event_title}&employee={employee_name}&date_since={date_since}&date_until={date_until}"
    response = requests.post(url)
    
    if response.status_code == 201:
        return True
    return False

def add_vacation_by_employee(employee_name: str, date_since: str, date_before: str):
    url = f"http://127.0.0.1:8000/api/v1/vacation?employee={employee_name}&date_since={date_since}&date_before={date_before}"
    response = requests.post(url)
    
    if response.status_code == 201:
        return True
    return False

def delete_employee_vacation_by_name_and_date(employee_name: str, date: str):
    url = f"http://127.0.0.1:8000/api/v1/vacation?employee={employee_name}&date={date}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        return True
    return False

def add_skip_by_employee(employee_name: str, date_since: str, date_before: str):
    url = f"http://127.0.0.1:8000/api/v1/skip?employee={employee_name}&date_since={date_since}&date_before={date_before}"
    response = requests.post(url)
    
    if response.status_code == 201:
        return True
    return False

def delete_employee_skip_by_name_and_date(employee_name: str, date: str):
    url = f"http://127.0.0.1:8000/api/v1/skip?employee={employee_name}&date={date}"
    response = requests.delete(url)
    
    if response.status_code == 200:
        return True
    return False


def dismiss_employee_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/employee/dismiss?employee={name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return True
    elif response.status_code == 400:
        return False
    return None

def get_vacations_by_employee_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/vacations/date?employee={name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return []

def get_skip_dates_by_employee_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/skips/date?employee={name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return []

def get_study_date_by_employee_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/events/date?responsible={name}"
    response = requests.get(url)
    
    return response.json()


def get_organizations():
    try:
        url = "http://127.0.0.1:8000/api/v1/organizations"
        response = requests.get(url)

        return response.json()
    except:
        return 0
    

def get_subdivisions():
    try:
        url = "http://127.0.0.1:8000/api/v1/subdivisions"
        response = requests.get(url)

        return response.json()
    except:
        return []
    

def get_sub_sub_divisions():
    try:
        url = "http://127.0.0.1:8000/api/v1/subsubdivisions"
        response = requests.get(url)

        return response.json()
    except:
        return []
    

def get_subdivision_by_id(id: int):

    subdivisions = get_subdivisions()

    for subdivision in subdivisions:
        subdivision_id = subdivision["id"]
        if subdivision_id==id:
            return subdivision
        
    return None


def get_sub_sub_division_by_id(id: int):

    sub_sub_divisions = get_sub_sub_divisions()

    for sub_sub_division in sub_sub_divisions:
        sub_sub_division_id = sub_sub_division["id"]
        if sub_sub_division_id==id:
            return sub_sub_division
        
    return False


def get_sub_division_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/subdivisions/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['id']
    return None


def get_organization_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/organizations/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['id']
    return None


def get_organization_by_id(id: int):
    url = f"http://127.0.0.1:8000/api/v1/organization?pk={id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None


def get_sub_sub_division_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/subsubdivisions/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['id']
    return None
    

def get_employees_by_department(department: str) -> list[dict]:
    url = f"http://127.0.0.1:8000/api/v1/employees/search_department/{department}"
    response = requests.get(url=url)
    return response.json()


def get_employees():
    url = "http://127.0.0.1:8000/api/v1/employees"
    response = requests.get(url)

    try:
        users = []
        for user in response.json():
            users.append(user["username"])
        return users
    except:
        return None


def get_employee_id_by_name(name: str):
    global employee
    url = f"http://127.0.0.1:8000/api/v1/employees/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["id"]
    else:
        return None

def get_employee_by_name(name: str):
    global employee
    url = f"http://127.0.0.1:8000/api/v1/employees/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_cabinets():
    url = "http://127.0.0.1:8000/api/v1/cabinets"
    response = requests.get(url)

    try:
        cabinets = []
        for cabinet in response.json():
            cabinets.append(cabinet["title"])

        return cabinets

    except:
        return None

def get_cabinet_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/cabinets/{name}"
    response = requests.get(url)

    return response.json()['id']


def get_job_titles():
    url = "http://127.0.0.1:8000/api/v1/jobtitles"
    response = requests.get(url)

    try:
        job_titles = []
        for job_title in response.json():
            job_titles.append(job_title["title"])

        return job_titles
    except:
        return None


def get_job_title_by_name(name: str):
    url = f"http://127.0.0.1:8000/api/v1/jobtitles/search_name/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["id"]
    return None