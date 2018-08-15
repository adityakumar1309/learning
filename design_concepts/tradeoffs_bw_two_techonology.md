## Mysql vs PostgresSql
-	MySQL doesn’t support CTE (very big deal!)
-	MySQL doesn’t support window functions (another big deal)
-	Array: MySQL doesn’t support working with arrays
-	PostgreSQL has better/consistent interface when working with date/times
-	PostgreSQL supports VALUES for manual list of values, MySQL you have to do SELECT UNION ALL (quite painful)
-	Various useful functions MySQL doesn’t support: generate_series, string split (into array); generally I find Postgres offers a lot more feature-specific functions than MySQL
-	JSON Support and NoSQL
-	This is a recent addition to PostgreSQL, and it does make the platform more appealing to anyone who wants to try out NoSQL and store JSON (JavaScript Object Notation) files in the database
-	It also supports indexing JSON data for faster access.
-	Subqueries were one of MySQL’s major weaknesses for a long time; it was notorious for losing its way with two or more levels of sub-queries. Since 5.6.5, though, there have been major improvements—but PostgreSQL is still considered better for joins especially as MySQL doesn’t support Full Outer Joins.

## Mechached Vs Redis
Another scenario in which Memcached has an advantage over Redis is in scaling. Because Memcached is multithreaded, you can easily scale up by giving it more computational resources. Redis, which is mostly single-threaded, can scale horizontally via clustering without loss of data. Clustering is an effective scaling solution, but it is comparatively more complex to set up and operate. Memcached does not support replication.
Memcached is very good to handle high traffic websites. It can read lots of information at a time and give you back at a great response time. Redis can also handle high traffic on read but also can handle heavy writes as well.

## Kafka vs RabbitMq
RabbitMQ will keep all states about consumed/acknowledged/unacknowledged messages while Kafka doesn't, it assumes the consumer keep tracks of what's been consumed and not. RabbitMQ's queues are fastest when they're empty, while Kafka retain large amounts of data with very little overhead - Kafka is designed for holding and distributing large volumes of messages. (If you plan to have very long queues in RabbitMQ you could have a look at lazy queues.)
Kafka is built from the ground up with horizontal scaling in mind, while RabbitMQ is mostly designed for vertical scaling.
RabbitMQ will keep all states about consumed/acknowledged/unacknowledged messages while Kafka doesn't, it assumes the consumer keep tracks of what's been consumed and not.

## Mutex vs Semaphore
  - Mutex can be released only by thread that had acquired it, while you can signal semaphore from any other thread (or process), so semaphores are more suitable for some synchronization problems like producer-consumer.
  - Basic----------------Semaphore is a signalling mechanism.	Mutex is a locking mechanism.
  - Existence------------Semaphore is an integer variable.	Mutex is an object.
  - Function-------------Semaphore allow multiple program threads to access a finite instance of resources.	Mutex allow multiple program thread to access a single resource but not simultaneously.
  - Ownership------------Semaphore value can be changed by any process acquiring or releasing the resource.	Mutex object lock is released only by the process that has acquired the lock on it.
  - Categorize-----------Semaphore can be categorized into counting semaphore and binary semaphore.	Mutex is not categorized further.
  - Operation------------Semaphore value is modified using wait() and signal() operation.	Mutex object is locked or unlocked by the process requesting or releasing the resource.
  - Resources_Occupied---If all resources are being used, the process requesting for resource performs wait() operation and block itself till semaphore count become greater than one.	If a mutex object is already locked, the process requesting for resources waits and queued by the system till lock is released.

## Observer Pattern vs Pub/Sub
Observer pattern, the Observers are aware of the Subject, also the Subject maintains a record of the Observers. Whereas, in Publisher/Subscriber, publishers and subscribers don’t need to know each other. They simply communicate with the help of message queues or broker.
In Publisher/Subscriber pattern, components are loosely coupled as opposed to Observer pattern.
Observer pattern is mostly implemented in a synchronous way, i.e. the Subject calls the appropriate method of all its observers when some event occurs. The Publisher/Subscriber pattern is mostly implemented in an asynchronous way (using message queue).
Observer pattern needs to be implemented in a single application address space. On the other hand, the Publisher/Subscriber pattern is more of a cross-application pattern.

## Strong Consistency vs Eventual Consistency
Strong consistency = It says data will get passed on to all the replicas as soon as a write request comes to one of the replicas of the database.
But during the time these replicas are being updated with new data, response to any subsequent read/write requests by any of the replicas will get delayed as all replicas are busy in keeping each other consistent.
As soon as they become consistent, they start to take care of the requests that have come at their door.
eventual consistency = Eventual consistency offers low latency at the risk of returning stale data

## Optimistic Locking vs Pessimist Locking
*Optimistic Locking* is a strategy where you read a record, take note of a version number (other methods to do this involve dates, timestamps or checksums/hashes) and check that the version hasn't changed before you write the record back. When you write the record back you filter the update on the version to make sure it's atomic. (i.e. hasn't been updated between when you check the version and write the record to the disk) and update the version in one hit.
If the record is dirty (i.e. different version to yours) you abort the transaction and the user can re-start it.
This strategy is most applicable to high-volume systems and three-tier architectures where you do not necessarily maintain a connection to the database for your session. In this situation the client cannot actually maintain database locks as the connections are taken from a pool and you may not be using the same connection from one access to the next.

*Pessimistic Locking* is when you lock the record for your exclusive use until you have finished with it. It has much better integrity than optimistic locking but requires you to be careful with your application design to avoid Deadlocks. To use pessimistic locking you need either a direct connection to the database (as would typically be the case in a two tier client server application) or an externally available transaction ID that can be used independently of the connection.

## Sticky Sesions vs Non Sticky Sessions
-If the load balancer is instructed to use sticky sessions, all of your interactions will happen with the same physical server, even though other servers are present. Thus, your session object will be the same throughout your entire interaction with this website.
-To summarize, In case of Sticky Sessions, all your requests will be directed to the same physical web server while in case of a non-sticky loadbalancer may choose any webserver to serve your requests.

*Collaboration systems utilizing Operational Transformations typically use replicated document storage, where each client has their own copy of the document; clients operate on their local copies in a lock-free, non-blocking manner, and the changes are then propagated to the rest of the clients; this ensures the client high responsiveness in an otherwise high-latency environment such as the Internet. When a client receives the changes propagated from another client, it typically transforms the changes before executing them; the transformation ensures that application-dependent consistency criteria (invariants) are maintained by all sites. This mode of operation results in a system particularly suited for implementing collaboration features, like simultaneous document editing, in a high-latency environment such as the web.*

