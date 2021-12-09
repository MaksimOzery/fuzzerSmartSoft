<?php
function Instrumentator($number, $type, $object) {
  	$file = 'full.txt';
	// Открываем файл для получения существующего содержимого
	$current = file_get_contents($file);
		
	if(strripos($current, (string) $number)==false){
	$current .= $newphrase.(string)$number." = ".(string)$type." = ".(string)$object;
	$current .= "\n";
	// Пишем содержимое обратно в файл
	file_put_contents($file, $current);	
	}
}
?>