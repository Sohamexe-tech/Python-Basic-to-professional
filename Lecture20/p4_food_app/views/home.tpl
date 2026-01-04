<html>
	<head>
		<title>
			Food You Like - JS Validation
		</title>
		<style>
		*{font-size:40px;	text-align:center;	font-family:Cambria;}
		body{background-color:lightpink;}
		</style>
	<script>
		fucntion check()
		{
			let num=document.getElementById("name");
			let msg=document.getElementById("msg");
	
			if (name.value==="")
			{
				alert("name should not be empty");
				msg.innerHTML="";
				name.focus();
				return false;
			}

			if (! name.value.match("^[A-Za-z]+$"))
			{
				alert("name should contain only alphabets");
				msg.innerHTML="";
				name.value="";
				name.focus();
				return false;
			}
			return true;
		}
	</script>
	</head>
	<body>
		<h1>Food You Like App</h1>

		<form method="POST" onsubmit="return check()">
		<label>Name</label>
		<br/>
		<input type="text"	name="name"	placeholder="Enter Name"	id="name"/>
			<br/> <br/>
			<label>Select One</label>
			<br/> 
			<input type="radio"	name="food"	value="North Indian"/>North Indian
			<input type="radio"	name="food"	value="South Indian"	checked=true/>South Indian
			<input type="radio"	name="food"	value="Fast Food"/>Fast Food
			<br/> <br/>
		<input type="submit" />
		</form>

		<h2 id="msg">{{msg}}</h2>
		
	</body>
</html>
