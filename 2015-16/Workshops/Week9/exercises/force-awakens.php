<?php
    if (isset($_POST['password'])) {
	if (md5($_POST['password'])=='e9b574e8a51f6e19e6ad8753860deea4') {
	    //hint: the password is 8 characters long and contains only lowercase letters and numbers
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
