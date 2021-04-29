from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import resolve_employees,resolve_emp
from api.mutations import resolve_create_employee

query = ObjectType("Query")
print(resolve_employees)
query.set_field("employees", resolve_employees)
query.set_field("employee", resolve_emp)

print(resolve_create_employee)
mutation = ObjectType("Mutation")
mutation.set_field("createEmployee", resolve_create_employee)


type_defs = load_schema_from_path("employee.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    print("data==>",data)
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    print("success==>",success)
    print("result==>",result)
    status_code = 200 if success else 400

    return jsonify(result), status_code

