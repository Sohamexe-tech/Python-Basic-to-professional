<html>
<head>
    <title>What Next App by Kamal Sir</title>

    <style>
        * { font-size: 40px; text-align: center; }
        body { background-color: azure; }
        .nav { background-color: black; }
        .nav a { color: white; text-decoration: none; margin: 5%; }
    </style>
</head>

<body>

    <div class="nav">
        <a href="/">Home</a>
        <a href="/whatnext">WhatNext</a>
    </div>

    <h1>WhatNext Page</h1>

    <form method="POST">
        <label>Name</label><br/>
        <input type="text" name="name" placeholder="Enter Name" required />
        <br/><br/>

        <label>Select One</label><br/>

        <input type="radio" name="choice" value="Job" checked /> Job
        <input type="radio" name="choice" value="MS" /> MS
        <input type="radio" name="choice" value="MBA" /> MBA

        <br/><br/>
        <input type="submit" value="Submit" />
    </form>

    <h2>{{ msg }}</h2>

</body>
</html>
