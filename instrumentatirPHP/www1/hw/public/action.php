<?php
$name="";
/**  инструментатор для интерпретироуемого когда*/

require_once "C:/projects_code/composer/vendor/autoload.php";

use PhpParser\Error;
use PhpParser\NodeDumper;
use PhpParser\ParserFactory;
use PhpParser\PrettyPrinter;
use PhpParser\Node;
use PhpParser\NodeTraverser;
use PhpParser\NodeVisitorAbstract;
use PhpParser\Node\Expr\Variable;
use PhpParser\Node\Scalar\String_;
use PhpParser\Node\Stmt\if_;
use PhpParser\Node\Stmt\TryCatch;
use PhpParser\Node\Stmt\Else_;
use PhpParser\Node\Stmt\ElseIf_;
use PhpParser\Node\Stmt\Throw_;
use PhpParser\Node\Stmt\Catch_;
use PhpParser\Node\Stmt\Case_;
use PhpParser\Node\Stmt\ClassMethod;
use PhpParser\Node\Stmt\For_;
use PhpParser\Node\Stmt\Foreach_;
use PhpParser\Node\Stmt\Do_;
use PhpParser\Node\Name;
use PhpParser\Node\Stmt\Use_;
use PhpParser\Node\Stmt\UseUse;
use PhpParser\Node\Stmt\Namespace_;
use PhpParser\Node\Expr\Include_;
use PhpParser\Node\Stmt\Function_;


class globalVars {
		static $b = 0;
		static $a = 0;
		static $name = "";
	}


$dictonry=[	"1"=>"system_usermanager.php",	
			
			 "2"=>"firewall_nat_edit.php",     
			 "3"=>"firewall_nat_1to1_edit.php",
			 "4"=>"firewall_nat_out.php",
			 "5"=>"firewall_nat_npt_edit.php",
			 "6"=>"firewall_rules_edit.php",
			 "7"=>"system_advanced_firewall.php",
			 "8"=>"firewall_scrub.php",
			 "9"=>"firewall_schedule_edit.php",  
			 "10"=>'system_groupmanager.php',
			 "11"=>'firewall_nat_out_edit.php',
			 "12"=>'system_authservers.php', 
			 "13"=>'diag_authentication.php',
			 "14"=>"firewall_scrub_edit.php",
			 "15"=>"system_certmanager.php"
			
			];

