<%-- 
    Document   : show
    Created on : 8 Sep, 2023, 10:16:10 AM
    Author     : students
--%>
<%@page import="java.sql.*"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>jsp program show 1</title>
    </head>
    <body>
        <%
            int rollno=0;
            int age=0;
            String name = "";
            try{
                rollno=Integer.parseInt(request.getParameter("e1"));
                age=Integer.parseInt(request.getParameter("e2"));
                name=request.getParameter("e3");
                Class.forName("com.mysql.jdbc.Driver");
                Connection con =DriverManager.getConnection("jdbc:mysql://localhost/adiii","root","");
                PreparedStatement stmt = con.prepareStatement("insert into emp values(?,?,?)");
                stmt.setInt(1,rollno);
                stmt.setString(2,name);
                stmt.setInt(3,age);
                stmt.execute();  
            }
            catch(Exception e){
            out.println("Error");
        }%>
        <h2><% out.println("Name :"+name);%></h2><br>
        <h2><% out.println("Age :"+age);%></h2><br>
        <h2><% out.println("Rollno :"+rollno);%></h2><br>
        <h3><a href="showall.jsp">View all Record</a></h3>         
    </body>
</html>
