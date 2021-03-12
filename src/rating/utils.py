from src.models import User

from .. import db


def change_rating(name:str, add:int, token:str) -> bool:
  '''
  Change the User's rating
  :param name: is name of the user
  :param add: is a value of added or subtracted rating
  '''
  user = User.query.filter_by(name=name).first()
  current = User.query.filter_by(token=token).first()
  
  _uprated = str(user.uprated)
  _downrated = str(user.downrated)

  downrated = [*map(int, _downrated.split())] # split string to list of ints
  uprated = [*map(int, _uprated.split())]
  
  _id = current.id
  to_remove = 0
  
  if add > 0:
    for ID in uprated:
      if ID == _id:
        return False
      
    for ID in downrated:
      if ID == _id:
        to_remove = int(_id)
        add *= 2
  else:
    for ID in uprated:
      if ID == _id:
        to_remove = int(_id)
        add *= 2
      
    for ID in downrated:
      if ID == _id:
        return False
  
  user.rating += add
  
  if to_remove:
    if add > 0:
      uprated = change_string(uprated, _id)
      downrated = change_string(downrated, 0, to_remove)
    else:
      downrated = change_string(downrated, _id)
      uprated = change_string(uprated, 0, to_remove)
  else:
    if add > 0:
      uprated = change_string(uprated, _id)
      downrated = change_string(downrated)
    else:
      downrated = change_string(downrated, _id)
      uprated = change_string(uprated)
    
  user.uprated = str(uprated)
  user.downrated = str(downrated)
  db.session.commit()
  
  return True


def change_string(old:list, to_add=0, to_remove=0) -> str:
  '''
  Add int and remove int from list of ints, then convert list of ints to string
  :param old: list of ints to convert
  :param add: int to add to list
  :param remove: int to remove from list 
  '''
  new = ""
  
  for _id in old:
    if int(_id) != to_remove:
      new += str(_id) + " "
  
  if to_add:
    new += str(to_add)
  
  return new
