<html> 
	<head> 
		<title> 
			Languages You Know App 
		</title> 
		<style> 
			*{ font-size: 40px; 		text-align:center; 	} 
			body { background-color: linen; } 
			.nav { background-color: black; } 
			.nav a { color: white; text-decoration:none; margin:5%;} 
			table { margin:2% auto; width:70%;}
		</style> 
	</head> 
	<body> 
 
		<div class="nav"> 
			<a href="/">	Home </a> 
			<a href="/language"> Language </a> 
		</div>
		<h1> Home Page </h1> 
 

		<table border="4"> 
			<tr>  
				<th>Name</th> 
				<th> Language </th> 
 
			</tr> 
		% for m in msg: 
			<tr> 

				<td>{{ m[0] }}</td> 
				<td>{{ m[1] }}</td> 
			</tr>
		% end
		</table> 
	</body>
</html> 
