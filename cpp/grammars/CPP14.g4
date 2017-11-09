/*******************************************************************************
 * The MIT License (MIT)
 *
 * Copyright (c) 2015 Camilo Sanchez (Camiloasc1)
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 ******************************************************************************/

/*******************************************************************************
 * C++14 Grammar for ANTLR v4
 *
 * Based on n4140 draft paper
 * https://github.com/cplusplus/draft/blob/master/papers/n4140.pdf
 * and
 * http://www.nongnu.org/hcb/
 *
 * Possible Issues:
 *
 * Input must avoid conditional compilation blocks (this grammar ignores any preprocessor directive)
 * GCC extensions not yet supported (do not try to parse the preprocessor output)
 * Right angle bracket (C++11) - Solution '>>' and '>>=' are not tokens, only '>'
 * Lexer issue with pure-specifier rule ('0' token) - Solution in embedded code
 *   Change it to match the target language you want in line 1097 or verify inside your listeners/visitors
 *   Java:
if($val.text.compareTo("0")!=0) throw new InputMismatchException(this);
 *   JavaScript:

 *   Python2:

 *   Python3:

 *   C#:

 ******************************************************************************/
grammar CPP14;

/*Basic concepts*/
translationunit
:
	declarationseq? EOF
;

/*Expressions*/
lambdacapture
:
	capturedefault
	| capturelist
	| capturedefault ',' capturelist
;

idexpression
:
	unqualifiedid
	| nestednamespecifier Template? unqualifiedid
;

unqualifiedid
:
	Identifier
	| Operator theoperator
	| Operator typespecifierseq conversiondeclarator?
	| literaloperatorid
	| '~' classname
	| '~' decltypespecifier
	| Identifier '<' templateargumentlist? '>'
    | Operator theoperator '<' templateargumentlist? '>'
    | literaloperatorid '<' templateargumentlist? '>'
;

nestednamespecifier
:
	'::'
	| thetypename '::'
	| Identifier '::'
	| decltypespecifier '::'
	| nestednamespecifier Identifier '::'
	| nestednamespecifier Template? Identifier '<' templateargumentlist? '>' '::'
;

capturedefault
:
	'&'
	| '='
;

capturelist
:
	capture '...'?
	| capturelist ',' capture '...'?
;

capture
:
	Identifier
    | '&' Identifier
    | This
	| Identifier initializer
    | '&' Identifier initializer
;

lambdadeclarator
:
	'(' parameterdeclarationclause ')' Mutable? exceptionspecification?
	attributespecifierseq? ('->' trailingtypespecifierseq abstractdeclarator?)?
;

postfixexpression
:
	Integerliteral
    | Characterliteral
    | Floatingliteral
    | Stringliteral
    | FalseToken
    | TrueToken
    | Nullptr
    | Userdefinedintegerliteral
    | Userdefinedfloatingliteral
    | Userdefinedstringliteral
    | Userdefinedcharacterliteral
    | This
    | '(' expression ')'
    | idexpression
    | '[' lambdacapture? ']' lambdadeclarator? '{' statementseq? '}'
	| postfixexpression '[' expression ']'
	| postfixexpression '[' bracedinitlist ']'
	| postfixexpression '(' initializerlist? ')'
	| simpletypespecifier '(' initializerlist? ')'
	| typenamespecifier '(' initializerlist? ')'
	| simpletypespecifier bracedinitlist
	| typenamespecifier bracedinitlist
	| postfixexpression '.' Template? idexpression
	| postfixexpression '->' Template? idexpression
	| postfixexpression '.' pseudodestructorname
	| postfixexpression '->' pseudodestructorname
	| postfixexpression '++'
	| postfixexpression '--'
	| Dynamic_cast '<' typespecifierseq abstractdeclarator? '>' '(' expression ')'
	| Static_cast '<' typespecifierseq abstractdeclarator? '>' '(' expression ')'
	| Reinterpret_cast '<' typespecifierseq abstractdeclarator? '>' '(' expression ')'
	| Const_cast '<' typespecifierseq abstractdeclarator? '>' '(' expression ')'
	| Typeid '(' expression ')'
	| Typeid '(' typespecifierseq abstractdeclarator? ')'
;

