<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <meta charset="utf-8" />
        <title>Login</title>
		<link rel="stylesheet" href="static/css/styles.css">
    </head>
    <body>
        <form method="post" action="/login">
			<legend>Login</legend>
			% if "error" in locals():
			<p>Error: {{error}}</p>
			% end
            <input type="text" name="username" placeholder="Username"/>
            <input type="password" name="password" placeholder="Password" />
			<input type="submit">
        </form>
    </body>
</html>