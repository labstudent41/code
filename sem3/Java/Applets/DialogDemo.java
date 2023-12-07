import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/*
<html>
<body>
<applet code="DialogDemo.class" width=300 height=100>
</applet>
</body>
</html>
*/

public class DialogDemo extends JApplet implements ActionListener {
	JFrame jf;
	JButton b1, b2, b3, b4, b5;
	
	// DialogDemo() {
		// // this.setAccessible(true);
	// }
	public void init() {
		jf = new JFrame("Dialog Demo");
		jf.setLayout(new FlowLayout());
		jf.setSize(400, 400);
		// jf.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		b1 = new JButton("Error");
		b2 = new JButton("Warning");
		b3 = new JButton("Information");
		b4 = new JButton("Text");
		b5 = new JButton("Question");

		jf.add(b1);
		jf.add(b2);
		jf.add(b3);
		jf.add(b4);
		jf.add(b5);
		
		b1.addActionListener(this);
		b2.addActionListener(this);
		b3.addActionListener(this);
		b4.addActionListener(this);
		b5.addActionListener(this);
		jf.setVisible(true);
	}
	
	public void actionPerformed(ActionEvent ae) {
		if (ae.getSource() == b1) {
			JOptionPane.showMessageDialog(jf, "Error", "", JOptionPane.ERROR_MESSAGE);
		}
		else if (ae.getSource() == b2) {
			JOptionPane.showMessageDialog(jf, "Warning", "", JOptionPane.WARNING_MESSAGE);
		}
		else if (ae.getSource() == b3) {
			JOptionPane.showMessageDialog(jf, "Info", "", JOptionPane.INFORMATION_MESSAGE);
		}
		else if (ae.getSource() == b4) {
			JOptionPane.showMessageDialog(jf, "Text", "", JOptionPane.PLAIN_MESSAGE);
		}
		else if (ae.getSource() == b5) {
			JOptionPane.showMessageDialog(jf, "Question", "", JOptionPane.QUESTION_MESSAGE);
		}
	}
	
	public static void main(String args[]) {
		new DialogDemo();
	}
}