pseudodestructorname
:
	nestednamespecifier? thetypename '::' '~' thetypename
	| nestednamespecifier Template Identifier '<' templateargumentlist? '>' '::' '~' thetypename
	| nestednamespecifier? '~' thetypename
	| '~' decltypespecifier
;

unaryexpression
:
	postfixexpression
	| unaryincdecexpression
	| unaryoperator castexpression
	| Sizeof unaryexpression
	| Sizeof '(' typespecifierseq abstractdeclarator? ')'
	| Sizeof '...' '(' Identifier ')'
	| Alignof '(' typespecifierseq abstractdeclarator? ')'
	| Noexcept '(' expression ')'
	| newexpression
	| deleteexpression
;

// used in ASSIGNMENTS
unaryincdecexpression
:
    '++' castexpression
	| '--' castexpression
;

unaryoperator
:
	'|'
	| '*'
	| '&'
	| '+'
	| '!'
	| '~'
	| '-'
;

// used in BRANCHES
newexpression
:
	'::'? New ('(' initializerlist ')')? typespecifierseq newdeclarator? newinitializer?
	| '::'? New ('(' initializerlist ')')? '(' typespecifierseq abstractdeclarator? ')' newinitializer?
;

newdeclarator
:
	ptroperator newdeclarator?
	| noptrnewdeclarator
;

noptrnewdeclarator
:
	'[' expression ']' attributespecifierseq?
	| noptrnewdeclarator '[' constantexpression ']' attributespecifierseq?
;

newinitializer
:
	'(' initializerlist? ')'
	| bracedinitlist
;

// used in BRANCHES
deleteexpression
:
	'::'? Delete castexpression
	| '::'? Delete '[' ']' castexpression
;

castexpression
:
	unaryexpression
	| '(' typespecifierseq abstractdeclarator? ')' castexpression
;

pmexpression
:
	castexpression
	| pmexpression '.*' castexpression
	| pmexpression '->*' castexpression
;

multiplicativeexpression
:
	pmexpression
	| multiplicativeexpression '*' pmexpression
	| multiplicativeexpression '/' pmexpression
	| multiplicativeexpression '%' pmexpression
;

additiveexpression
:
	multiplicativeexpression
	| additiveexpression '+' multiplicativeexpression
	| additiveexpression '-' multiplicativeexpression
;

shiftexpression
:
	additiveexpression
	| shiftexpression '<<' additiveexpression
	| shiftexpression rightShift additiveexpression
;

// used in CONDITIONALS
relationalexpression
:
	shiftexpression
	| relationalexpression '<' shiftexpression
	| relationalexpression '>' shiftexpression
	| relationalexpression '<=' shiftexpression
	| relationalexpression '>=' shiftexpression
;

// used in CONDITIONALS
equalityexpression
:
	relationalexpression
	| equalityexpression '==' relationalexpression
	| equalityexpression '!=' relationalexpression
;

andexpression
:
	equalityexpression
	| andexpression '&' equalityexpression
;

exclusiveorexpression
:
	andexpression
	| exclusiveorexpression '^' andexpression
;

inclusiveorexpression
:
	exclusiveorexpression
	| inclusiveorexpression '|' exclusiveorexpression
;

logicalandexpression
:
	inclusiveorexpression
	| logicalandexpression '&&' inclusiveorexpression
;

logicalorexpression
:
	logicalandexpression
	| logicalorexpression '||' logicalandexpression
;

// used in CONDITIONALS
ternaryconditionalexpression
:
    logicalorexpression '?' expression ':' assignmentexpression
;

// used in CONDITIONALS
unaryconditionalexpression
:
    logicalorexpression '?' ':' assignmentexpression
;

assignmentexpression
:
	logicalorexpression
    | ternaryconditionalexpression
    | unaryconditionalexpression
	| logicalorexpression assignmentoperator initializerclause
	| Throw assignmentexpression?
;

// used in ASSIGNMENTS
assignmentoperator
:
	'='
	| '*='
	| '/='
	| '%='
	| '+='
	| '-='
	| rightShiftAssign
	| '<<='
	| '&='
	| '^='
	| '|='
;

expression
:
	assignmentexpression
	| expression ',' assignmentexpression
;

constantexpression
:
	logicalorexpression
    | ternaryconditionalexpression
    | unaryconditionalexpression
