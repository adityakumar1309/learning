# feed publish 
    -> 3 components
        - data model/ feed generation
        - feed ranking . it has two parts (feed agregator, feed ranker)
        - feed publish
        
	-> hybrid of push model(disable fanout for high profiles) and pull model(high profiles activity feed calculated on fly when asked for) . fan out on write vs fan out on load
	
  -> push may have priority like more priority for online/active users
	
  -> push not very good for mobile due to bandwith issue
	
  -> denormalised data 
	
  -> in memory redis . lru for users feed in redis (only generate feed for users who login on regular basis)
	
  -> indexing on (user_id, created_date)
	
  -> Ranking of feed . 
		  Sensitivity factors 
			-> affinity score (close friend's activity will get high score)
			
      -> edge type and edge wt (likes, tag, comment, share etc will have different scores)
			
      -> time decay (more recent will get higher wts)
	
  -> API
		getUserFeed(api_dev_key, user_id, since_id, count, max_id, exclude_replies)

