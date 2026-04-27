<!DOCTYPE html>
<html>
<head>
    <title>Daily Motivation</title>

    <style>
        * {
            font-family: "Cambria", serif;
            text-align: center;
        }

        body {
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea, #764ba2);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }

        .card {
            width: 70%;
            max-width: 900px;
            padding: 50px;
            border-radius: 25px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }

        .quote {
            font-size: 42px;
            font-style: italic;
            line-height: 1.4;
        }

        .author {
            margin-top: 25px;
            font-size: 28px;
            opacity: 0.9;
        }

        button {
            margin-top: 40px;
            padding: 14px 45px;
            font-size: 26px;
            border-radius: 50px;
            border: none;
            background-color: white;
            color: #764ba2;
            cursor: pointer;
            transition: 0.3s ease;
        }

        button:hover {
            transform: scale(1.05);
            background-color: #f1f1f1;
        }

        footer {
            margin-top: 25px;
            font-size: 20px;
            opacity: 0.7;
        }
    </style>
</head>

<body>

<div class="card">

    <div class="quote">
        “{{quote}}”
    </div>

    <div class="author">
        — {{author}}
    </div>

    <form>
        <button type="submit">✨ New Quote</button>
    </form>

    <footer>
        Stay positive. Keep moving forward.
    </footer>

</div>

</body>
</html>