;
/*Statements*/
statement
:
	attributespecifierseq? Identifier ':' statement
    | attributespecifierseq? casestatement
    | attributespecifierseq? defaultstatement
	| attributespecifierseq? expression? ';'
	| attributespecifierseq? '{' statementseq? '}'
	| attributespecifierseq? selectionstatement
	| attributespecifierseq? iterationstatement
	| attributespecifierseq? jumpstatement
    | attributespecifierseq? Using Namespace nestednamespecifier? Identifier ';'
    | attributespecifierseq declspecifierseq? initdeclaratorlist ';'
	| attributespecifierseq? tryblock
	| declspecifierseq? initdeclaratorlist? ';'
    | Asm '(' Stringliteral ')' ';'
    | Namespace Identifier '=' nestednamespecifier? Identifier ';'
    | Using Typename? nestednamespecifier unqualifiedid ';'
    | Using '::' unqualifiedid ';'
    | Using Identifier attributespecifierseq? '=' typespecifierseq abstractdeclarator? ';'
    | Static_assert '(' constantexpression ',' Stringliteral ')' ';'
    | enumkey attributespecifierseq? Identifier (':' typespecifierseq)? ';'
;

// used in CONDITIONALS
casestatement
:
    Case constantexpression ':' statement
;

// used in CONDITIONALS
defaultstatement
:
    Default ':' statement
;

statementseq
:
	statement
	| statementseq statement
;

selectionstatement
:
	If '(' condition ')' statement
	| If '(' condition ')' statement elsestatement
	| Switch '(' condition ')' statement
;

// used in CONDITIONALS
elsestatement
:
    Else statement
;

condition
:
	expression
	| attributespecifierseq? declspecifierseq declarator '=' initializerclause
	| attributespecifierseq? declspecifierseq declarator bracedinitlist
;

iterationstatement
:
	While '(' condition ')' statement
	| Do statement While '(' expression ')' ';'
	| For '(' forinitstatement condition? ';' expression? ')' statement
	| For '(' attributespecifierseq? declspecifierseq declarator ':' forrangeinitializer ')' statement
;

forinitstatement
:
	expression? ';'
	| declspecifierseq? initdeclaratorlist? ';'
    | attributespecifierseq declspecifierseq? initdeclaratorlist ';'
;

forrangeinitializer
:
	expression
	| bracedinitlist
;

jumpstatement
:
	Break ';'
	| Continue ';'
	| Return expression? ';'
	| Return bracedinitlist ';'
	| gotostatement
;

// used in BRANCHES
gotostatement
:
    Goto Identifier ';'
;

/*Declarations*/
declarationseq
:
	declaration
	| declarationseq declaration
;

declaration
:
	declspecifierseq? initdeclaratorlist? ';'
	| attributespecifierseq ';'
    | attributespecifierseq declspecifierseq? initdeclaratorlist ';'
    | attributespecifierseq? Using Namespace nestednamespecifier? Identifier ';'
    | Asm '(' Stringliteral ')' ';'
    | Namespace Identifier '=' nestednamespecifier? Identifier ';'
    | Using '::' unqualifiedid ';'
    | Using Typename? nestednamespecifier unqualifiedid ';'
    | Using Identifier attributespecifierseq? '=' typespecifierseq abstractdeclarator? ';'
    | Static_assert '(' constantexpression ',' Stringliteral ')' ';'
    | enumkey attributespecifierseq? Identifier (':' typespecifierseq)? ';'
	| functiondefinition
	| Template '<' templateparameterlist '>' declaration
	| Extern? Template declaration
	| Template '<' '>' declaration
	| Extern Stringliteral '{' declarationseq? '}'
    | Extern Stringliteral declaration
	| Inline? Namespace Identifier '{' declarationseq? '}'
    | Inline? Namespace '{' declarationseq? '}'
	| ';'
;

declspecifier
:
	Register
    | Static
    | Thread_local
    | Extern
    | Mutable
	| typespecifier
	| Inline
    | Virtual
    | Explicit
	| Friend
	| Typedef
	| Constexpr
;

declspecifierseq
:
	declspecifier attributespecifierseq?
	| declspecifier declspecifierseq
;

typespecifier
:
	trailingtypespecifier
	| classhead '{' memberspecification? '}'
	| enumhead '{' enumeratorlist? '}'
    | enumhead '{' enumeratorlist ',' '}'
