import javax.swing.*;
import java.awt.*;

class JColorChooserDemo extends JFrame {

	public JColorChooserDemo() {
		changeAndSetColor();
	}
	private void changeAndSetColor() {

		setTitle("JColorChooserDemo");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		Color c = JColorChooser.showDialog(this, "chooseacolor", Color.BLUE);
		getContentPane().setBackground(c);
		setSize(300, 300);
		setVisible(true);
	}

	public static void main(String args[]) {
		new JColorChooserDemo();
	}
}
