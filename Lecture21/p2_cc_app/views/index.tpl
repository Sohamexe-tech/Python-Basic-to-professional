<html>
	<head>
		<title>
			Currency converter app by Soham Dalvi
		</title>
		<style>
			*{font-size:40px;	text-align:center;}
			body{background-color:orange;}
			.fc{border:groove;	width:60%	margin:2%auto;
	padding:2%;	border-radius:30px;}
			h2{border:solid}
		</style>
	</head>
	<body>
		<h1>Currency converter Message App</h1>
		<div class="fc">
			<form method="POST">
				<input type="number"	step="0.01"	name="amt"
				placeholder="Enter Amt in $: "required		/>
				<br/><br/>
				<input type="submit"	value="Convert to: "/>

			</form>
		<h2>
			{{msg}}
		</h2>		
		</div>
		
	</body>
<html>