;

trailingtypespecifier
:
	simpletypespecifier
	| classkey attributespecifierseq? nestednamespecifier? Identifier
    | classkey Identifier '<' templateargumentlist? '>'
    | classkey nestednamespecifier Template? Identifier '<' templateargumentlist? '>'
    | Enum nestednamespecifier? Identifier
	| typenamespecifier
	| cvqualifier
;

typespecifierseq
:
	typespecifier attributespecifierseq?
	| typespecifier typespecifierseq
;

trailingtypespecifierseq
:
	trailingtypespecifier attributespecifierseq?
	| trailingtypespecifier trailingtypespecifierseq
;

simpletypespecifier
:
	nestednamespecifier? thetypename
	| nestednamespecifier Template Identifier '<' templateargumentlist? '>'
	| Char
	| Char16
	| Char32
	| Wchar
	| Bool
	| Short
	| Int
	| Long
	| Signed
	| Unsigned
	| Float
	| Double
	| Void
	| Auto
	| decltypespecifier
;

thetypename
:
	classname
	| Identifier
	| Identifier '<' templateargumentlist? '>'
;

decltypespecifier
:
	Decltype '(' expression ')'
	| Decltype '(' Auto ')'
;

enumhead
:
	enumkey attributespecifierseq? Identifier? (':' typespecifierseq)?
	| enumkey attributespecifierseq? nestednamespecifier Identifier (':' typespecifierseq)?
;

enumkey
:
	Enum
	| Enum Class
	| Enum Struct
;

enumeratorlist
:
	enumeratordefinition
	| enumeratorlist ',' enumeratordefinition
;

enumeratordefinition
:
	Identifier
	| Identifier '=' constantexpression
;

attributespecifierseq
:
	attributespecifier
	| attributespecifierseq attributespecifier
;

attributespecifier
:
	'[' '[' attributelist ']' ']'
	| Alignas '(' typespecifierseq abstractdeclarator? '...'? ')'
    | Alignas '(' constantexpression '...'? ')'
;

attributelist
:
	attribute?
	| attributelist ',' attribute?
	| attribute '...'
	| attributelist ',' attribute '...'
;

attribute
:
	attributetoken ('(' balancedtokenseq ')')?
;

attributetoken
:
	Identifier
	| Identifier '::' Identifier
;

balancedtokenseq
:
	balancedtoken?
	| balancedtokenseq balancedtoken
;

balancedtoken
:
	'(' balancedtokenseq ')'
	| '[' balancedtokenseq ']'
	| '{' balancedtokenseq '}'
	/*any token other than a parenthesis , a bracket , or a brace*/
;

/*Declarators*/
initdeclaratorlist
:
	declarator initializer?
	| initdeclaratorlist ',' declarator initializer?
;

declarator
:
	ptrdeclarator
	| noptrdeclarator parametersandqualifiers '->' trailingtypespecifierseq abstractdeclarator?
;

ptrdeclarator
:
	noptrdeclarator
	| ptroperator ptrdeclarator
;

noptrdeclarator
:
	'...'? idexpression attributespecifierseq?
	| noptrdeclarator parametersandqualifiers
	| noptrdeclarator '[' constantexpression? ']' attributespecifierseq?
	| '(' ptrdeclarator ')'
;

parametersandqualifiers
:
	'(' parameterdeclarationclause ')' cvqualifierseq? refqualifier?
	exceptionspecification? attributespecifierseq?
;

ptroperator
:
	'*' attributespecifierseq? cvqualifierseq?
	| '&' attributespecifierseq?
	| '&&' attributespecifierseq?
	| nestednamespecifier '*' attributespecifierseq? cvqualifierseq?
;

cvqualifierseq
:
	cvqualifier cvqualifierseq?
;

cvqualifier
:
	Const
	| Volatile
;

refqualifier
:
	'&'
	| '&&'
;

abstractdeclarator
:
	ptrabstractdeclarator
	| noptrabstractdeclarator? parametersandqualifiers '->' trailingtypespecifierseq abstractdeclarator?
	| abstractpackdeclarator
;

ptrabstractdeclarator
:
	noptrabstractdeclarator
	| ptroperator ptrabstractdeclarator?
;

