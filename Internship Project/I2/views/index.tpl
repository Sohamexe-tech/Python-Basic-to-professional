<!DOCTYPE html>
<html>
<head>
    <title>Zodiac Sign Finder</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: white;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            width: 500px;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
            text-align: center;
            background: #f9f9f9;
        }

        h1 {
            margin-bottom: 30px;
            font-size: 28px;
        }

        input {
            width: 100%;
            padding: 14px;
            margin: 15px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
        }

        button {
            width: 100%;
            padding: 14px;
            margin-top: 20px;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            background-color: black;
            color: white;
            cursor: pointer;
        }

        button:hover {
            background-color: #333;
        }

        .result {
            margin-top: 20px;
            font-size: 20px;
            color: green;
        }

        .error {
            margin-top: 20px;
            font-size: 18px;
            color: red;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Zodiac Sign Finder</h1>

    <form method="post">
        <input type="text" name="day" placeholder="Enter Day (1-31)" required>
        <input type="text" name="month" placeholder="Enter Month (1-12)" required>
        <input type="text" name="year" placeholder="Enter Year (e.g. 2003)" required>

        <button type="submit">Find Zodiac</button>
    </form>

    % if zodiac:
        <div class="result">
            Your Zodiac Sign is: <b>{{zodiac}}</b>
        </div>
    % end

    % if error:
        <div class="error">
            {{error}}
        </div>
    % end
</div>

</body>
</html>
