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
        User(username='admin', email='admin@sharklabs.local', uuid=admin_uuid, admin_cap=True, password="0d3ae6d144edfb313a9f0d32186d4836791cbfd5603b2d50cf0d9c948e50ce68"),] # JWTW1ns
    print("@>Adding Users")
    addUsers(users)
    print("@>Creating Notes")
    notes = [
        Notes(owner_uuid=admin_uuid, title="Need to fix config", note="Have to fix this issue where PHP files are being executed :/. This can be a potential security issue for the server. (Update. Fixed"),
        Notes(owner_uuid=admin_uuid, title="Backups are scheduled", note="Finally! Regular backups are necessary. Thank god it's all easy on server."),
        Notes(owner_uuid=admin_uuid, title="SSH Key", note="I stored my ssh key here, for when I need access to the server remotely this webapp is secure enough. \n ")
    ]
    print("@>Adding Notes")
    addNotes(notes)
    print("@>DONE. Database initialized and populated.")
