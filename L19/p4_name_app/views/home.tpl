<!DOCTYPE html>
<html>
<head>
    <title>Greeting App by Soham Dalvi</title>
    <style>
        * {
            font-size: 28px;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
            color: white;
        }

        body {
            background-color: #1e1e2f;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .card {
            background-color: #2a2a3d;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.6);
            text-align: center;
            width: 450px;
        }

        h1 {
            margin-bottom: 30px;
        }

        input[type="text"] {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            border: none;
            background-color: #3a3a55;
            color: white;
        }

        input::placeholder {
            color: #bbbbbb;
        }

        input[type="submit"] {
            margin-top: 20px;
            background-color: #4caf50;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #43a047;
        }

        h2 {
            margin-top: 25px;
            font-size: 40px;
            color: white;
        }
    </style>
</head>

<body>
    <div class="card">
        <h1>Greeting App</h1>

        <form method="POST">
            <input type="text" name="name"
                   placeholder="Enter Name" required/>
            <br/><br/>
            <input type="submit" value="Greet"/>
        </form>

        <h2>{{msg}}</h2>
    </div>
</body>
</html>
