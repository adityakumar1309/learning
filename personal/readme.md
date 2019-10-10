
->Handle millions of data of a client and apply some nlp and data processing and returning them some result

->I have also been invloved in tokenising simple sentences and later transforming those into rules, grammar .

->I have been part of a project where i had to solely design end to end architiecture .
Where clients send there huge data and we need to automate or pipeline the whole process to extract the data, apply some nlp and then pass it through our knowledge graph and then load to our in-memory cache ie redis and mysql db

## Most Challenging
1) MemcacheD applocation issues and how did we resolve it . 
2) Implement Generic Parser

## Most Difficult Problem
	Designing end to end to overcome bottleneck of existing system
		- database tuning
		- redis layer
		- sharding of db
		
## Interesting problem solved 
As others mentioned on the thread Bloom filter is a way to quickly tell whether an element does not belong to the set. I last used it when I was crawling a billion pages for building an offline search engine. At that we had four 4 GB RAM machines of which just 2.1 GB was accessible to the Java VM. We were doing an Open Crawl (discovering pages on the fly) and we had to ensure that we do not crawl the same pages again and again. Had we used a hashset with the 8 byte key as hash of URL we would have needed more than 2 Gigs just for this set. So we ended up using Bloom filter for this.
