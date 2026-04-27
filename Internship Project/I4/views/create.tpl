<!DOCTYPE html>
<html>
<head>
<title>Add Task</title>
<style>
body { background:#fffdd0; text-align:center; font-size:26px; }
input, select { font-size:24px; width:50%; padding:10px; }
.error { color:red; }
</style>
</head>
<body>

<h2>Add Task</h2>

% if error:
<p class="error">{{error}}</p>
% end

<form method="post">
<input name="title" required><br><br>

<select name="status">
<option>Not Completed</option>
<option>Completed</option>
</select><br><br>

<input type="submit" value="Save">
</form>

<br>
<a href="/">Back</a>
</body>
</html>
