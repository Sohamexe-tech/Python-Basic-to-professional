<!DOCTYPE html>
<html>
<head>
    <title>Daily Utility Calculator</title>
    <style>
        body {
            background-color: #f4f6f8;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
        }
        form {
            background-color: white;
            width: 350px;
            margin: auto;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input, select {
            width: 90%;
            padding: 10px;
            margin: 8px 0;
            border-radius: 4px;
            border: 1px solid #ccc;
            font-size: 14px;
        }
        button {
            width: 95%;
            padding: 10px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 15px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        .result {
            color: #2c3e50;
            font-size: 18px;
            margin-top: 15px;
        }
        .error {
            color: red;
            font-size: 16px;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<h1>Daily Utility Calculator</h1>

<form method="post">
    <select name="operation">
        <option value="">Select Operation</option>
        <option value="add">Addition</option>
        <option value="sub">Subtraction</option>
        <option value="mul">Multiplication</option>
        <option value="div">Division</option>
        <option value="bmi">BMI Calculator</option>
    </select>

    <input type="text" name="n1" placeholder="Enter First Value">
    <input type="text" name="n2" placeholder="Enter Second Value / Weight">

    <button type="submit">Calculate</button>

    <p class="error">{{error}}</p>
    <p class="result">{{result}}</p>
</form>

</body>
</html>
