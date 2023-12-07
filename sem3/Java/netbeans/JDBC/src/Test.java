// import java.util.Scanner;
// import java.awt.*;
// import javax.swing.*;
import java.io.File;
import java.util.Arrays;

class Test {
	public static void main(String arg[]) {
   String classpath = System.getProperty("java.class.path");
   String[] classPathValues = classpath.split(File.pathSeparator);
   System.out.println(Arrays.toString(classPathValues));
	}
}