noptrabstractdeclarator
:
	noptrabstractdeclarator parametersandqualifiers
	| parametersandqualifiers
	| noptrabstractdeclarator '[' constantexpression? ']' attributespecifierseq?
	| '[' constantexpression? ']' attributespecifierseq?
	| '(' ptrabstractdeclarator ')'
;

abstractpackdeclarator
:
	noptrabstractpackdeclarator
	| ptroperator abstractpackdeclarator
;

noptrabstractpackdeclarator
:
	noptrabstractpackdeclarator parametersandqualifiers
	| noptrabstractpackdeclarator '[' constantexpression? ']'
	attributespecifierseq?
	| '...'
;

parameterdeclarationclause
:
	parameterdeclarationlist? '...'?
	| parameterdeclarationlist ',' '...'
;

parameterdeclarationlist
:
	parameterdeclaration
	| parameterdeclarationlist ',' parameterdeclaration
;

parameterdeclaration
:
	attributespecifierseq? declspecifierseq declarator
	| attributespecifierseq? declspecifierseq declarator '=' initializerclause
	| attributespecifierseq? declspecifierseq abstractdeclarator?
	| attributespecifierseq? declspecifierseq abstractdeclarator? '='
	initializerclause
;

functiondefinition
:
	attributespecifierseq? declspecifierseq? declarator virtspecifierseq?
	functionbody
;

functionbody
:
	(':' meminitializerlist)? '{' statementseq? '}'
	| Try (':' meminitializerlist)? '{' statementseq? '}' handlerseq
	| '=' Default ';'
	| '=' Delete ';'
;

// used in ASSIGNMENTS
initializer
:
	braceorequalinitializer
	| '(' initializerlist ')'
;

braceorequalinitializer
:
	'=' initializerclause
	| bracedinitlist
;

initializerclause
:
	assignmentexpression
	| bracedinitlist
;

initializerlist
:
	initializerclause '...'?
	| initializerlist ',' initializerclause '...'?
;

bracedinitlist
:
	'{' initializerlist ','? '}'
	| '{' '}'
;

/*Classes*/
classname
:
	Identifier
	| Identifier '<' templateargumentlist? '>'
;

classhead
:
	classkey attributespecifierseq? nestednamespecifier? classname Final? (':' basespecifierlist)?
	| classkey attributespecifierseq? (':' basespecifierlist)?
;

classkey
:
	Class
	| Struct
	| Union
;

memberspecification
:
	memberdeclaration memberspecification?
	| accessspecifier ':' memberspecification?
;

memberdeclaration
:
	attributespecifierseq? declspecifierseq? memberdeclaratorlist? ';'
	| functiondefinition
	| Using Typename? nestednamespecifier unqualifiedid ';'
    | Using '::' unqualifiedid ';'
	| Static_assert '(' constantexpression ',' Stringliteral ')' ';'
	| Template '<' templateparameterlist '>' declaration
	| Using Identifier attributespecifierseq? '=' typespecifierseq abstractdeclarator? ';'
	| ';'
;

memberdeclaratorlist
:
	memberdeclarator
	| memberdeclaratorlist ',' memberdeclarator
;

memberdeclarator
:
	declarator virtspecifierseq? purespecifier?
	| declarator braceorequalinitializer?
	| Identifier? attributespecifierseq? ':' constantexpression
;

virtspecifierseq
:
	virtspecifier
	| virtspecifierseq virtspecifier
;

virtspecifier
:
	Override
	| Final
;

/*
purespecifier:
	'=' '0'//Conflicts with the lexer
 ;
 */
purespecifier
:
	Assign val = Octalliteral
	{if($val.text.compareTo("0")!=0) throw new InputMismatchException(this);}

;

/*Derived classes*/
basespecifierlist
:
	basespecifier '...'?
	| basespecifierlist ',' basespecifier '...'?
;

basespecifier
:
	attributespecifierseq? classordecltype
	| attributespecifierseq? Virtual accessspecifier? classordecltype
	| attributespecifierseq? accessspecifier Virtual? classordecltype
;

classordecltype
:
	nestednamespecifier? classname
	| decltypespecifier
;

accessspecifier
:
	Private
	| Protected
	| Public
;

/*Special member functions*/
conversiondeclarator
:
	ptroperator conversiondeclarator?
;

meminitializerlist
:
	meminitializer '...'?
	| meminitializer '...'? ',' meminitializerlist
