import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class claculator  implements ActionListener {

    int n1,n2,op,result;

    JTextField tf = new JTextField(20);
    JButton b[]= new JButton[16];
    JPanel p1 = new  JPanel();
    JPanel p2 = new JPanel();
    JFrame jf = new JFrame();

    JButton b17 = new JButton("Clear Text field");
    JButton b18 = new JButton("Back Space");

    public claculator(){
        jf.setLayout(new GridLayout(3,0));
        jf.setSize(600,400);
        jf.setVisible(true);

        p1.setLayout(new GridLayout(4,4));

        String symbol[] ={
            "0","1","2","3","4","5","6","7","8","9","+","-","/","*","%","="
        };
        for(int i = 0 ; i<16;i++){
            b[i]=new JButton(symbol[i]);
            b[i].addActionListener(this);
            p1.add(b[i]);
        }
        p2.setLayout(new GridLayout(2,0));
        p2.add(b17);
        p2.add(b18);

        b17.addActionListener(this);
        b18.addActionListener(this);

        //p2.add(p1,"Center");
        //p1.add(p2,"Center");

        jf.add(tf);
        jf.add(p1);
        jf.add(p2);
    }
    public void actionPerformed(ActionEvent e){
        String symbol = e.getActionCommand();
        System.out.println("Symbol :"+symbol);
        /*if(symbol=="0"||symbol=="1"||symbol=="2"||symbol=="3"||symbol=="4"||symbol=="5"
        ||symbol=="6"||symbol=="7"||symbol=="8"||symbol=="9"){
            tf.setText(tf.getText()+symbol);
        }*/
        if(symbol=="="){
            cal();
        }
        else if(symbol=="+"){
            operation(1);
        }
        else if(symbol=="-"){
            operation(2);
        }
        else if(symbol=="*"){
            operation(3);
        }
        else if(symbol=="/"){
            operation(4);
        }
        else if(symbol=="%"){
            operation(5);
        }
        else if(symbol=="Clear Text field"){
            tf.setText("");
            n1=n2=0;
        }
        else if (symbol=="Back Space"){
            int p=Integer.parseInt(tf.getText());
            int q=p/10;
            tf.setText(String.valueOf(q));
            if(q==0){
                tf.setText("");
            }
        }
        else{
            tf.setText(tf.getText()+symbol);
        }
    }
    public void operation(int op){
        this.op=op;
        String text=tf.getText();
        if(!text.isEmpty()){
        n1=Integer.parseInt(text);
        tf.setText("");
        }
        else{
            System.out.println("Enter value");
        }
    }
    public void cal(){
        String text=tf.getText();
        if(!text.isEmpty()){
        n2=Integer.parseInt(text);
        tf.setText("");
        }
        else{
            return;
        }
        System.out.println("n1 :"+n1+"  "+"n2 :"+n2+"   "+"operation :"+op);
        switch(op){
            case 1:result=n1+n2;break;
            case 2:result=n1-n2;break;
            case 3:result=n1*n2;break;
            case 4:result=n1/n2;break;
            case 5:result=n1%n2;break;
        }
        tf.setText(String.valueOf(result));
    }
    public static void main(String args[]) {
        new claculator();
    }

}
