import java.awt.*;
import java.applet.*;
import java.awt.event.*;
import javax.swing.*;

/* <applet code="Calculator.class" width=400 height=400></applet> */

public class Calculator extends JApplet implements ActionListener {
	int acc = 0, tmp = 0, operation = 0;
	JTextField tf = new JTextField();
	Panel root = new Panel();
	Panel p1 = new Panel();
	Panel p2 = new Panel();

	String specialOps[] = {
		"<=", "AC",
	};

	String symbols[] = {
		"7", "8", "9", "+",
		"4", "5", "6", "-",
		"1", "2", "3", "*",
		"%", "0", "=", "/"
	};

	JButton keypad[] = new JButton[symbols.length];
	JButton specialKeys[] = new JButton[specialOps.length];

	public void init() {
		setVisible(true);
		root.setLayout(new BorderLayout());
		p1.setLayout(new FlowLayout(FlowLayout.RIGHT));
		p2.setLayout(new GridLayout(4, 4));
		tf.setPreferredSize(new Dimension(100, 100));

		for (int i = 0; i < specialOps.length; i++) {
			specialKeys[i] = new JButton(specialOps[i]);
			specialKeys[i].setPreferredSize(new Dimension(50, 50));
			specialKeys[i].addActionListener(this);
			p1.add(specialKeys[i]);
		}

		for (int i = 0; i < symbols.length; i++) {
			keypad[i] = new JButton(symbols[i]);
			keypad[i].addActionListener(this);
			p2.add(keypad[i]);
		}

		root.add(p1, BorderLayout.NORTH);
		root.add(p2, BorderLayout.CENTER);
		add(tf, BorderLayout.NORTH);
		add(root, BorderLayout.CENTER);

	}

	public void actionPerformed(ActionEvent e) {
		// String symbol = ((JButton)e.getSource()).getText();
		String symbol = e.getActionCommand();
		if (symbol == "=") {
			calculate();
		} else if (symbol == "+") {
			setOperation(1);
		} else if (symbol == "-") {
			setOperation(2);
		} else if (symbol == "*") {
			setOperation(3);
		} else if (symbol == "/") {
			setOperation(4);
		} else if (symbol == "%") {
			setOperation(5);
		} else if (symbol == "<=") {
			String text = tf.getText();
			text = text.substring(0, text.length() - 1);
			tf.setText(text);
		} else if (symbol == "AC") {
			tf.setText("");
			acc = tmp = 0;
		} else {
			tf.setText(tf.getText() + symbol);
		}
		System.out.print(String.format("\n[%s] %4s   <%s> %4s\t",
					symbol, acc, operation, tmp));
	}

	public void setOperation(int operation) {
		String text = tf.getText();
		// System.out.println("Setting opereation " + this.operation);
		if (text.isEmpty()) return;
		if (acc == 0) {
			this.acc = Integer.parseInt(text);
			this.operation = operation;
			tf.setText("");
		} else {
			calculate();
		}
	}

	public void calculate() {
		System.out.print("Evaluating...");
		String text = tf.getText();
		if (text.isEmpty()) return;
		this.tmp = Integer.parseInt(text);

		switch(operation) {
			case 1: acc = acc + tmp; break;
			case 2: acc = acc - tmp; break;
			case 3: acc = acc * tmp; break;
			case 4: acc = acc / tmp; break;
			case 5: acc = acc % tmp; break;
			default: break;
		}
		tf.setText(String.valueOf(acc));
		this.acc = 0;
	}
}
