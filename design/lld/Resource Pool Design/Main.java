package pool.resource;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Enumeration;
import java.util.Hashtable;

abstract class ObjectPool<T> { 
	long deadTime; 

	Hashtable<T, Long> lock, unlock; 

	ObjectPool() 
	{ 
		deadTime = 50000; // 50 seconds 
		lock = new Hashtable<T, Long>(); 
		unlock = new Hashtable<T, Long>(); 
	} 

	abstract T create(); 
	abstract boolean validate(T o); 
	abstract void dead(T o); 

	synchronized T getPoolObject() 
	{ 
		long now = System.currentTimeMillis(); 
		T t; 
		if (unlock.size() > 0) { 
			Enumeration<T> e = unlock.keys(); 
			while (e.hasMoreElements()) { 
				t = e.nextElement(); 
				if ((now - unlock.get(t)) > deadTime) { 
					// object has deadd 
					unlock.remove(t); 
					dead(t); 
					t = null; 
				} 
				else { 
					if (validate(t)) { 
						unlock.remove(t); 
						lock.put(t, now); 
						return (t); 
					} 
					else { 
						// object failed validation 
						unlock.remove(t); 
						dead(t); 
						t = null; 
					} 
				} 
			} 
		} 
		// no objects available, create a new one 
		t = create(); 
		lock.put(t, now); 
		return (t); 
	} 
	synchronized void returnPoolObject(T t) 
	{ 
		lock.remove(t); 
		unlock.put(t, System.currentTimeMillis()); 
	} 
} 


class JDBCConnectionPool extends ObjectPool<Connection> { 
	String dsn, usr, pwd; 

	JDBCConnectionPool(String driver, String dsn, String usr, String pwd) 
	{ 
		super(); 
		/*
		try { 
			Class.forName(driver).newInstance(); 
		} 
		catch (Exception e) { 
			e.printStackTrace(); 
		} */
		this.dsn = dsn; 
		this.usr = usr; 
		this.pwd = pwd; 
	} 

	Connection create() 
	{ 
		try { 
			return (DriverManager.getConnection(dsn, usr, pwd)); 
		} 
		catch (SQLException e) { 
			e.printStackTrace(); 
			return (null); 
		} 
	} 

	void dead(Connection o) 
	{ 
		try { 
			((Connection)o).close(); 
		} 
		catch (SQLException e) { 
			e.printStackTrace(); 
		} 
	} 

	boolean validate(Connection o) 
	{ 
		try { 
			return (!((Connection)o).isClosed()); 
		} 
		catch (SQLException e) { 
			e.printStackTrace(); 
			return (false); 
		} 
	}

 
} 

class Main { 
	public static void main(String args[]) 
	{ 
		// Create the ConnectionPool: 
		JDBCConnectionPool pool = new JDBCConnectionPool( 
			"org.hsqldb.jdbcDriver", "jdbc:hsqldb: //localhost/mydb", 
			"sa", "password"); 

		// Get a connection: 
		Connection con = pool.getPoolObject(); 
		// Return the connection: 
		pool.returnPoolObject(con); 
	} 
} 
