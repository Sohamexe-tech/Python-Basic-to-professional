<!DOCTYPE html>
<html>
<head>
    <title>MyDay Planner</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        h2 {
            color: #2c3e50;
        }
        .box {
            background-color: white;
            width: 400px;
            margin: auto;
            padding: 20px;
            border-radius: 6px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
        }
        input {
            width: 90%;
            padding: 8px;
            margin: 10px 0;
        }
        button {
            padding: 6px 18px;
            background-color: #3498db;
            color: white;
            border: none;
            cursor: pointer;
        }
        ul {
            text-align: left;
            margin-top: 15px;
        }
        li {
            margin: 6px 0;
        }
        a {
            color: red;
            margin-left: 10px;
            text-decoration: none;
            font-size: 14px;
        }
        .error {
            color: red;
        }
        .msg {
            color: green;
        }
    </style>
</head>
<body>

<h2>MyDay Planner</h2>

<div class="box">
    <form method="post">
        <input type="text" name="task" placeholder="Enter task (alphabets only)">
        <br>
        <button type="submit">Add Task</button>
    </form>

    <p class="error">{{error}}</p>
    <p class="msg">{{message}}</p>

    <ul>
        % for i, task in enumerate(tasks):
            <li>
                {{task}}
                <a href="/delete/{{i}}">Delete</a>
            </li>
        % end
    </ul>
</div>

</body>
</html>
