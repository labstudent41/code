/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author students
 */
import java.sql.*;
import javax.sql.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class insert extends JFrame implements ActionListener{
    JFrame jf;
    JLabel l1,l2,l3,l4;
    JTextField t1,t2,t3,t4,t5;
    JButton b1;
    public insert(){
        jf=new JFrame();
        
        jf.setLayout(new FlowLayout());
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        l1=new JLabel("id");
        t1=new JTextField(10);
        l2=new JLabel("name");
        t2=new JTextField(10);
        l3=new JLabel("dept");
        t3=new JTextField(10);
        l4=new JLabel("salary");
        
        
        
        
        t4=new JTextField(10);
        t5=new JTextField(10);
        
        
        
        b1=new JButton("insert");
        jf.add(l1);
        jf.add(t1);
        jf.add(l2);
        jf.add(t2);
        jf.add(l3);
        jf.add(t3);
        jf.add(l4);
        
        
        
        jf.add(t4);
        jf.add(t5);
        jf.add(b1);
        jf.setSize(100,400);
        
        b1.addActionListener(this);
        jf.setVisible(true);
        }
    
    public void actionPerformed(ActionEvent ae){
        if (ae.getSource()==b1){
            try{
                Class.forName("com.mysql.jdbc.Driver");
                Connection con=DriverManager.getConnection("jdbc:mysql://localhost/jdbc","root","");
                String sql="insert into emp values(?,?,?,?)";
                PreparedStatement pstmt=con.prepareStatement("update emp set name=?");
                int r1=Integer.parseInt(t1.getText());
                pstmt.setString(1,t1.getText());
                pstmt.setString(2,t2.getText());
                pstmt.setString(3,t3.getText());
                pstmt.setString(4,t4.getText());
                
                
                JOptionPane.showMessageDialog(null,"record"+r1+"inserted");
                pstmt.executeUpdate();
                pstmt.close();
                con.close();
            
                
            }
            catch(SQLException e){
                System.out.println("sql error"); 
        }
            catch(ClassNotFoundException e){
                System.out.println("class not found exception");
        }
        }
            
        }
    public static void main(String args[]){
        new insert();
    }
        
    }
    
    

