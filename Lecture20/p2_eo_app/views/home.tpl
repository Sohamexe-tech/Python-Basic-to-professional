<html>
	<head>
		<title>
			Even Odd Finder-JS Validation
		</title>
		<style>
			*{
				font-size: 40px;
				text-align: center;
				font-family: "Times New Roman";
			}

    body{
        background-color: azure;
    }
</style>


		<script>
			function check()
			{
				let num=document.getElementById("Num");
				let msg=document.getElementById("msg");
			
				if(num.value==="")
				{
					alert("please enter integer");
					msg.innerHTML="";
					num.focus();
					return.false;
				}

				return.true;
			}
		</script>
	</head>
	<body>
		<h1>Even Odd Finder</h1>
		
		<form method="POST">
		<input type="number" name="num"	id="num"
		placeholder="Enter Integer"	/>
		<br/><br/>
		<input type="submit"	value="Check E/O"/>
		</form>

		<h2>{{msg}}</h2>
	</body>
</html>
