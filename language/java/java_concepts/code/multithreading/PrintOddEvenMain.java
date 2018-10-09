package Multithreading;

public class PrintOddEvenMain {
	public static void main(String[] args) {
 
		OddEvenRunnable oddRunnable=new OddEvenRunnable(1);
		OddEvenRunnable evenRunnable=new OddEvenRunnable(0);
 
		Thread t1=new Thread(oddRunnable,"Odd");
		Thread t2=new Thread(evenRunnable,"Even");
		
		t1.start();
		t2.start();
 
	}
}
 