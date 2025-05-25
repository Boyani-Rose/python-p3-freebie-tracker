#!/usr/bin/env python3

# Script goes here!

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


company1= Company(name = "R&B Ltd.", founding_year = 2011) 
company2= Company(name = "Momanyi B&G Ltd.", founding_year = 1999) 
company3= Company(name = "Kiango Kenya Ltd.", founding_year = 1989) 
company4= Company(name = "Boyani Ltd.", founding_year = 2013) 


dev1= Dev(name= "Rose B. Momanyi")
dev2= Dev(name= "Vincent A. Asumari")
dev3= Dev(name= "Josiah O. Ombasa")
dev4= Dev(name= "Diana B. Ondieki")

session.add_all([company1, company2, company3, company4, dev1, dev2, dev3, dev4])
session.commit()

# Give freebies
session.add_all([
    company1.give_freebie(dev1, "Laptop", 1),
    company1.give_freebie(dev2, "Stylus", 2),
    company2.give_freebie(dev1, "iPad", 3),
    company2.give_freebie(dev2, "Headphones", 4),
    company3.give_freebie(dev3, "Phone", 5),
    company4.give_freebie(dev4, "Tablet", 6)
])
session.commit()

# Print all freebies
for freebie in session.query(Freebie).all():
  print(freebie.print_details())
