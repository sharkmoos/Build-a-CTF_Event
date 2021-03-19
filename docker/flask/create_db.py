from main import db, uuid, User, Notes
def addUsers(users):
    for x in users:
        db.session.add(x)
    db.session.commit()

def addNotes(notes):
    for x in notes:
        db.session.add(x)
    db.session.commit()

if __name__ == "__main__":
    print("@>Initializing Database for webapp")
    db.create_all()
    print("@>Creating Users")
    admin_uuid=str(uuid.uuid4())
    noah_uuid=str(uuid.uuid4())
    users = [
        User(username='admin', email='admin@sharklabs.local', uuid=admin_uuid, admin_cap=True, password="0d3ae6d144edfb313a9f0d32186d4836791cbfd5603b2d50cf0d9c948e50ce68"),
        User(username="intern", email="intern@canely.com", uuid=admin_uuid, admin_cap=True, password="fb001dfcffd1c899f3297871406242f097aecf1a5342ccf3ebcd116146188e4b")
        ] # JWTW1ns
    print("@>Adding Users")
    addUsers(users)
    print("@>DONE. Database initialized and populated.")
pwd
