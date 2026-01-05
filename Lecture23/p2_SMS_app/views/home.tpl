<html>
<head>
    <title>SMS App</title>
    <style>
        *{font-size:40px;text-align:center;}
        body{background-color:lightyellow;}
        .nav{background-color:black;}
        .nav a{color:white;text-decoration:none;margin:5%;}
        table{margin:auto;}
    </style>
</head>
<body>
    <div class="nav">
        <a href="/">Home</a>
        <a href="/create">Create</a>
    </div>

    <h1>Home Page</h1>

    <table border="5">
        <tr>
            <th>Rno</th>
            <th>Name</th>
            <th>Marks</th>
            <th>Delete</th>
            <th>Update</th>
        </tr>

        % for m in msg:
        <tr>
            <td>{{m[0]}}</td>
            <td>{{m[1]}}</td>
            <td>{{m[2]}}</td>
            <td><a href="/delete/{{m[0]}}"><button>Delete</button></a></td>
            <td><a href="/update/{{m[0]}}"><button>Update</button></a></td>
        </tr>
        % end
    </table>
</body>
</html>
