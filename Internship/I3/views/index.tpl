<!DOCTYPE html>
<html>
<head>
    <title>Student Management System</title>
    <style>
        body {
            background-color: #b7d0d0;
            text-align: center;
            font-family: Georgia;
        }
        table {
            margin: auto;
            border-collapse: collapse;
            width: 60%;
        }
        th, td {
            border: 1px solid black;
            padding: 10px;
            font-size: 22px;
        }
        th {
            background-color: #cfe0e0;
        }
        a {
            font-size: 22px;
        }
    </style>
</head>
<body>

<h1>Student Management System</h1>

<a href="/create">Add New Student</a>
<br><br>

<table>
    <tr>
        <th>Rno</th>
        <th>Name</th>
        <th>Marks</th>
        <th>Update</th>
        <th>Delete</th>
    </tr>

% for s in students:
    <tr>
        <td>{{s['rollno']}}</td>
        <td>{{s['name']}}</td>
        <td>{{s['marks']}}</td>
        <td><a href="/update/{{s['rollno']}}">Update</a></td>
        <td><a href="/delete/{{s['rollno']}}">Delete</a></td>
    </tr>
% end

</table>

</body>
</html>
