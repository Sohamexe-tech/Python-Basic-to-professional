<html>
	<head>
		<title>
			Even Odd Finder-HTML Validation
		</title>
		<style>
			*{ font-size:40px;	text-align:center;
				font-family:Time New Roman}
			body{background-color:azure;}
		</style>
	</head>
	<body>
		<h1>Even Odd Finder</h1>
		
		<form method="POST">
		<input type="number" name="num"
		placeholder="Enter Integer"	required	/>
		<br/><br/>
		<input type="submit"	value="Check E/O"/>
		</form>

		<h2>{{msg}}</h2>
	</body>
</html>