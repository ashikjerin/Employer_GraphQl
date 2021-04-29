from main import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    department = db.Column(db.String)
    joined_Date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "department": self.department,
            "name": self.name,
            "joined_Date": str(self.joined_Date.strftime('%d-%m-%Y'))
        }


