<!DOCTYPE html>
<html>
<head>
    <title>Update Student</title>
    <style>
        body {
            background-color: #88d488;
            text-align: center;
            font-family: Georgia;
        }
        input {
            width: 300px;
            height: 35px;
            font-size: 22px;
            margin: 15px;
        }
        label {
            font-size: 24px;
        }
        button {
            font-size: 22px;
            padding: 5px 15px;
        }
        a {
            font-size: 22px;
        }
    </style>
</head>
<body>

<h1>Update Student</h1>

<form method="post">

<label>Rno:</label>
<input type="number" value="{{student['rollno']}}" readonly><br>

<label>Name:</label>
<input type="text" name="name" value="{{student['name']}}" required><br>

<label>Marks:</label>
<input type="number" name="marks" value="{{student['marks']}}" min="0" max="100" required><br>

<br>
<button type="submit">Update</button>

</form>

<br><br>
<a href="/">Back</a>

</body>
</html>
