## Cashing Features / Estimation
  - TB of data
  - 50k to 1M qps
  - ~= 1ms Latency
  - LRU (eviction)
  - 100 % avaialability
  - Scalable
  - Fault Tolerant / Persistent

## Caching Best Practice
  - validity
  - high hit rate
  - cache miss
  - ttl
  
 ## cache access patterns
  - write through cache (writes the cache and db)
  - write around cache (go around cache ie misses cache and write to db)
  - write back cache (writes into cache and another service sync up cache and db)
  
 ## Implementation
   HAshTable
   - size 30 lets say
   - (word) --> hashFunc --> hashedValued (it is base 256 if we are using md5) --> convert into base10 (decimal) -> base10Value % sizeOfCache = index of HashTable
   - inacse of collision we will have chain of linked list for given index . 
   - use consitent hasing to make this hasing distributed 
   - we need to have service which can do read/update hash and linked list etc . 
   - So we need event driven logic .
   ![alt text](https://github.com/adityakumar1309/learning/blob/master/images/Screen%20Shot%202018-10-07%20at%207.50.06%20PM.png)
   
## How to make Your Caching fault tolerant/persistent ?
 1) Regular time snapshot eg : how redis does dumps rdb file which is snapshot file periodically
 2) Have Replicas
 3) Use Log to reconstruct . Requests will be written to some kind of queue where requests will be written async . One service will keep reading this and update the log .
 Picture Gives what we mean 
 ![alt text](https://github.com/adityakumar1309/learning/blob/master/images/Screen%20Shot%202018-10-07%20at%209.53.33%20PM.png)
 
 ## How do we handle Availability ?
  1) Have Replication factor 2 . (means every node will have 2 other replicas)
     Advantage of this beside the obvious is loads will also get distributed among replicas . Other replica can act as slave .
  
   
 
