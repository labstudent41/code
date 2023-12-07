import javax.swing.*;

public class JComboBoxExample {
	JFrame jf;
	JComboBoxExample() {
		jf = new JFrame("JComboBox Example");
		String subjects[] = {"Java", "Python", "DBMS"};
		JComboBox cb = new JComboBox(subjects);
		cb.setBounds(10, 10, 150, 20);
		jf.add(cb);
		jf.setLayout(null);
		jf.setSize(200, 200);
		jf.setVisible(true);
	}
	
	public static void main(String args[]) {
		new JComboBoxExample();
	}
}