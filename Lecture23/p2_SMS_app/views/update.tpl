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

    <h1>Update Page</h1>

    % if data:
    <form method="POST">
        <input type="number" name="rno" value="{{data[0]}}" readonly>
        <br><br>
        <input type="text" name="name" value="{{data[1]}}">
        <br><br>
        <input type="number" name="marks" value="{{data[2]}}" min="0" max="100">
        <br><br>
        <input type="submit" value="Update">
    </form>
    % end

    <h2>{{msg}}</h2>
</body>
</html>