foreach($dictonry as $key=>$value){
	
	$file1 = file_get_contents('./test/'.$value);
	$code = $file1;

	$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);
	try {
		$ast = $parser->parse($code);
	} catch (Error $error) {
		echo "Parse error: {$error->getMessage()}\n";
		return;
	}

	$dumper = new NodeDumper;


	$traverser = new NodeTraverser();


	echo "</br>";
	echo "start Instrumentation \n";
    echo (string)$value;
	
	(string)globalVars::$name =(string)$value;
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {	
			
			if ($node instanceof Namespace_ ) {  
				$useUse = new UseUse(new Name('\InstrumentatorPHP.php'));                
				$node->stmts= array_merge( [new Use_([$useUse])],$node->stmts); 
				
				}
			}
		});		
	
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof if_ ) {            
				$node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.', "if" , "'.(string)globalVars::$name.'");')],$node->stmts ) ;
				globalVars::$b=globalVars::$b+1;
				globalVars::$a=	globalVars::$a+1;	
				
				}
			}
		});	
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof Node\Stmt\Else_ ) {            
				$node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.', "else" , "'.(string)globalVars::$name.'");')],$node->stmts ) ;
				globalVars::$b=globalVars::$b+1;
				globalVars::$a=	globalVars::$a+1;			
				}
			}
		});
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof Node\Stmt\ElseIf_ ) {            
				$node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.' , "elseif"  , "'.(string)globalVars::$name.'");')],$node->stmts ) ;
				globalVars::$b=globalVars::$b+1;
				globalVars::$a=	globalVars::$a+1;	
				}
			}
		});				
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof TryCatch  ) {
				$node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.' , "TryCatch" , "'.(string)globalVars::$name.'");')],$node->stmts ) ;
				globalVars::$b=globalVars::$b+1;
				globalVars::$a=	globalVars::$a+1;	
		}
			}
				});	
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof Catch_  ) {
				$node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.' , "Catch_" , "'.(string)globalVars::$name.'");')],$node->stmts ) ;	
				globalVars::$b=globalVars::$b+1;
				globalVars::$a=	globalVars::$a+1;	
				}
			}
		});
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof Case_  ) {
			   $node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.', "Case_"   , "'.(string)globalVars::$name.'");')],$node->stmts ) ;
			   globalVars::$b=globalVars::$b+1;
			   globalVars::$a=	globalVars::$a+1;	
				}							
			}
		}	
	);
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof ClassMethod  ) { 		   
			   $node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.' , "ClassMethod"  , "'.(string)globalVars::$name.'");')] ,$node->stmts ) ;
			   globalVars::$b=globalVars::$b+1;		
				globalVars::$a=	globalVars::$a+1;				   
				}							
			}
		});
		
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
	public function leaveNode(Node $node) {
		if ($node instanceof Function_  ) { 		   
		   $node->stmts= array_merge( [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.' , "Function_"  , "'.(string)globalVars::$name.'");')] ,$node->stmts ) ;
		   globalVars::$b=globalVars::$b+1;		
		   globalVars::$a=	globalVars::$a+1;				   
			}							
		}
	});	
		
	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof For_  ) { 		  
			   $node->stmts= array_merge( $node->stmts, [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.'  , "For_"  , "'.(string)globalVars::$name.'");')] ) ;	
			   globalVars::$b=globalVars::$b+1;
				globalVars::$a=	globalVars::$a+1;				   
				}							
			}
		});

	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof Foreach_  ) { 
			   $node->stmts= array_merge( $node->stmts, [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.' , "Foreach_" , "'.(string)globalVars::$name.'");')] ) ;
			   globalVars::$b=globalVars::$b+1;
			   globalVars::$a=	globalVars::$a+1;	
				}							
			}
		});

	$traverser->addVisitor(new class extends NodeVisitorAbstract {
		public function leaveNode(Node $node) {
			if ($node instanceof Do_  ) { 
			   $node->stmts= array_merge( $node->stmts, [new Node\Scalar\String_('Instrumentator('.(string)globalVars::$b.', "Do_" , "'.(string)globalVars::$name.'");')] ) ;	
				globalVars::$b=globalVars::$b+1;
				globalVars::$a=	globalVars::$a+1;					
							
				}							
			}
		});

	$ast = $traverser->traverse($ast);
	echo "</br>";
	echo "End Instrumentation \n";

	$prettyPrinter = new PrettyPrinter\Standard;
	$text =$prettyPrinter->prettyPrintFile($ast);
	
	
	$pos      = strripos($text, "$peremen");
	echo $pos;
	if($pos ==false){
	$newphrase = str_replace("'Ins", "Ins", $text);
	$newphrase = str_replace(");'", ");", $newphrase);
	}else{
	$newphrase = str_replace("'if($peremen==0)", "if($peremen==0)", $text);
	$newphrase = str_replace("$peremen+1;}'", "$peremen+1;}", $newphrase);	
		
	}
	$file = './text/'.$value;
	// Открываем файл для получения существующего содержимого
	$current = file_get_contents($file);
	$current .= $newphrase;
	// Пишем содержимое обратно в файл
	file_put_contents($file, $current);
	echo "</br>";
	echo "file write \n";
	echo "</br>";
	echo "< Node in write to code = \n".(string)globalVars::$b;
	echo "< Name file = ".$value;
	echo "< information to file write = ".(string)globalVars::$a;
	(string)globalVars::$a=0;
}

?>


