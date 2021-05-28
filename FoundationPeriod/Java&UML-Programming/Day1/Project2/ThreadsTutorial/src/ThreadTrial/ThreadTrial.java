package ThreadTrial;

import java.util.logging.Level;
import java.util.logging.Logger;

import threadsexample.ThreadsExample;

//import threadsexample.MyThread;
//import threadsexample.ThreadsExample.InnerThread;

//import threadsexample.MyThread;

public class ThreadTrial {
	static int x=10;
	 public static void main(String[] args) {
		 MyThread mth=new MyThread();
	        mth.setName("Square Root");
	        MyTask mt=new MyTask();
	        Thread th=new Thread(mt);
	        th.setName("Exponential");
	        // will start the exponential then the square root
	        mth.start();
	        th.start();
	      //for non static member inner classes only
	        ThreadTrial te=new ThreadTrial();
	        //for static member inner classes only
	        ThreadTrial.InnerThread sic=new ThreadTrial.InnerThread();
	        
	        Thread th3=new Thread(new Runnable(){
	            public void run(){
	                int x=10;
	        while(x<100){
	        	ThreadTrial.print(x);
	            x++;
	            }
	        }
	        });
	        
	      new Thread(() -> {
	          int x1 = 10;
	            while (x1 < 100) {
	            	ThreadTrial.print(x1);
	                x1++;
	            }
	        }).start(); 
	        
	        
	        
	        
	 }
	 public static synchronized void print(int x)
     { // to make the thread work in synchronized theme
         System.out.println(Thread.currentThread().getName()+"=== ");
         try {
             Thread.sleep(20);
         } catch (InterruptedException ex) {
             Logger.getLogger(MyThread.class.getName()).log(Level.SEVERE, null, ex);
         }
         System.out.println(Math.sqrt(x));
     }
	 static class InnerThread extends Thread{
	        // creating a static inner class
	        public void myInnerMethod(){
	           x=100;
	        }   
	    }
	  public void outerMethod(){
	        InnerThread ic=this.new InnerThread();}
	        
	    }   

