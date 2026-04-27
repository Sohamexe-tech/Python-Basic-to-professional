<!DOCTYPE html>
<html>
<head>
    <title>Add Languages</title>
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

        input[type=text] {
            width: 60%;
            padding: 12px;
            margin-top: 10px;
        }

        input[type=checkbox] {
            width: 25px;
            height: 25px;
            margin: 15px;
        }

        input[type=submit] {
            padding: 12px 40px;
            margin-top: 20px;
            background-color: #222;
            color: white;
            border: none;
            cursor: pointer;
        }

        .msg {
            margin-top: 20px;
            font-weight: bold;
            color: darkred;
        }
    </style>
</head>

<body>

<div class="nav">
    <a href="/">Home</a>
    <a href="/language">Language</a>
</div>

<h1>Add Languages</h1>

<form method="POST">
    Name<br/>
    <input type="text" name="name"/><br/><br/>

    Select Languages<br/>
    <input type="checkbox" name="py"/>Python
    <input type="checkbox" name="js"/>JavaScript
    <input type="checkbox" name="ja"/>Java
    <input type="checkbox" name="genai"/>Gen AI
    <br/>

    <input type="submit"/>

    <div class="msg">{{msg}}</div>
</form>

<p>Code by Soham Dalvi</p>

</body>
</html>
