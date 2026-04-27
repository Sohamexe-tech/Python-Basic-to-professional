<!DOCTYPE html>
<html>
<head>
    <title>Addition Application by Soham Dalvi</title>
    <style>
        * {
            font-size: 28px;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background-color: linen;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .card {
            background-color: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
            text-align: center;
            width: 450px;
        }

        h1 {
            margin-bottom: 30px;
        }

        input[type="number"] {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #999;
        }

        input[type="submit"] {
            background-color: #2c7be5;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #1a5fd0;
        }

        h2 {
            margin-top: 25px;
            color: green;
        }
    </style>
</head>

<body>
    <div class="card">
        <h1>Addition App</h1>

        <form method="POST">
            <input type="number" step="any" name="n1"
                   placeholder="Enter First Number" required/>
            <br/><br/>

            <input type="number" step="any" name="n2"
                   placeholder="Enter Second Number" required/>
            <br/><br/>

            <input type="submit" value="Add"/>
        </form>

        <h2>{{msg}}</h2>
    </div>
</body>
</html>
