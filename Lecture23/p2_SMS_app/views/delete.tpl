<html>
<head>
    <title>SMS App</title>
    <style>
        *{font-size:40px;text-align:center;}
        body{background-color:lightyellow;}
        .nav{background-color:black;}
        .nav a{color:white;text-decoration:none;margin:5%;}
    </style>
</head>
<body>
    <div class="nav">
        <a href="/">Home</a>
        <a href="/create">Create</a>
    </div>

    <h1>Delete Page</h1>

    <form method="POST">
        <input type="number" name="rno" value="{{data}}" readonly>
        <br><br>
        <input type="submit" value="Delete">
    </form>

    <h2>{{msg}}</h2>
</body>
</html>
