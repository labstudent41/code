import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.sql.*;
import javax.sql.*;
public class delete extends JFrame implements ActionListener{
    JLabel l1,l2,l3,l4,l11;
    JTextField t1,t2,t3,t4,t11;
    JButton b1;
    public delete(){
    JFrame f=new JFrame("delete");
    setSize(300,300);
    f.setLayout(null);
    f.setVisible(true);
    l1=new JLabel("id");
    t1=new JTextField(10);
    l1.setBounds(120,20,80,20);
    t1.setBounds(220,20,100,20);
    f.add(l1);
    f.add(t1);
    b1=new JButton("Enter");
    b1.setBounds(100,220,100,20);
    f.add(b1);
    b1.addActionListener(this);
    f.setDefaultCloseOperation(EXIT_ON_CLOSE);
    }
    public void actionPerformed(ActionEvent ae){
        if(ae.getSource()==b1){
            try{
         
                Class.forName("com.mysql.jdbc.Driver");
                Connection con=DriverManager.getConnection("jdbc:mysql://localhost/jdbc","root","");
                String sql="delete from employee where id=?";
                PreparedStatement pstmt=con.prepareStatement(sql);
                int r1=Integer.parseInt(t1.getText());
                pstmt.setString(1,t1.getText());
                JOptionPane.showMessageDialog(null,"Record"+r1+"Deleted");
                pstmt.executeUpdate();
                pstmt.close();
                con.close();
            }
            
            catch(SQLException e){
                System.out.println("sql error");
            }
            catch(ClassNotFoundException e){
                System.out.println("Class not found");
            }
       }
       
    }
    public static void main (String args[]){
        new delete();
    }
         
}