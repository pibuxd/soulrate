from flask_login import current_user, login_required
from src.models import User

from .. import db


def change_rating(name:str, add:int) -> bool:
  '''
  Change the User's rating
  :param name: is name of the user
  :param add: is a value of added or subtracted rating
  '''
  user = User.query.filter_by(name=name).first()
  
  _upvoted = str(user.upvoted)
  _downvoted = str(user.downvoted)

  downvoted = [*map(int, _downvoted.split())] # split string to list of ints
  upvoted = [*map(int, _upvoted.split())]
  
  _id = current_user.id
  to_remove = 0
  
  if add > 0:
    for ID in upvoted:
      if ID == _id:
        return False
      
    for ID in downvoted:
      if ID == _id:
        to_remove = int(_id)
        add *= 2
  else:
    for ID in upvoted:
      if ID == _id:
        to_remove = int(_id)
        add *= 2
      
    for ID in downvoted:
      if ID == _id:
        return False
  
  user.rating += add
  
  if to_remove:
    if add > 0:
      upvoted = change_string(upvoted, _id)
      downvoted = change_string(downvoted, 0, to_remove)
    else:
      downvoted = change_string(downvoted, _id)
      upvoted = change_string(upvoted, 0, to_remove)
  else:
    if add > 0:
      upvoted = change_string(upvoted, _id)
      downvoted = change_string(downvoted)
    else:
      downvoted = change_string(downvoted, _id)
      upvoted = change_string(upvoted)
    
  user.upvoted = str(upvoted)
  user.downvoted = str(downvoted)
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
