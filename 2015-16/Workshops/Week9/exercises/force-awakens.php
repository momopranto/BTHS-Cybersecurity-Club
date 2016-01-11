<?php
    if (isset($_POST['password'])) {
	if (md5($_POST['password'])=='9c6b65aeedaf95394d530f685f770a0c') {
	    ////hint: the password is 6 characters long and contains lowercase letters (%s) and numbers (%d) in the following format, %s%s%d%d%s%d
            echo "flag{XXXXXXXXXXXXXXXXXXX}";
        }
    }
    else {
        echo "<h1>Welcome back, Lord Ren</h1>
        <p>To verify your identity, please enter your secret password</p>
        <form action='#' method='post'>
        <input type='password' name='password' placeholder='Enter password'/>
        <input type='submit'/>
        </form>";
    }
?>
