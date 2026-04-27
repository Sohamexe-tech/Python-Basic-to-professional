<!DOCTYPE html>
<html>
<head>
<title>Update Task</title>
<style>
body { background:#fffdd0; text-align:center; font-size:26px; }
input, select { font-size:24px; width:50%; padding:10px; }
.error { color:red; }
</style>
</head>
<body>

<h2>Update Task</h2>

% if error:
<p class="error">{{error}}</p>
% end

<form method="post">
<input name="title" value="{{task['title']}}" required><br><br>

<select name="status">
<option {{'selected' if task['status']=='Not Completed' else ''}}>Not Completed</option>
<option {{'selected' if task['status']=='Completed' else ''}}>Completed</option>
</select><br><br>

<input type="submit" value="Update">
</form>

<br>
<a href="/">Back</a>
</body>
</html>
