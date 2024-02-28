<%-- 
    Document   : temp
    Created on : Sep 2, 2023, 10:55:05 AM
    Author     : STUDENTS
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
            int ctemp;
            float ftemp;
            ctemp=Integer.parseInt(request.getParameter("temp"));
            ftemp=((9.0f/5.0f)*ctemp)+32.0f;
        %>
        <b>Temperature in Fahrenheit is<%=ftemp%>
        </b>
    </body>       
</html>
