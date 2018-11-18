# coding=utf-8


from orm_class import Session,App,engine,Base

try:
 session = Session()
 
 stu_obj = session.query(App).filter(App.name=='alex').first()
 if stu_obj == None:
   obj = App(name='alex',id=2)
   session.add(obj)
   session.commit()
   print('insert record successfully')
 else:
   print(stu_obj)

except Exception as e:
   print(str(e))

finally:
   stu_obj = session.query(App).all()
   print(stu_obj)
   session.close()
