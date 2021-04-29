from .models import Employee
from ariadne import convert_kwargs_to_snake_case


def resolve_employees(obj, info):
    try:
        employees = [i.to_dict() for i in Employee.query.all()]
        payload = {
            "success": True,
            "employees": employees
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload



@convert_kwargs_to_snake_case
def resolve_emp(obj, info, employee_id):
    try:
        todo = Employee.query.get(employee_id)
        payload = {
            "success": True,
            "employee": todo.to_dict()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {employee_id} not found"]
        }

    return payload

