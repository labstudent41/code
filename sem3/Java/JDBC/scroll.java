import java.sql.*;
import javax.swing.*;
public class scroll{
    public static void main(String args[]){
        try{
            Class.forName("com.mysl.jdbc.Driver");
            Connection con=DriverManager.getConnection("jdbc:mysql://localhost/jdbc","root","");
            Statement stmt=con.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_READ_ONLY);
            ResultSet rs=stmt.executeQuery("select * from emp");
            rs.absolute(4);
            System.out.println(rs.getString(1)+"\t"+rs.getString(2)+rs.getString(3));
            rs.previous();
            System.out.println(rs.getString(1)+"\t"+rs.getString(2)+rs.getString(3));
            rs.relative(2);
            System.out.println(rs.getString(1)+"\t"+rs.getString(2)+rs.getString(3));
            rs.relative(-2);
            System.out.println(rs.getString(1)+"\t"+rs.getString(2)+rs.getString(3));
            stmt.close();
            con.close();
           }
        catch(Exception e)
        {
            System.out.println("SQL error");
        }
}}