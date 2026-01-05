<!DOCTYPE html>
<html>
<head>
    <title>Languages You Know App</title>

    <style>
        * {
            font-size: 40px;
            font-family: Cambria;
            text-align: center;
        }

        body {
            background-color: linen;
        }

        .nav {
            background-color: black;
            padding: 20px;
        }

        .nav a {
            color: white;
            text-decoration: none;
            margin: 5%;
        }

        input[type=checkbox] {
            height: 25px;
            width: 25px;
            margin-left: 20px;
        }

        input[type=text] {
            width: 60%;
            padding: 10px;
            font-size: 35px;
        }

        input[type=submit] {
            font-size: 35px;
            padding: 10px 30px;
        }
    </style>
</head>

<body>

    <div class="nav">
        <a href="/">Home</a>
        <a href="/language">Language</a>
    </div>

    <h1>Language Page</h1>

    <form method="POST">
        <label>Name</label><br/>
        <input type="text" name="name" placeholder="Enter Name"/><br/><br/>

        <label>Select All You Know</label><br/>

        <input type="checkbox" name="py"/> Python
        <input type="checkbox" name="js"/> JavaScript
        <input type="checkbox" name="ja"/> Java
        <input type="checkbox" name="genai"/> Gen AI
        <br/><br/>

        <input type="submit"/><br/><br/>

        {{ msg }}
    </form>

    <p>Code by Soham Dalvi</p>

</body>
</html>
