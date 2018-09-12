HLD
1) simple workflow system
2) s3 storage
3) consistent hashing use and application
4) paxos algo
5) youtube
6) twitter trending
7) recommendation engine
8) logger aggregated system


LLD
1) bookmyshow
2) parking slot
3) traffic light signal (v)
4) twitter trending
5) snake and ladder
6) online game system
7) uber backend system
8) design logger (atm machine, employee heirarchy transaction system)
9) elevator system
10) soduku game
11) push notification
12) deck of cards 


connection pool 
lru cache

logger - info, warn, debug, error 
usecase: 

Class A:
	log.info("Hello")
	log.warn("Aditya")
	log.debug("Shishir")
	log.error("All")

chain of responsibility
rmq
segement tree
topological sort

http://blog.gainlo.co/index.php/2016/05/24/design-a-recommendation-system/
https://www.tutorialspoint.com/design_pattern/chain_of_responsibility_pattern.htm
https://www.quora.com/How-would-you-design-a-cloud-storage-service-like-Amazons-S3

https://www.quora.com/How-do-I-design-a-cross-road-traffic-light-system-in-oops
Design a school with rooms, students, instructors, grades in object oriented way
https://www.quora.com/What-is-Amazon-Simple-Workflow-SWF-used-for
https://www.quora.com/What-are-some-alternatives-to-Amazon-Simple-Workflow


solve -> https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/


operational transformation -> understand deeply


feed publish 
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

Stock Ticker
	-> pub sub model
	-> Publish-subscribe messaging systems can support use cases in which multiple consumers receive each message and/or that messages are received in order by each consumer. For example, a stock ticker service can be used by a large number of people and applications, all of whom want to receive all messages (e.g. prices at which stock trades occur) on their topics of choice


first attempt last three tabs
https://stackoverflow.com/questions/493276/modelling-an-elevator-using-object-oriented-analysis-and-design
https://inst.eecs.berkeley.edu/~cs162/sp07/Nachos/chess.shtml
https://www.youtube.com/watch?v=fJW65Wo7IHI

notifications systems
recommendation systems
collaberative editor  operational transform
type ahead
url shortner
