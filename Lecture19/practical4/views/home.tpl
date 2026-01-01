<html>
<head>
	<title>Greeting App by Soham Dalvi</title>
	<style>
		h1 { font-size:40px; text-align:center; }
		body { background-color:azure; }
		h2 { font-size:70px; text-align:center; color:red; }
		body {background-color:azur;}
	</style>
</head>

<body>
	<h1> Greeting App </h1>

	<form method="POST">
		<input type="text" name="name" 
		placeholder="Enter Name" />
		<br/><br/>
		<input type="submit"/>
	</form>

	<h2>{{msg}}</h2>
</body>
</html>
