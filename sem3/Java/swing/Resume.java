import java.awt.*;
import javax.swing.*;
import javax.swing.plaf.FontUIResource;
import java.lang.reflect.Array;

public class Resume extends JFrame {

	public Resume() {
		setUIFont(new FontUIResource("Monospace", Font.BOLD, 18));
		JFrame jf = new JFrame("Swing");
		jf.setSize(800, 600);
		jf.setDefaultCloseOperation(EXIT_ON_CLOSE);
		jf.setLayout(new FlowLayout());

		JPanel jp = new JPanel(new GridLayout(5, 2));

		JTextField t1 = new JTextField(10);
		JTextField t2 = new JTextField(10);
		String quals[] = {"SSC", "HSC", "Degree"};
		JComboBox<String> cb = new JComboBox<>(quals);
		JTextField t3 = new JTextField();

		JPanel gp = new JPanel();
		JRadioButton rm = new JRadioButton("Male");
		JRadioButton rf = new JRadioButton("Female");
		ButtonGroup bg = new ButtonGroup();
		bg.add(rm); bg.add(rf);
		gp.add(rm); gp.add(rf);

		String fields[] = {
			"Name",
			"Email",
			"Qualification",
			"Gender",
			// "Age",
			"Address",
		};

		JComponent components[] = {t1, t2, cb, gp, t3};

		int nFields = Array.getLength(fields);
		for (int i = 0; i < nFields; i++) {
			jp.add(new JLabel(String.valueOf(fields[i])));
			jp.add(components[i]);
		}

		jf.add(jp);
		jf.setVisible(true);
	}

	public static void setUIFont(FontUIResource f) {
    java.util.Enumeration<Object> keys = UIManager.getDefaults().keys();
    while (keys.hasMoreElements()) {
      Object key = keys.nextElement();
      Object value = UIManager.get(key);
      if (value instanceof FontUIResource)
        UIManager.put(key, f);
      }
    }

	public static void main(String args[]) {
		System.out.println("Resume");
		new Resume();
	}
}
