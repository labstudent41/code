<%-- 
    Document   : login
    Created on : Sep 2, 2023, 12:06:35 PM
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
    if(request.getParameter("t2").equals("Carslover")){
        %><jsp:forward page="successful.html"/><%                  
    }
    else
    {
    %><jsp:include page="failure.html"/><%
    }
    %>   
    </body>
</html>
