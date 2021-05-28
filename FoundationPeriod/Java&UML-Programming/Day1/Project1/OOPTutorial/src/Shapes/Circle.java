package Shapes;

import commonvariables.Constants;

public class Circle extends Closedshape  {
	private int raduis;
	//Point vertix;
	//double pi=22/7;
	public double computeArea() {
		//pi*r^2
		return raduis*Constants.pi*raduis;
	}
	public double computeCircum() {
		//pi*r^2
		return 2*Constants.pi*raduis;
	}
	public void setRaduis(int r) {
		this.raduis=r;
		}
	public double getRaduis() {
		return raduis;
		}
	

}
