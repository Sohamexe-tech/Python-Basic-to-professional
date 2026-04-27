<!DOCTYPE html>
<html>
<head>
    <title>ExpenseTrack Lite</title>

    <style>
        *{
            font-family: Cambria;
        }

        body{
            background-color: #e3f2fd;
            text-align: center;
        }

        h1{
            font-size: 42px;
            color: #0d47a1;
            margin-top: 30px;
        }

        .card{
            background-color: white;
            width: 450px;
            margin: 30px auto;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        input[type="text"]{
            width: 90%;
            padding: 12px;
            font-size: 22px;
            margin: 10px 0;
            text-align: center;
        }

        .checkbox-group{
            font-size: 22px;
            text-align: left;
            margin-left: 40px;
        }

        button{
            background-color: #1976d2;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 24px;
            cursor: pointer;
            margin-top: 15px;
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

<h1>ExpenseTrack Lite</h1>

<div class="card">
    <form method="post">

        <input type="text" name="day" placeholder="Day (alphabets only)" />

        <input type="text" name="amount" placeholder="Amount (numbers only)" />

        <div class="checkbox-group">
            <b>Select Categories</b><br/>
            <input type="checkbox" name="category" value="Food"/> Food<br/>
            <input type="checkbox" name="category" value="Travel"/> Travel<br/>
            <input type="checkbox" name="category" value="Shopping"/> Shopping<br/>
            <input type="checkbox" name="category" value="Bills"/> Bills<br/>
            <input type="checkbox" name="category" value="Other"/> Other
        </div>

        <br/>
        <button type="submit">Add Expense</button>
    </form>

    <p class="error">{{error}}</p>
    <p class="msg">{{message}}</p>
</div>

<table>
    <tr>
        <th>Day</th>
        <th>Amount</th>
        <th>Categories</th>
        <th>Action</th>
    </tr>

    % for i, e in enumerate(expenses):
        <tr>
            <td>{{e["day"]}}</td>
            <td>{{e["amount"]}}</td>
            <td>{{e["categories"]}}</td>
            <td><a href="/delete/{{i}}">Delete</a></td>
        </tr>
    % end
</table>

</body>
</html>
