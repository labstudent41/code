<%-- 
    Document   : fib.jsp
    Created on : Sep 2, 2023, 11:50:12 AM
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
        int n=Integer.parseInt(request.getParameter("txtno"));
        int f0=0;
        int f1=1;
        int f2=0,i=1;
       while(i<=n)
        {
            %>
            <b><%=f0%></b>
            <%out.print("\t");
            f2=f0+f1;
            f0=f1;
            f1=f2;
            i++;
            }
%>
    </body>
</html>
