package RestShapes;

import Shapes.Closedshape;

public class Triangle extends Closedshape {
    private int base,height; 
    // we can need to know the type of the triangle
    String type;
    
	@Override
	public double computeCircum() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public double computeArea() {
		// TODO Auto-generated method stub
		return 0.5*(base*height);
	}

	public int getBase() {
		return base;
	}

	public void setBase(int base) {
		this.base = base;
	}

	public int getHeight() {
		return height;
	}

	public void setHeight(int height) {
		this.height = height;
	}
	

}
