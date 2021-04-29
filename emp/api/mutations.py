from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Employee


@convert_kwargs_to_snake_case
def resolve_create_employee(obj, info, name, department, joined_Date):
    try:
        print("resolve_create_employee")
        joined_Date = datetime.strptime(joined_Date, '%d-%m-%Y').date()
        employee = Employee(name=name, department=department, joined_Date=joined_Date)
        db.session.add(employee)
        db.session.commit()
        payload = {
            "success": True,
            "employee": employee.to_dict()
        }

    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload



