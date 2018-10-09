package ImmutableClass;

public final class ImmutableStudent {
	String name;
	int rollNo;
	public ImmutableStudent(String name, int rollNo) {
		this.name = name;
		this.rollNo = rollNo;
	}
	
	public String getName() {
		return this.name;
	}
	
	public int getRollNo() {
		return this.rollNo;
	}

}
