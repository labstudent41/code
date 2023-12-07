/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.sql.*;
import javax.sql.*;

public class employee{
    public static void main(String args[]){
        try{
            Class.forName("com.mysql.jdbc.Driver");
        Connection con=DriverManager.getConnection("jdbc:mysql://localhost/emp","root","");
        Statement stmt=con.createStatement();
        String sql="select * from employ";
        ResultSet rs=stmt.executeQuery(sql);
        System.out.println("Display data from emp table");
        while(rs.next()){
        System.out.println(rs.getString(1)+ "\t");
        System.out.println(rs.getString(2)+ "\t");
        System.out.println(rs.getString(3)+ "\t");
        System.out.println(rs.getString(4)+ "\t");
        System.out.println();
    }
        stmt.close();
        con.close();
}
    catch(SQLException  e){
    System.out.println("sql error");}
    catch (ClassNotFoundException e ){
    System.out.println("class not found Exception");
}
    }
}
    
        
        
     

/**
 *
 * @author students
 */

    
