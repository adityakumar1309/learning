# How is data written?
Cassandra processes data at several stages on the write path, 
starting with the immediate logging of a write and ending in with a write of data to disk:
Logging data in the commit log
Writing data to the memtable
Flushing data from the memtable
Storing data on disk in SSTables
Logging writes and memtable storage
When a write occurs, Cassandra stores the data in a memory structure called memtable, and to provide configurable durability, it also appends writes to the commit log on disk. The commit log receives every write made to a Cassandra node, and these durable writes survive permanently even if power fails on a node. The memtable is a write-back cache of data partitions that Cassandra looks up by key. The memtable stores writes in sorted order until reaching a configurable limit, and then is flushed.

##Flushing data from the memtable
To flush data from the memtable, the database writes data to disk in the memtable-sorted order. 
A partition index is also created on the disk that maps the tokens to a location on disk.

When the memtable content exceeds the configurable threshold, or the commitlog space exceeds the commitlog_total_space_in_mb, 
the memtable is put in a queue that is flushed to disk. You can configure the memtable_heap_space_in_mb or 
memtable_offheap_space_in_mb setting in the cassandra.yaml file. If the data to be flushed exceeds the memtable_cleanup_threshold, 
the database blocks writes until the next flush succeeds.

Manually flush a table using nodetool flush or nodetool drain (flushes memtables without listening for connections to other nodes). To reduce the commit log replay time, DataStax recommends flushing the memtable before you restart the nodes. If a node stops working, replaying the commit log restores the writes to the memtable that were there before the node stopped.

##Storing data on disk in SSTables
Memtables and SSTables are maintained per table. The commit log is shared among tables. SSTables are immutable, not written to again after the memtable is flushed. Consequently, a partition is typically stored across multiple SSTable files. A number of other SSTable structures exist to assist read operations:

![alt text](https://github.com/adityakumar1309/coding/blob/master/images/cassandra_write.png)

# How is data read?
To satisfy a read, Cassandra must combine results from the active memtable and potentially multiple SSTables.
