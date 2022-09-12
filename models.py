from typing import Text
from database import Base
from sqlalchemy import String,Boolean,Integer,Column
 #dbhsugfjndslkfhdisuhfc

class Item(Base):
    __tablename__='items'
    firstname=Column(Integer,primary_key=True)
    lastname=Column(String(255),nullable=False,unique=True)
    contact=Column(Text)
    drivers_license_number=Column(Integer,nullable=False)
    region=Column(Boolean,default=False)
    
    
    def _ref_(self):
        return f"<Item name={self.name} price={self.price}>"
    
