<html>
	<head>
		<title>
			Food You Like - JS Validation
		</title>
		<style>
		*{font-size:40px;	text-align:center;	font-family:Cambria;}
		body{background-color:linen;}
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
		<input type="text"	name="name"	placeholder="Enter Name"	id="name" />
		<br/> <br/>
		<label>Select One</label>
		<br/>
		<select name="food">
			<option name="North Indian">North Indian</option>
			<option name="South Indian">South Indian</option>
			<option name="Chinese">Chinese</option>
			<option name="Italian">Italian</option>
			<option name="Mexican">Mexican</option>
			<option name="Konkani">Konkani</option>
		</select>
		<br/> <br/>
		<input type="submit" />
		</form>

		<h2 id="msg">{{msg}}</h2>
		
	</body>
</html>
