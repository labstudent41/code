import javax.swing.*;
import java.awt.*;
import java.awt.event.*;


class Myframe extends JFrame{

    Container c;
    JLabel l1,l2;
    JPasswordField pass;
    JTextField f1;
    JButton b1;

    Myframe(){
        setTitle("Login Form");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(700, 500);
        setLocation(100, 50);
        

        c=getContentPane();
        c.setLayout(null);

        l1=new JLabel("USERNAME");
        l1.setBounds(10, 10, 100, 30);
        c.add(l1);

        l2=new JLabel("PASSWORD");
        l2.setBounds(10, 70, 100, 30);
        c.add(l2);

        f1=new JTextField();
        f1.setBounds(90, 10, 80, 30);
        c.add(f1);

        pass=new JPasswordField();
        pass.setBounds(90, 70, 80, 30);
        c.add(pass);

        b1=new JButton("LOGIN");
        b1.setBounds(10, 140, 100,30);
        c.add(b1);


        
        b1.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
        String username = f1.getText();
        String password = new String(pass.getPassword());

            if(username.equals("admin") && password.equals("password")) {
                JOptionPane.showMessageDialog(null, "Login Successful!");
            } else {
                JOptionPane.showMessageDialog(null, "Invalid Username or Password!");
            }
        }
        });


        setVisible(true);

    }

}
class loginform {
    public static void main(String args[]){
        Myframe frame=new Myframe();
    }

    
    
}
