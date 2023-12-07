<%-- 
    Document   : ShowAll
    Created on : 8 Sep, 2023, 11:55:44 AM
    Author     : students
--%>

<%@page import="java.sql.*"%>
<%@page import="java.sql.ResultSet"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Show ALL</title>
    </head>
    <body>
        
        <%
            Connection conn = null;
            Statement stmt = null;
            ResultSet rs = null;
            String query;
            try {
                Class.forName("com.mysql.jdbc.Driver");
                conn = DriverManager.getConnection("jdbc:mysql://localhost/sycs19", "root", "");
                stmt = conn.createStatement();
                query = "SELECT * FROM tycs";
                rs = stmt.executeQuery(query);
//                while(rs.next()) {
//                    out.println(rs.getString(1));
////                    for (int i = 1; i <= 3; i++) {
////                        out.println(rs.getString(i));
////                    }
//                }
//                stmt.close();
//                conn.close();
            } catch (ClassNotFoundException e) {
                out.println("Class not found");
                e.printStackTrace();
            } catch (SQLException e) {
                out.println("Sql error");
                e.printStackTrace()0;
            }
        %>
    </body>
</html>
