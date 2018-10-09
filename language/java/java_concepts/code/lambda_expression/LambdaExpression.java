package LambdaExpressions;

interface Addable{
	void add(int a, int b);
}

public class LambdaExpression {
	public static void main(String[] args) {  
		Addable adObj = (a,b) -> {
			System.out.println(a+b);
		};
		
	adObj.add(5, 6);
	}
}
