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

import java.sql.*;
// import javax.sql.*;

public class SelectQuery {
    public static void main(String args[]) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost/sycs19", "master", "");
            Statement stmt = con.createStatement();
            String sql = "select * from employee";
            ResultSet rs = stmt.executeQuery(sql);
            System.out.println("Display data from employee table");
            while (rs.next()) {
                for (int i = 1; i < 5; i++) {
                    System.out.print(rs.getString(i) + "\t");
                }
                System.out.println();
            }
            stmt.close();
            con.close();
        }
        catch(SQLException e) {
            System.out.println("SQL Error");
        }
        catch (ClassNotFoundException e) {
            System.out.println("Class not found exception");
        }
    }
}
