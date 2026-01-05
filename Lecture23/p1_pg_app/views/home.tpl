<!DOCTYPE html>
<html>
<head>
    <title>Password Generator App</title>
    <style>
        *{
            font-size:40px;
            text-align:center;
        }
        body{
            background-color:azure;
        }
        input, select{
            font-size:35px;
        }
    </style>
</head>

<body>

<h1>Password Generator App</h1>

<form method="POST">

    <label>Select Password Length</label><br/>
    <select name="le">
        <option value="6">6</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
        <option value="10">10</option>
        <option value="11">11</option>
    </select>

    <br/><br/>

    <input type="checkbox" name="uc"> Uppercase Letters<br/>
    <input type="checkbox" name="di"> Digits<br/>
    <input type="checkbox" name="sp"> Special Characters

    <br/><br/>

    <input type="submit" value="Generate Password">

</form>

<h2>{{ msg }}</h2>

<p>Code by Soham Dalvi</p>

</body>
</html>
