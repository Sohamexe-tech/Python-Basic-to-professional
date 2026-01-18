<!DOCTYPE html>
<html>
<head>
    <title>Attendance Tracker</title>

    <style>
        *{
            font-family: Cambria;
        }

        body{
            background-color: #fffde7;
            text-align: center;
        }

        h1{
            font-size: 42px;
            color: #1f3b4d;
            margin-top: 30px;
        }

        .card{
            background-color: white;
            width: 420px;
            margin: 30px auto;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        input[type="text"], select{
            width: 90%;
            padding: 12px;
            font-size: 22px;
            margin: 15px 0;
            text-align: center;
        }

        button{
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 24px;
            cursor: pointer;
        }

        h2{
            margin-top: 30px;
            font-size: 32px;
        }

        label{
            font-size: 26px;
        }

        .radio-group{
            margin: 15px 0;
        }

        .radio-group input{
            transform: scale(1.5);
            margin: 10px;
        }

        table{
            margin: auto;
            margin-top: 25px;
            border-collapse: collapse;
            font-size: 22px;
        }

        th, td{
            border: 2px solid black;
            padding: 10px 20px;
        }

        .error{
            color: red;
            font-size: 22px;
        }

        .msg{
            color: green;
            font-size: 22px;
        }

        a{
            color: red;
            text-decoration: none;
        }
    </style>
</head>

<body>

<h1>Attendance Tracker</h1>

<div class="card">
    <form method="post">
        <input type="text" name="name"
               placeholder="Student Name (alphabets only)" />

        <select name="status">
            <option value="">Select Attendance</option>
            <option value="Present">Present</option>
            <option value="Absent">Absent</option>
        </select>

        <br><br>
        <button type="submit">Add Attendance</button>
    </form>

    <p class="error">{{error}}</p>
    <p class="msg">{{message}}</p>
</div>

<h2>Attendance Tracker App</h2>

<table>
    <tr>
        <th>Student Name</th>
        <th>Status</th>
        <th>Action</th>
    </tr>

    % for i, r in enumerate(records):
        <tr>
            <td>{{r["name"]}}</td>
            <td>{{r["status"]}}</td>
            <td><a href="/delete/{{i}}">Delete</a></td>
        </tr>
    % end
</table>

</body>
</html>