;

meminitializer
:
	meminitializerid '(' initializerlist? ')'
	| meminitializerid bracedinitlist
;

meminitializerid
:
	classordecltype
	| Identifier
;

/*Overloading*/
literaloperatorid
:
	Operator Stringliteral Identifier
	| Operator Userdefinedstringliteral
;

/*Templates*/
templateparameterlist
:
	templateparameter
	| templateparameterlist ',' templateparameter
;

templateparameter
:
	Class '...'? Identifier?
    | Class Identifier? '=' typespecifierseq abstractdeclarator?
    | Typename '...'? Identifier?
    | Typename Identifier? '=' typespecifierseq abstractdeclarator?
    | Template '<' templateparameterlist '>' Class '...'? Identifier?
    | Template '<' templateparameterlist '>' Class Identifier? '=' idexpression
	| parameterdeclaration
;

templateargumentlist
:
	templateargument '...'?
	| templateargumentlist ',' templateargument '...'?
;

templateargument
:
	typespecifierseq abstractdeclarator?
	| constantexpression
	| idexpression
;

typenamespecifier
:
	Typename nestednamespecifier Identifier
	| Typename nestednamespecifier Template? Identifier '<' templateargumentlist? '>'
;

/*Exception handling*/
// used in CONDITIONALS
tryblock
:
	Try '{' statementseq? '}' handlerseq
;

handlerseq
:
	handler handlerseq?
;

// used in CONDITIONALS
handler
:
	Catch '(' exceptiondeclaration ')' '{' statementseq? '}'
;

exceptiondeclaration
:
	attributespecifierseq? typespecifierseq declarator
	| attributespecifierseq? typespecifierseq abstractdeclarator?
	| '...'
;

exceptionspecification
:
	Throw '(' typeidlist? ')'
	| Noexcept '(' constantexpression ')'
    | Noexcept
;

typeidlist
:
	typespecifierseq abstractdeclarator? '...'?
	| typeidlist ',' typespecifierseq abstractdeclarator? '...'?
;

/*Preprocessing directives*/

MultiLineMacro
:
    '#' (~[\n]*? '\\' '\r'? '\n')+ ~[\n]+ -> channel(HIDDEN)
;

Directive
:
    '#' ~[\n]* -> channel(HIDDEN)
;

/*Lexer*/

/*Keywords*/
Alignas
:
	'alignas'
;

Alignof
:
	'alignof'
;

Asm
:
	'asm'
;

Auto
:
	'auto'
;

Bool
:
	'bool'
;

Break
:
	'break'
;

Case
:
	'case'
;

Catch
:
	'catch'
;

Char
:
	'char'
;

Char16
:
	'char16_t'
;

Char32
:
	'char32_t'
;

Class
:
	'class'
;

Const
:
	'const'
;

Constexpr
:
	'constexpr'
;

Const_cast
:
	'const_cast'
;

Continue
:
	'continue'
;

Decltype
:
	'decltype'
;

Default
:
	'default'
;

Delete
:
	'delete'
;

Do
:
	'do'
;

Double
:
	'double'
;

Dynamic_cast
:
	'dynamic_cast'
;

Else
:
	'else'
;

Enum
:
	'enum'
;

Explicit
:
	'explicit'
;

Export
:
	'export'
;

Extern
:
	'extern'
;

FalseToken
:
	'false'
;

Final
:
	'final'
;

Float
:
	'float'
;

For
:
	'for'
;

Friend
:
	'friend'
;

Goto
:
	'goto'
;

If
:
	'if'
;

Inline
:
	'inline'
;

Int
:
	'int'
;

Long
:
	'long'
;

Mutable
:
	'mutable'
;

Namespace
:
	'namespace'
;

New
:
	'new'
;

Noexcept
:
	'noexcept'
;

Nullptr
:
	'nullptr'
;

Operator
:
	'operator'
;

Override
:
	'override'
;

Private
:
	'private'
;

Protected
:
	'protected'
;

Public
:
	'public'
;

Register
:
	'register'
;

Reinterpret_cast
:
	'reinterpret_cast'
;

Return
:
	'return'
;

Short
:
	'short'
;

Signed
:
	'signed'
;

Sizeof
:
	'sizeof'
;

Static
:
	'static'
