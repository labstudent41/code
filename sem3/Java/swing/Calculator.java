import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Calculator extends JFrame implements ActionListener {
	JFrame jf;
	JLabel firstNL, secondNL, resultL;
	JTextField firstNT, secondNT, resultT;
	JButton plusB, minusB, mulB, divB;
	Calculator() {
		jf = new JFrame("Simple Calculator");
		jf.setLayout(new FlowLayout());
		jf.setSize(400, 400);
		jf.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		firstNL = new JLabel("First First");
		secondNL = new JLabel("Second Number");
		resultL = new JLabel("Result");
		
		firstNT = new JTextField(5);
		secondNT = new JTextField(5);
		resultT = new JTextField(5);
		
		plusB = new JButton("+");
		minusB = new JButton("-");
		mulB = new JButton("*");
		divB = new JButton("/");
		
		jf.add(firstNL); jf.add(firstNT);
		jf.add(secondNL); jf.add(secondNT);
		jf.add(resultL); jf.add(resultT);
		jf.add(plusB); jf.add(minusB);
		jf.add(mulB); jf.add(divB);
		
		plusB.addActionListener(this);
		minusB.addActionListener(this);
		mulB.addActionListener(this);
		divB.addActionListener(this);
		
		jf.setVisible(true);
	}
	
	public void actionPerformed(ActionEvent ae) {
		int a, b, c = 0;
		a = Integer.parseInt(firstNT.getText());
		b = Integer.parseInt(secondNT.getText());
		
		if (ae.getSource() == plusB) {
			c = a + b;
		}
		else if (ae.getSource() == minusB) {
			c = a - b;
		}
		else if (ae.getSource() == mulB) {
			c = a * b;
		}
		else if (ae.getSource() == divB) {
			c = a / b;
		}
		resultT.setText(Integer.toString(c));
	}
	
	public static void main(String args[]) {
		new Calculator();
	}
}