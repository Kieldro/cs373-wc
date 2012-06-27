import datetime
from google.appengine.ext import db
from google.appengine.api import users


class Crisis(db.Model):
	'''
	A model class describes a kind of entity.
	'''
	# entity properties
	name = db.StringProperty(required=True)
	kind = db.StringProperty(required=True, choices=set(["executive", "manager", "producer"]))
	date = db.DateProperty()
	new_hire_training_completed = db.BooleanProperty(indexed=False)
	account = db.UserProperty()


# create an entity
e = Crisis(name="Fukushima",
			role="nulcear",
			account=users.get_current_user() )

e.date = datetime.datetime.now().date()

# store in the datastore
e.put()

training_registration_list = [users.User("Alfred.Smith@example.com"),
								users.User("jharrison@example.com"),
								users.User("budnelson@example.com")]
# GQL query to the datastore
employees_trained = db.GqlQuery("SELECT * FROM Crisis WHERE account IN :1",
								training_registration_list)

for e in employees_trained:
	e.new_hire_training_completed = True
	db.put(e)