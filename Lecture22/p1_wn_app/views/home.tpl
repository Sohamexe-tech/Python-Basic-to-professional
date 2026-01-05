<html>
<head>
    <title>What Next App by SOHAM DALVI</title>

    <style>
        * { font-size: 40px; text-align: center; }
        body { background-color: azure; }
        .nav { background-color: black; }
        .nav a { color: white; text-decoration: none; margin: 5%; }
        table { margin: 2% auto; width: 60%; }
    </style>
</head>

<body>

    <div class="nav">
        <a href="/">Home</a>
        <a href="/whatnext">WhatNext</a>
    </div>

    <h1>Home Page</h1>

    <table border="5">
        <tr>
            <th>Name</th>
            <th>Choice</th>
        </tr>

        % for m in msg:
        <tr>
            <td>{{ m[0] }}</td>
            <td>{{ m[1] }}</td>
        </tr>
        % end

    </table>

</body>
</html>
