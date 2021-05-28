package commonvariables;

public interface Constants {
  double pi =22/7;
  double computeArea();
  default void myMethod(){
      System.out.println("Test");
  }
}
