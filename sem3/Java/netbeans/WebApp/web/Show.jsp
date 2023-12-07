<%-- 
    Document   : Show
    Created on : 8 Sep, 2023, 11:27:12 AM
    Author     : students
--%>

<%@page import="java.sql.*"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        
        <%
            Connection conn = null;
            PreparedStatement stmt = null;
            String name = "";
            int rollno = 0, age = 0;
            try {
                rollno = Integer.parseInt(request.getParameter("rollno"));
                age = Integer.parseInt(request.getParameter("age"));
                name = request.getParameter("name");
                Class.forName("com.mysql.jdbc.Driver");
                conn = DriverManager.getConnection("jdbc:mysql://localhost/sycs19", "root", "");
                stmt = conn.prepareStatement("INSERT INTO TYCS VALUES(?, ?, ?)");
                stmt.setInt(1, rollno);
                stmt.setString(2, name);
                stmt.setInt(3, age);
                stmt.execute();
                stmt.close();
                conn.close();
            } catch (ClassNotFoundException e) {
                out.println("Class not found");
                e.printStackTrace();
            } catch (SQLException e) {
                out.println("Sql error");
//                out.println(e.printStackTrace());
            }
        %>
        <h2>
            Name : <%out.println(name);%>
            Age : <%out.println(age);%>
            Roll no : <%out.println(rollno);%>
            Record saved!!!
        </h2>
        <h3><a href="ShowAll.jsp">View all records</a></h3>
    </body>
</html>
