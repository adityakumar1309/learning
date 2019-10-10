![Image description](https://github.com/adityakumar1309/learning/blob/master/images/bloom_filter1.png)
![Image description](https://github.com/adityakumar1309/learning/blob/master/images/bloom_filter2.png)

Applications of Bloom filters

Medium uses bloom filters for recommending post to users by filtering post which have been seen by user.

Quora implemented a shared bloom filter in the feed backend to filter out stories that people have seen before.

The Google Chrome web browser used to use a Bloom filter to identify malicious URLs

Google BigTable, Apache HBase and Apache Cassandra, and Postgresql use Bloom filters to reduce the disk lookups for non-existent rows or columns

https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
