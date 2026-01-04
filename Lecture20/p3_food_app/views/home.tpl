<html>
<head>
	<title>Food You Like - HTML Validation</title>

	<style>
		*{
			font-size:40px;
			font-family:Cambria;
		}

		body{
			background-color:lightyellow;
			text-align:center;
		}

		input{
			text-align:center;
		}
	</style>
</head>

<body>
	<h1>Food You Like App</h1>

	<form method="POST">
		<label>Name</label>
		<br/>
		<input type="text" name="name" placeholder="Enter Name"
		       pattern="^[A-Za-z]+$" required/>
		<br/><br/>

		<label>Select One</label>
		<br/>
		<input type="radio" name="food" value="North Indian"/> North Indian
		<input type="radio" name="food" value="South Indian" checked/> South Indian
		<input type="radio" name="food" value="Fast Food"/> Fast Food
		<br/><br/>

		<input type="submit"/>
	</form>

	<h2 id="msg">{{msg}}</h2>
</body>
</html>
