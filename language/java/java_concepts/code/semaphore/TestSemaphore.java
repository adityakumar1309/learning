package Semaphores;

import java.util.concurrent.Semaphore;

class SharedResource{
	public static int count = 0;
}

class CustomThread extends Thread{
	Semaphore sem;
	String name;
	
	public CustomThread(Semaphore sem, String name) {
		this.sem = sem;
		this.name = name;
	}
	
	@Override
	public void run() {
		if (this.name.equals("A")) {
			System.out.println("Thread A is waiting for the Permit");
			try {
				sem.acquire();
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			System.out.println("Thread A gets the Permit");
			for (int i = 0; i < 5; i++) {
				try {
					Thread.sleep(10);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				SharedResource.count = SharedResource.count - 1;
				System.out.println("A: "+SharedResource.count);
				
			}
			sem.release();
		}
		
		if (this.name.equals("B")) {
			System.out.println("Thread B is waiting for the Permit");
			try {
				sem.acquire();
			} catch (InterruptedException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			System.out.println("Thread B gets the Permit");
			for (int i = 0; i < 5; i++) {
				try {
					Thread.sleep(10);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				SharedResource.count = SharedResource.count - 1;
				System.out.println("B: "+SharedResource.count);
				
			}
			sem.release();
		}
	}
}

public class TestSemaphore {
	public static void main(String args[]) throws InterruptedException {
		Semaphore sem = new Semaphore(1);
		CustomThread t1, t2;
		t1 = new CustomThread(sem, "A");
		t2 = new CustomThread(sem, "B");
		
		t1.start();
		t2.start();
		
		t1.join();
		t2.join();
	}

}
