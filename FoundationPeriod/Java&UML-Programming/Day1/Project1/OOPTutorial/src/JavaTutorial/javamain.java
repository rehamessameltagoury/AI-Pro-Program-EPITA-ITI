package JavaTutorial;

import RestShapes.Triangle;
import Shapes.Circle;
import Shapes.Rectangle;

public class javamain {
public static void main(String[] args){
	System.out.println("################Circle############");
   Circle c=new Circle();

   c.setRaduis(4);
   System.out.println(c.getRaduis());
   System.out.println(c.computeArea());
   System.out.println("################Rectangle############");
   Rectangle r= new Rectangle();
   r.setHeight(5);
   r.setWidth(5);
   System.out.println(r.getHeight());
   System.out.println(r.computeArea());
   System.out.println("################Triangle############");
   Triangle t=new Triangle();
   t.setBase(10);
   t.setHeight(5);
   System.out.println(t.computeArea());
}

}
