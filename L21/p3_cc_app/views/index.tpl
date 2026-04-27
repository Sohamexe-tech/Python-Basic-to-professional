<html>
<head>
    <title>Currency Converter App by Soham Dalvi</title>

    <style>
        *{
            font-size: 26px;
            font-family: Arial, Helvetica, sans-serif;
            box-sizing: border-box;
        }

        body{
            background: linear-gradient(135deg, #ff9800, #ff5722);
            min-height: 100vh;
            margin: 0;

            display: flex;
            justify-content: center;   /* horizontal center */
            align-items: center;       /* vertical center */
        }

        h1{
            color: white;
            margin-bottom: 20px;
            text-align: center;
        }

        .container{
            text-align: center;
        }

        .fc{
            background-color: white;
            width: 350px;
            padding: 30px;
            border-radius: 25px;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
            text-align: center;
        }

        input[type=number]{
            width: 90%;
            padding: 12px;
            border-radius: 12px;
            border: 2px solid #ff9800;
            outline: none;
        }

        input[type=radio]{
            transform: scale(1.3);
            margin: 0 6px;
        }

        input[type=submit]{
            padding: 12px 30px;
            border: none;
            border-radius: 14px;
            background-color: #ff5722;
            color: white;
            cursor: pointer;
            transition: 0.3s;
        }

        input[type=submit]:hover{
            background-color: #e64a19;
            transform: scale(1.05);
        }

        h2{
            margin-top: 25px;
            padding: 15px;
            border-radius: 12px;
            background-color: #fff3e0;
            color: #e65100;
            border: 2px solid #ffcc80;
        }
    </style>
</head>

<body>

    <div class="container">
        <h1>Currency Converter App</h1>

        <div class="fc">
            <form method="POST">
                <input type="number" name="amt" placeholder="Enter Amount in ₹" required />
                <br/><br/>

                <input type="radio" name="curr" value="USD" checked /> USD
                <input type="radio" name="curr" value="GBP" /> GBP
                <input type="radio" name="curr" value="EUR" /> EUR
                <br/><br/>

                <input type="submit" value="Convert" />
            </form>

            <h2>{{msg}}</h2>
        </div>
    </div>

</body>
</html>
