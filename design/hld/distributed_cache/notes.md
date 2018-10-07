## Cashing Features / Estimation
  - TB of data
  - 50k to 1M qps
  - ~= 1ms Latency
  - LRU (eviction)
  - 100 % avaialability
  - Scalable

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
   
