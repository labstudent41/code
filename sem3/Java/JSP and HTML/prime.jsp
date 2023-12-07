<%-- 
    Document   : prime
    Created on : Sep 2, 2023, 11:32:49 AM
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
        int n=Integer.parseInt(request.getParameter("no"));
        int flag=1;
        if(n==1 || n<=0)
        {
            out.println("cant check prime name for this number");
        }
        else
        {
            for(int i=2;i<n;i++)
            {
                if(n%i==0)
                {
                    flag=0;
                    break;
                }
            }
            if(flag==1)
            {
                out.println(n+"is prime no");
            }
            else
            {
                out.println(n+"is not prime no");
            }
        }
        %>
    </body>
</html>
