1) use thread safe queue or some hash datastructure like hashtable or use hashtable with synchronized 
    - make use of two sets of currently_used set and available resource set .

2) In ResourcePool abstract class 
    - have abstract methods like create(), validate(), dead()
    - have getResourceObject() method
    - have releaseResourceObject() method
    
3) One class extending ResourcePool abstract class like eg DatabaseConnectionPool class 

4) Client class which makes use of this 

eg:

abstract class ObjectPool<T>
  
  	Hashtable<T, Long> lock, unlock; 
    
  	abstract T create(); 
	
  	abstract boolean validate(T o); 
	
	abstract void dead(T o); 
  
  	synchronized T getPoolObject(){...}
	
	synchronized void returnPoolObject(T t){...}
  
 class JDBCConnectionPool extends ObjectPool<Connection>
    
    Connection create(){...}
    
    void dead(Connection o){...}
    
    boolean validate(Connection o){...}
    
    
  class Main{...}
