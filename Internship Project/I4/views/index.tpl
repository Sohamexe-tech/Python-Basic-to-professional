<!DOCTYPE html>
<html>
<head>
<title>To Do List</title>
<style>
body {
    background:#c8dddd;
    text-align:center;
    font-size:26px;
}
table {
    margin:auto;
    width:90%;
    border-collapse:collapse;
}
th, td {
    border:2px solid black;
    padding:20px;
}
</style>

<script>
function confirmDelete() {
    return confirm("Are you sure you want to delete this task?");
}
</script>
</head>

<body>

<h1>To Do List</h1>
<a href="/create">Add New Task</a><br><br>

<table>
<tr>
<th>S.No</th>
<th>Task</th>
<th>Status</th>
<th>Update</th>
<th>Delete</th>
</tr>

% for i, t in enumerate(tasks, start=1):
<tr>
<td>{{i}}</td>
<td>{{t['title']}}</td>
<td>{{t['status']}}</td>
<td><a href="/update/{{t['id']}}">Update</a></td>
<td><a href="/delete/{{t['id']}}" onclick="return confirmDelete()">Delete</a></td>
</tr>
% end

</table>

</body>
</html>
