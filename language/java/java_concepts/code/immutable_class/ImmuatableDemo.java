package ImmutableClass;

public class ImmuatableDemo {
	 public static void main(String args[]) 
	    {
		 ImmutableStudent s = new ImmutableStudent("ABC", 101); 
		 	System.out.println(s.name); 
		 	System.out.println(s.rollNo); 
		 	
		 ImmutableStudent s1 = new ImmutableStudent("ABCD", 1012); 
		 System.out.println(s1.name); 
		 System.out.println(s1.rollNo); 
	    }
}
