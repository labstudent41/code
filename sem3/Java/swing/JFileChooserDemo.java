import java.awt.Event;
import java.io.File;
import javax.swing.*;

public class JFileChooserDemo extends JFrame {
	static JFileChooser fc = new JFileChooser();
	public JFileChooserDemo() {
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}
	public static void main(String args[]) {
		fc.setCurrentDirectory(new File("D:/sycs_vikas/Java"));
		fc.showDialog(new JFileChooser(), "open");
	}
}