;

Static_assert
:
	'static_assert'
;

Static_cast
:
	'static_cast'
;

Struct
:
	'struct'
;

Switch
:
	'switch'
;

Template
:
	'template'
;

This
:
	'this'
;

Thread_local
:
	'thread_local'
;

Throw
:
	'throw'
;

TrueToken
:
	'true'
;

Try
:
	'try'
;

Typedef
:
	'typedef'
;

Typeid
:
	'typeid'
;

Typename
:
	'typename'
;

Union
:
	'union'
;

Unsigned
:
	'unsigned'
;

Using
:
	'using'
;

Virtual
:
	'virtual'
;

Void
:
	'void'
;

Volatile
:
	'volatile'
;

Wchar
:
	'wchar_t'
;

While
:
	'while'
;

/*Operators*/
LeftParen
:
	'('
;

RightParen
:
	')'
;

LeftBracket
:
	'['
;

RightBracket
:
	']'
;

LeftBrace
:
	'{'
;

RightBrace
:
	'}'
;

Plus
:
	'+'
;

Minus
:
	'-'
;

Star
:
	'*'
;

Div
:
	'/'
;

Mod
:
	'%'
;

Caret
:
	'^'
;

And
:
	'&'
;

Or
:
	'|'
;

Tilde
:
	'~'
;

Not
:
	'!'
;

Assign
:
	'='
;

Less
:
	'<'
;

Greater
:
	'>'
;

PlusAssign
:
	'+='
;

MinusAssign
:
	'-='
;

StarAssign
:
	'*='
;

DivAssign
:
	'/='
;

ModAssign
:
	'%='
;

XorAssign
:
	'^='
;

AndAssign
:
	'&='
;

OrAssign
:
	'|='
;

LeftShift
:
	'<<'
;

rightShift
:
//'>>'
	Greater Greater
;

LeftShiftAssign
:
	'<<='
;

rightShiftAssign
:
//'>>='
	Greater Greater Assign
;

Equal
:
	'=='
;

NotEqual
:
	'!='
;

LessEqual
:
	'<='
;

GreaterEqual
:
	'>='
;

AndAnd
:
	'&&'
;

OrOr
:
	'||'
;

PlusPlus
:
	'++'
;

MinusMinus
:
	'--'
;

Comma
:
	','
;

ArrowStar
:
	'->*'
;

Arrow
:
	'->'
;

Question
:
	'?'
;

Colon
:
	':'
;

Doublecolon
:
	'::'
;

Semi
:
	';'
;

Dot
:
	'.'
;

DotStar
:
	'.*'
;

Ellipsis
:
	'...'
;

theoperator
:
	New
	| Delete
	| New '[' ']'
	| Delete '[' ']'
	| '+'
	| '-'
	| '*'
	| '/'
	| '%'
	| '^'
	| '&'
	| '|'
	| '~'
	| '!'
	| '='
	| '<'
	| '>'
	| '+='
	| '-='
	| '*='
	| '/='
	| '%='
	| '^='
	| '&='
	| '|='
	| '<<'
	| rightShift
	| rightShiftAssign
	| '<<='
	| '=='
	| '!='
	| '<='
	| '>='
	| '&&'
	| '||'
	| '++'
	| '--'
	| ','
	| '->*'
	| '->'
	| '(' ')'
	| '[' ']'
;

/*Lexer*/
fragment
Hexquad
:
	HEXADECIMALDIGIT HEXADECIMALDIGIT HEXADECIMALDIGIT HEXADECIMALDIGIT
;

fragment
Universalcharactername
:
	'\\u' Hexquad
	| '\\U' Hexquad Hexquad
;

Identifier
:
/*
	Identifiernondigit
	| Identifier Identifiernondigit
	| Identifier DIGIT
	*/
	Identifiernondigit
	(
		Identifiernondigit
		| DIGIT
	)*
;

fragment
Identifiernondigit
:
	NONDIGIT
	| Universalcharactername
	/* other implementation defined characters*/
;

fragment
NONDIGIT
:
	[a-zA-Z_]
;

fragment
DIGIT
:
	[0-9]
;

Integerliteral
:
	Decimalliteral Integersuffix?
	| Octalliteral Integersuffix?
	| Hexadecimalliteral Integersuffix?
	| Binaryliteral Integersuffix?
