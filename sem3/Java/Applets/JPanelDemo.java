import java.awt.*;
import javax.swing.*;

/*
<applet code="JPanelDemo.class" width=300 height=300></applet>
*/

public class JPanelDemo extends JApplet {
	public void init() {
		
		JPanel pnl1 = new JPanel();
		JLabel lbl1 = new JLabel("Enter name");
		JTextField txt1 = new JTextField(10);
		JLabel lbl2 = new JLabel("Enter email");
		JTextField txt2 = new JTextField(10);
		pnl1.add(lbl1); pnl1.add(txt1);
		pnl1.add(lbl2); pnl1.add(txt2);
		
		JPanel pnl2 = new JPanel();
		JButton btn1 = new JButton("Ok");
		JButton btn2 = new JButton("Cancel");
		pnl2.add(btn1); pnl2.add(btn2);
		
		setLayout(new GridLayout());
		add(pnl1);
		add(pnl2);
		this.setSize(500, 200);
	}
}