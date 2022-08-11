from models import Pet, db
from app import app

db.drop_all()
db.create_all()

# if table isn't empty, empty it
Pet.query.delete()

# add pets
Buddy = Pet(name='buddy', species="bulldog", photo_url="https://cdn.wamiz.fr/cdn-cgi/image/format=auto,quality=80,width=400,height=400,fit=cover/animal/breed/pictures/61a8ad46965d5085827792.jpg", age=30, notes="quiet dog", available=True)

Honey = Pet(name='honey', species="duck", photo_url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcore2.staticworld.net%2Fimages%2Farticle%2F2014%2F05%2Fduckduckgo-logo-100266737-large.png&f=1&nofb=1", age=5, notes="duck from duckduckgo", available=True)



db.session.add_all([Buddy,Honey])

db.session.commit()

# db.session.add_all([post1,post2])

# db.session.commit()