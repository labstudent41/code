import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;

public class addemps extends JFrame implements ActionListener {
	JLabel l1, l2, l3, l4, l5;
	JButton b1, b2, b3;
	JTextField t1, t2, t3, t4, t5;

	addemps() {
		setSize(300, 300);
		setLayout(new FlowLayout());
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setTitle("Add Employee");
		l1 = new JLabel("Employee ID");
		l2 = new JLabel("Employee Name");
		l3 = new JLabel("Employee Dept");
		l4 = new JLabel("Employee Salary");
		l5 = new JLabel("Insert emp id to Update");

		t1 = new JTextField(10);
		t2 = new JTextField(10);
		t3 = new JTextField(10);
		t4 = new JTextField(10);
		t5 = new JTextField(10);

		b1 = new JButton("Insert Employee");
		b2 = new JButton("Update Employee");
		b3 = new JButton("Delete Employee");

		add(l5);
		add(t5);
		t1.setText(t5.getText());
		add(l1);
		add(t1);

		add(l2);
		add(t2);
		add(l3);
		add(t3);
		add(l4);
		add(t4);
		add(b1);
		add(b2);
		add(b3);

		b1.addActionListener(this);
		b2.addActionListener(this);
		b3.addActionListener(this);
		setVisible(true);
	}

	public static void main(String[] args) {
		new addemps();
	}

	@Override
	public void actionPerformed(ActionEvent ae) {
		if (ae.getSource() == b1) {
			try {
				Class.forName("com.mysql.jdbc.Driver");
				Connection con = DriverManager.getConnection("jdbc:mysql://localhost/jdbc", "root", "");
				String sql = "insert into emp values(?,?,?,?)";
				PreparedStatement pstmt = con.prepareStatement(sql);
				int r1 = Integer.parseInt(t1.getText());
				pstmt.setString(1, t1.getText());
				pstmt.setString(2, t2.getText());
				pstmt.setString(3, t3.getText());
				pstmt.setString(4, t4.getText());
				JOptionPane.showMessageDialog(null, "Record" + r1 + "inserted");
				pstmt.executeUpdate();
				pstmt.close();
				con.close();
			} catch (SQLException e) {
				System.out.println("SQL Error");
			} catch (ClassNotFoundException e) {
				System.out.println("Class Not Found Exception");
			}
		} else if (ae.getSource() == b2) {
			try {
				t1.setText(t5.getText());
				Class.forName("com.mysql.jdbc.Driver");
				Connection con = DriverManager.getConnection("jdbc:mysql://localhost/jdbc", "root", "");
				String sql = "update emp set e_name =?,e_dept=?,e_salary=? where e_id =?";
				PreparedStatement pstmt = con.prepareStatement(sql);
				int r1 = Integer.parseInt(t1.getText());
				pstmt.setString(1, t2.getText());
				pstmt.setString(2, t3.getText());
				pstmt.setString(3, t4.getText());
				pstmt.setString(4, t5.getText());
				JOptionPane.showMessageDialog(null, "Record" + r1 + "Updated");
				pstmt.executeUpdate();
				pstmt.close();
				con.close();
			} catch (SQLException e) {
				System.out.println("SQL Error");
			} catch (ClassNotFoundException e) {
				System.out.println("Class Not Found Exception");
			}
		} else if (ae.getSource() == b3) {
			try {
				t1.setText(t5.getText());
				Class.forName("com.mysql.jdbc.Driver");
				Connection con = DriverManager.getConnection("jdbc:mysql://localhost/jdbc", "root", "");
				String sql = "delete from emp where e_id=?";
				PreparedStatement pstmt = con.prepareStatement(sql);
				int r1 = Integer.parseInt(t1.getText());
				pstmt.setString(1, t5.getText());
				JOptionPane.showMessageDialog(null, "Record" + r1 + "Deleted");
				pstmt.executeUpdate();
				pstmt.close();
				con.close();
			} catch (SQLException e) {
				System.out.println("SQL Error");
			} catch (ClassNotFoundException e) {
				System.out.println("Class Not Found Exception");
			}
		}

	}

}
