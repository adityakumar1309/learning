# Collaberative Filtering (CF)
    - user-based collaborative filtering
    - item-based collaborative filtering
    
In a nutshell, to recommend videos for a user, I can provide videos liked by similar users. 
For instance, if user A and B have watched a bunch of same videos, it’s highly likely that user A will like videos liked by B. 
Of course, there are many ways to define what “similar” means here. 
It could be two users have liked same videos, it could also mean that they share the same location.

The above algorithm is called user-based collaborative filtering. 
Another version is called item-based collaborative filtering, 
which means to recommend videos (items) that are similar to videos a user has watched.

Factors:
Offline Generation
Sensitivity Factors: 
  a) Freshness
  b) Location

User Choice data can be reprenseted in column vector (may be using casandra which is wide column)
