<!DOCTYPE html>
<html>
<head>
    <title>Languages App</title>
    <style>
        * {
            font-family: Cambria;
            text-align: center;
            font-size: 34px;
        }

        body {
            background-color: #f7f3ef;
        }

        .nav {
            background-color: #222;
            padding: 18px;
        }

        .nav a {
            color: white;
            text-decoration: none;
            margin: 5%;
        }

        table {
            width: 75%;
            margin: 40px auto;
            border-collapse: collapse;
            background-color: white;
        }

        th, td {
            padding: 18px;
            border-bottom: 2px solid #ccc;
        }

        th {
            background-color: #444;
            color: white;
        }
    </style>
</head>

<body>

<div class="nav">
    <a href="/">Home</a>
    <a href="/language">Language</a>
</div>

<h1>Known Languages</h1>

<table>
    <tr>
        <th>Name</th>
        <th>Languages</th>
    </tr>
    % for row in msg:
    <tr>
        <td>{{row[0]}}</td>
        <td>{{row[1]}}</td>
    </tr>
    % end
</table>

</body>
</html>
