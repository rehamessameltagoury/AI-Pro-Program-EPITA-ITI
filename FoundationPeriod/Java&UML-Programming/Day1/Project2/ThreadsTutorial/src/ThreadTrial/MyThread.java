package ThreadTrial;

public class MyThread extends Thread {
	
	@Override
    public void run() {
        int x=10;
        while(x<100){
        	System.out.println(this.getName());
           System.out.println(Math.sqrt(x));
            x++;
        }
        }
}
