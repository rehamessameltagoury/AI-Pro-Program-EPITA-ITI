package ThreadTrial;

//import threadsexample.ThreadsExample;

public class MyTask implements Runnable{
	
	  @Override
	    public void run() {
	        int x=10;
	        while(x<100){
	           // ThreadsExample.print(x);
	        	System.out.println("Exponential");
	            System.out.println(Math.getExponent(x));
	            x++;
	        }
	  }
	  }
