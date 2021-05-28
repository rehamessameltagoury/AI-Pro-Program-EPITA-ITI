package Shapes;

import java.awt.Point;

import commonvariables.Constants;

public abstract class Closedshape implements Constants{
	 protected   Point vertix;
	    
	    public abstract double computeCircum();
	    public abstract double computeArea();

	    @Override
	    public String toString() {
	        return this.getClass().getName();
	    }

}
