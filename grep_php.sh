grep -Ri "echo" .
grep -Ri "\$_" . | grep "echo"
grep -Ri "\$_GET" .
grep -Ri "\$_GET" . | grep "echo"
grep -Ri "\$_POST" . 
grep -Ri "\$_POST" . | grep "echo"
grep -Ri "\$_REQUEST" .
grep -Ri "\$_REQUEST" . | grep "echo"
grep -Ri "shell_exec(" .
grep -Ri "system(" .
grep -Ri "exec(" .
grep -Ri "popen(" .
grep -Ri "passthru(" .
grep -Ri "proc_open(" .
grep -Ri "pcntl_exec(" .
grep -Ri "eval(" .
grep -Ri "assert(" .
grep -Ri "preg_replace" . | grep "/e"
grep -Ri "create_function(" .
grep -Ri "\$sql" .
grep -Ri "\$sql" . | grep "\$_"
grep -Ri "phpinfo" .
grep -Ri "debug" .
grep -Ri "\$_GET['debug']" .
grep -Ri "\$_GET['test']" .
grep -Ri "file_include" .
grep -Ri "include(" .
grep -Ri "require(" .
grep -Ri "require(\$file)" .
grep -Ri "include_once(" .
grep -Ri "require_once(" .
grep -Ri "require_once(" . | grep "\$_"
grep -Ri "header(" . | grep "\$_"
grep -Ri '$_SERVER["HTTP_USER_AGENT"]' .
grep -Ri file_get_contents .
