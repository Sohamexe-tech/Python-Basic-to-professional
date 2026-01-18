<!DOCTYPE html>
<html>
<head>
    <title>Tariff Calculator</title>
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: Arial;
            text-align: center;
        }
        h1 {
            color: #00ffcc;
        }
        input {
            padding: 10px;
            margin: 10px;
            width: 300px;
            font-size: 16px;
            border-radius: 8px;
            border: none;
        }
        button {
            padding: 10px 30px;
            font-size: 18px;
            background-color: #00ffcc;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        .error {
            color: red;
            font-size: 18px;
        }
        .result {
            color: #00ffcc;
            font-size: 20px;
        }
    </style>
</head>
<body>

    <h1>USA Tariff Calculator</h1>

    <form method="post">
        <input type="text" name="country" placeholder="Enter Country Name">
        <br>
        <input type="text" name="amount" placeholder="Enter Amount in USD">
        <br>
        <button type="submit">Calculate Tariff</button>
    </form>

    <p class="error">{{error}}</p>
    <p class="result">{{result}}</p>

</body>
</html>
