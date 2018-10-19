package Semaphores;

import java.util.concurrent.Semaphore;

class SharedCounter{
	public static int count = 1;
}

class MyCustomThread extends Thread{
	Semaphore sem;
	String name;
	int rem;
	
	public MyCustomThread(Semaphore sem, String name, int rem) {
		this.sem = sem;
		this.name = name;
		this.rem = rem;
	}
	
	@Override
	public void run() {
			while (SharedCounter.count < 10) {
				if (SharedCounter.count % 2 != rem) {
					try {
							sem.acquire();
						} catch (InterruptedException e) {
							e.printStackTrace();
						}
					
					System.out.println(name + ":" + SharedCounter.count);
					SharedCounter.count++;
					sem.release();
				}
			}
		}
}

public class PrintOddEven {
	public static void main(String args[]) throws InterruptedException {
		Semaphore sem = new Semaphore(1);
		MyCustomThread t1, t2;
		t1 = new MyCustomThread(sem, "Odd", 0);
		t2 = new MyCustomThread(sem, "Even", 1);
		
		t1.start();
		t2.start();
		
		t1.join();
		t2.join();
	}

}
