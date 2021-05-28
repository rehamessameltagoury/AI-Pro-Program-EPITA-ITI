package Shapes;


public class Rectangle extends Closedshape {
	private int height,width;
	public int getWidth() {
		return width;
	}

	public void setWidth(int width) {
		if(width>0)
		this.width = width;
	}

	public int getHeight() {
		return height;
	}

	public void setHeight(int height) {
		if(height>0)
		this.height = height;
	}
	public double computeArea() {
		return height*width;
		
	}
	public double computeCircum() {
		return 2*(height+width);
		
	}

	

}
