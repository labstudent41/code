/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package jdbc;

/**
 *
 * @author students
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.sql.*;

public class EmployeeDataForm extends JFrame implements ActionListener {

    String fields[] = {"ID", "Name", "Department", "Salary"};
    JLabel labels[] = new JLabel[fields.length];
    JTextField tfields[] = new JTextField[fields.length];
    JButton b1;

    EmployeeDataForm() {
        setSize(400, 200);
        setTitle("Employee form");
        setLayout(new GridLayout(5, 2));
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        for (int i = 0; i < fields.length; i++) {
            labels[i] = new JLabel(fields[i]);
            tfields[i] = new JTextField();
            add(labels[i]);
            add(tfields[i]);
        }

        b1 = new JButton("Submit");
        b1.addActionListener(this);
        add(b1);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        if (ae.getSource() == b1) {
            try {
                Class.forName("com.mysql.jdbc.Driver");
                Connection con = DriverManager.getConnection("jdbc:mysql://localhost/sycs19", "master", "");
                String sql = "INSERT INTO employee VALUES (?, ?, ?, ?)";
                PreparedStatement pstmt = con.prepareStatement(sql);
                int r1 = Integer.parseInt(tfields[0].getText());
                for (int i = 0; i < fields.length; i++) {
                    pstmt.setString(i+1, tfields[i].getText());
                }
                JOptionPane.showMessageDialog(null, "Record " + r1 + " inserted");
                pstmt.executeUpdate();
                pstmt.close();
                con.close();

            } catch (SQLException e) {
                System.out.println("SQL Error : " + e.getMessage());
            } catch (ClassNotFoundException e) {
                System.out.println("Class not found exception");
            }
        }
    }

    public static void main(String args[]) {
        new EmployeeDataForm();
    }
}
