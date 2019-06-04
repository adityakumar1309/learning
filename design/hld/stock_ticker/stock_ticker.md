# Stock Ticker
	-> websocket connection 
	-> pub sub model
	-> Publish-subscribe messaging systems can support use cases in which multiple consumers receive each message and/or that messages are received in order by each consumer. 
  For example, a stock ticker service can be used by a large number of people and applications, 
  all of whom want to receive all messages (e.g. prices at which stock trades occur) on their topics of choice
  
  
 # Design Stock Ticker System

## 1. Requirements
	Fr:
		- new user should be able to get alerts for a stock
		- user can add new stocks to alerts 
		- user can removed himself from any stock alert
		- new stocks can be added to the system 

	Nfr:
		- system should higly be available
		- consistency can tak a hit 
		- stock rendering should be really fast 

## 2. API
	- add_stock(user_id, stock_id, timzone, frequency)
	- remove_stocks(user_id, stock_id)
	- create_stock(stock_name)

## 3. Data Modelling
	- user
	- stock
	- user_stock_subscription

## 4. Capacity
	Some considerations:
		1M total users, 500K active users, each user is subscribed to 5 stocks, updates are active from 10am-6pm ie 8hrs .. lets says we update every 5sec
		total updates = 500K * 5 * 1/5 each sec = 500K per sec

	- newtwork bandwidth
		- Since 500K per sec updates are happening (ignore new stocks being added and user adding new stocks to minimal bandwidth)
		- each request takes 10kb of data so total of 500K*50kb per sec = 25gb per sec 

	- storage 
		- each user record takes 100kb so user table will take = 1M * 100kb = 100gb 
		- stocks contribution will be negligible 

## 5. HLD
	Some consideration

	- since stock updates needs to be realtime we need to have http long poll or socket connection . Lets stick with socket connection since updates can be sent realy fast due to the fact that we dont need handshake connection each time 
	- storing socket connection object in memory
	- model we going to use will be pub/sub model . Each user will be subsribed to stocks and when stocks get updated we will we publish the updates 
	- we will use queue like kafka to store all incoming updates from stocks and also users in queue as subcribers 
	- each subscription queue will be labelled/named or by stockId 
	- there will retry model (when user does not get stock updates) 
	- sync server which will periodacly sync stock value in db incase (for analytical purpose)
	