;

Decimalliteral
:
	NONZERODIGIT
	(
		'\''? DIGIT
	)*
;

Octalliteral
:
	'0'
	(
		'\''? OCTALDIGIT
	)*
;

Hexadecimalliteral
:
	(
		'0x'
		| '0X'
	) HEXADECIMALDIGIT
	(
		'\''? HEXADECIMALDIGIT
	)*
;

Binaryliteral
:
	(
		'0b'
		| '0B'
	) BINARYDIGIT
	(
		'\''? BINARYDIGIT
	)*
;

fragment
NONZERODIGIT
:
	[1-9]
;

fragment
OCTALDIGIT
:
	[0-7]
;

fragment
HEXADECIMALDIGIT
:
	[0-9a-fA-F]
;

fragment
BINARYDIGIT
:
	[01]
;

Integersuffix
:
	Unsignedsuffix Longsuffix?
	| Unsignedsuffix Longlongsuffix?
	| Longsuffix Unsignedsuffix?
	| Longlongsuffix Unsignedsuffix?
;

fragment
Unsignedsuffix
:
	[uU]
;

fragment
Longsuffix
:
	[lL]
;

fragment
Longlongsuffix
:
	'll'
	| 'LL'
;

Characterliteral
:
	'\'' Cchar+ '\''
	| 'u' '\'' Cchar+ '\''
	| 'U' '\'' Cchar+ '\''
	| 'L' '\'' Cchar+ '\''
;

fragment
Cchar
:
	~['\\\r\n]
	| Escapesequence
	| Universalcharactername
;

fragment
Escapesequence
:
	Simpleescapesequence
	| Octalescapesequence
	| Hexadecimalescapesequence
;

fragment
Simpleescapesequence
:
	'\\\''
	| '\\"'
	| '\\?'
	| '\\\\'
	| '\\a'
	| '\\b'
	| '\\f'
	| '\\n'
	| '\\r'
	| '\\t'
	| '\\v'
;

fragment
Octalescapesequence
:
	'\\' OCTALDIGIT
	| '\\' OCTALDIGIT OCTALDIGIT
	| '\\' OCTALDIGIT OCTALDIGIT OCTALDIGIT
;

fragment
Hexadecimalescapesequence
:
	'\\x' HEXADECIMALDIGIT+
;

Floatingliteral
:
	Fractionalconstant Exponentpart? Floatingsuffix?
	| Digitsequence Exponentpart Floatingsuffix?
;

fragment
Fractionalconstant
:
	Digitsequence? '.' Digitsequence
	| Digitsequence '.'
;

fragment
Exponentpart
:
	'e' SIGN? Digitsequence
	| 'E' SIGN? Digitsequence
;

fragment
SIGN
:
	[+-]
;

fragment
Digitsequence
:
	DIGIT
	(
		'\''? DIGIT
	)*
;

fragment
Floatingsuffix
:
	[flFL]
;

Stringliteral
:
	Encodingprefix? '"' Schar* '"'
	| Encodingprefix? 'R' Rawstring
;

fragment
Encodingprefix
:
	'u8'
	| 'u'
	| 'U'
	| 'L'
;

fragment
Schar
:
	~["\\\r\n]
	| Escapesequence
	| Universalcharactername
;

fragment
Rawstring /* '"' dcharsequence? '(' rcharsequence? ')' dcharsequence? '"' */
:
	'"' .*? '(' .*? ')' .*? '"'
;

Userdefinedintegerliteral
:
	Decimalliteral Udsuffix
	| Octalliteral Udsuffix
	| Hexadecimalliteral Udsuffix
	| Binaryliteral Udsuffix
;

Userdefinedfloatingliteral
:
	Fractionalconstant Exponentpart? Udsuffix
	| Digitsequence Exponentpart Udsuffix
;

Userdefinedstringliteral
:
	Stringliteral Udsuffix
;

Userdefinedcharacterliteral
:
	Characterliteral Udsuffix
;

fragment
Udsuffix
:
	Identifier
;

Whitespace
:
	[ \t]+ -> skip
;

Newline
:
	(
		'\r' '\n'?
		| '\n'
	) -> skip
;

BlockComment
:
	'/*' .*? '*/' -> skip
;

LineComment
:
	'//' ~[\r\n]* -> skip
;