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
	declaration* EOF
;

/*Expressions*/
unqualifiedid
:
	'~'? Identifier ('<' templateargumentlist? '>')?
	| Operator (
	    (theoperator | Stringliteral Identifier | Userdefinedstringliteral) ('<' templateargumentlist? '>')?
	    | typespecifier+ attributespecifier* ptroperator*
	)
	| '~' Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
;

nestednamespecifier
:
	(Identifier ('<' templateargumentlist? '>')? | Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')') '::'
	((Identifier | Template? Identifier '<' templateargumentlist? '>') '::')*
;

lambdadeclarator
:
	'(' ((
            parameterdeclaration (',' parameterdeclaration)*)? '...'?
            | parameterdeclaration (',' parameterdeclaration)* ',' '...'
        ) ')' Mutable? (
	    Throw '(' (typespecifier+ attributespecifier* abstractdeclarator? '...'? (',' typespecifier+ attributespecifier* abstractdeclarator? '...'?)*)? ')'
	    | Noexcept ('(' constantexpression ')')?
	)? attributespecifier* ('->' trailingtypespecifier+ attributespecifier* abstractdeclarator?)?
;


postfix
:
    '[' (
        assignmentexpression (',' assignmentexpression)*
        | '{' (initializerlist ','?)? '}'
    ) ']'
    | '(' initializerlist? ')'
    | ('.' | '->') (
        Template? (nestednamespecifier Template?)? unqualifiedid
        | pseudodestructorname
    )
;

postfixexpression
:
	(
        (
            Numberliteral
            | Characterliteral
            | Stringliteral
            | TrueFalse
            | Nullptr
            | Userdefinedliteral
            | Userdefinedstringliteral
            | This
        )
        | (nestednamespecifier Template?)? unqualifiedid
        | '[' (
            ('&' | '=') (',' ('&'? Identifier initializer? | This) '...'?)*
            | ('&'? Identifier initializer? | This) '...'? (',' ('&'? Identifier initializer? | This) '...'?)*
        )? ']' lambdadeclarator? '{' statement* '}'
        | simpletypespecifier (
            '(' initializerlist? ')'
            | '{' (initializerlist ','?)? '}'
        )
        | Typename nestednamespecifier (
            Identifier
            | Template? Identifier '<' templateargumentlist? '>'
        ) (
            '(' initializerlist? ')'
            | '{' (initializerlist ','?)? '}'
        )
        | (Cast '<' typespecifier+ attributespecifier* abstractdeclarator? '>')? '(' assignmentexpression (',' assignmentexpression)* ')'
        | Typeid (
            '(' assignmentexpression (',' assignmentexpression)* ')'
            | '(' typespecifier+ attributespecifier* abstractdeclarator? ')'
        )
	) postfix*
;

pseudodestructorname
:
	(
	    nestednamespecifier? (Identifier ('<' templateargumentlist? '>')? '::')?
	    | nestednamespecifier Template Identifier '<' templateargumentlist? '>' '::'
	) '~' Identifier ('<' templateargumentlist? '>')?
	| '~' Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
;

unaryexpression
:
	postfixexpression
	| unaryincdecexpression
	| ('|' | '*' | '&' | '+' | '!' | '~' | '-') castexpression
	| Sizeof (
	    unaryexpression
	    | '(' typespecifier+ attributespecifier* abstractdeclarator? ')'
	    | '...' '(' Identifier ')'
	)
	| Alignof '(' typespecifier+ attributespecifier* abstractdeclarator? ')'
	| Noexcept '(' assignmentexpression (',' assignmentexpression)* ')'
	| newexpression
	| deleteexpression
;

// used in ASSIGNMENTS
unaryincdecexpression
:
    ('++' | '--') castexpression
    | postfixunaryincdecexpression
;

postfixunaryincdecexpression
:
    postfixexpression ('++' | '--') | postfixunaryincdecexpression postfix* ('++' | '--')
;

// used in BRANCHES
newexpression
:
	'::'? New ('(' initializerlist ')')? (
	    typespecifier+ attributespecifier* newdeclarator?
	    | '(' typespecifier+ attributespecifier* abstractdeclarator? ')'
	) (
	    '(' initializerlist? ')'
	    | '{' (initializerlist ','?)? '}'
	)?
;

newdeclarator
:
	ptroperator newdeclarator?
	| '[' assignmentexpression (',' assignmentexpression)* ']' attributespecifier*
     ('[' constantexpression ']' attributespecifier*)*
;

// used in BRANCHES
deleteexpression
:
	'::'? Delete ('[' ']')? castexpression
;

castexpression
:
	('(' typespecifier+ attributespecifier* abstractdeclarator? ')')* unaryexpression
;

shiftexpression
:
    castexpression (('.*' | '->*' | '*' | '/' | '%' | '+' | '-' | '<<' | Greater Greater ) castexpression)*
;

// used in CONDITIONALS
relationalexpression
:
	shiftexpression	| relationalexpression ('<' | '>' | '<=' | '>=') shiftexpression
;

// used in CONDITIONALS
equalityexpression
:
	relationalexpression | equalityexpression ('==' | '!=') relationalexpression
;

// used in CONDITIONALS
ternaryconditionalexpression
:
    equalityexpression (('&' | '&&' | '^' | '|' | '||') equalityexpression)* '?' assignmentexpression (',' assignmentexpression)* ':' assignmentexpression
;

// used in CONDITIONALS
unaryconditionalexpression
:
    equalityexpression (('&' | '&&' | '^' | '|' | '||') equalityexpression)* '?:' assignmentexpression
;

assignmentexpression
:
	equalityexpression (('&' | '&&' | '^' | '|' | '||') equalityexpression)* (assignmentoperator (
	    assignmentexpression
	    | '{' (initializerlist ','?)? '}'
	))?
    | ternaryconditionalexpression
    | unaryconditionalexpression
	| Throw assignmentexpression?
;

// used in ASSIGNMENTS
assignmentoperator
:
	(
        '='
        | '*='
        | '/='
        | '%='
        | '+='
        | '-='
        | '<<='
        | '&='
        | '^='
        | '|='
	)
	| Greater Greater Assign
;

constantexpression
:
	equalityexpression (('&' | '&&' | '^' | '|' | '||') equalityexpression)*
    | ternaryconditionalexpression
    | unaryconditionalexpression
;
/*Statements*/
statement
:
	attributespecifier* (
	    (Identifier ':' | (Switch | While) '(' condition ')') statement
        | casestatement
        | (assignmentexpression (',' assignmentexpression)*)? ';'
        | '{' statement* '}'
        | If '(' condition ')' statement elsestatement?
        | Do statement While '(' assignmentexpression (',' assignmentexpression)* ')' ';'
        | For ('(' (
            forinitstatement condition? ';' (assignmentexpression (',' assignmentexpression)*)?
            | attributespecifier* declspecifierseq declarator ':' (
                assignmentexpression (',' assignmentexpression)*
                | '{' (initializerlist ','?)? '}'
            )
        ) ')' statement)
        | (Break | Continue) ';'
        | Return (
            (assignmentexpression (',' assignmentexpression)*)?
            | '{' (initializerlist ','?)? '}'
        ) ';'
        | gotostatement
        | Using Namespace nestednamespecifier? Identifier ';'
        | tryblock
	)
	| attributespecifier+ declspecifierseq? declarator initializer? (',' declarator initializer?)* ';'
	| declspecifierseq? (declarator initializer? (',' declarator initializer?)*)? ';'
    | Asm '(' Stringliteral ')' ';'
    | Namespace Identifier '=' nestednamespecifier? Identifier ';'
    | Using (
        ('::' | Typename? nestednamespecifier) unqualifiedid
        | Identifier attributespecifier* '=' typespecifier+ attributespecifier* abstractdeclarator?
    ) ';'
    | Static_assert '(' constantexpression ',' Stringliteral ')' ';'
    | Enum (Class | Struct)? attributespecifier* Identifier (':' typespecifier+ attributespecifier*)? ';'
;

// used in CONDITIONALS
casestatement
:
    (Case constantexpression | Default) ':' statement
;

// used in CONDITIONALS
elsestatement
:
    Else statement
;

condition
:
	assignmentexpression (',' assignmentexpression)*
	| attributespecifier* declspecifierseq declarator (
	    '=' assignmentexpression
	    | '='? '{' (initializerlist ','?)? '}'
	)
;

forinitstatement
:
	(
	    (assignmentexpression (',' assignmentexpression)*)?
	    | declspecifierseq? (declarator initializer? (',' declarator initializer?)*)?
        | attributespecifier+ declspecifierseq? declarator initializer? (',' declarator initializer?)*
    ) ';'
;

// used in BRANCHES
gotostatement
:
    Goto Identifier ';'
;

/*Declarations*/
declaration
:
	declspecifierseq? (declarator initializer? (',' declarator initializer?)*)? ';'
	| attributespecifier+ (declspecifierseq? declarator initializer? (',' declarator initializer?)*)? ';'
    | attributespecifier* (
        Using Namespace nestednamespecifier? Identifier ';'
        | declspecifierseq? declarator (Override | Final)* (
            (':' meminitializerlist)? '{' statement* '}'
            | Try (':' meminitializerlist)? '{' statement* '}' handler+
            | '=' (Default | Delete) ';'
        )
    )
    | Asm '(' Stringliteral ')' ';'
    | Namespace Identifier '=' nestednamespecifier? Identifier ';'
    | Using (
        ('::' | Typename? nestednamespecifier) unqualifiedid
        | Identifier attributespecifier* '=' typespecifier+ attributespecifier* abstractdeclarator?
    ) ';'
    | Static_assert '(' constantexpression ',' Stringliteral ')' ';'
    | Enum (Class | Struct)? attributespecifier* Identifier (':' typespecifier+ attributespecifier*)? ';'
	| (Template '<' templateparameterlist? '>' | Extern? Template) declaration
	| Extern Stringliteral ('{' declaration* '}' | declaration)
	| Inline? Namespace Identifier? '{' declaration* '}'
	| ';'
;

declspecifierseq
:
	(
	    (
             Specifier
             | Mutable
             | Extern
             | Virtual
             | Inline
        )
        | typespecifier
	)+ attributespecifier*
;

typespecifier
:
	trailingtypespecifier
	| (Class | Struct | Union) attributespecifier* (nestednamespecifier? Identifier ('<' templateargumentlist? '>')? Final?)?
	    (':' basespecifier '...'? (',' basespecifier '...'?)*)? '{' (memberdeclaration | PrivateProtectedPublic ':')? '}'
	| Enum (Class | Struct)? attributespecifier* (nestednamespecifier? Identifier)? (':' typespecifier+ attributespecifier*)?
	    '{' Identifier ('=' constantexpression)? (',' Identifier ('=' constantexpression)?)*? ','? '}'
;

trailingtypespecifier
:
	simpletypespecifier
	| (Class | Struct | Union) (
	    attributespecifier* nestednamespecifier? Identifier
        | (nestednamespecifier Template?)? Identifier '<' templateargumentlist? '>'
    )
    | Enum nestednamespecifier? Identifier
	| Typename nestednamespecifier (
	    Identifier
	    | Template? Identifier '<' templateargumentlist? '>'
	)
	| ConstOrVolatile
;

simpletypespecifier
:
	nestednamespecifier? Identifier ('<' templateargumentlist? '>')?
	| nestednamespecifier Template Identifier '<' templateargumentlist? '>'
	| (
        Types
        | SignedUnsigned
        | Auto
	)
	| Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
;

attributespecifier
:
	'[' '[' (Identifier ('::' Identifier)? ('(' balancedtoken* ')')? '...'?)?
	   (',' (Identifier ('::' Identifier)? ('(' balancedtoken* ')')? '...'?)?)* ']' ']'
	| Alignas '(' (
	    typespecifier+ attributespecifier* abstractdeclarator?
	    | constantexpression
	) '...'? ')'
;

balancedtoken
:
	  '(' balancedtoken* ')'
	| '[' balancedtoken* ']'
	| '{' balancedtoken* '}'
	/*any token other than a parenthesis , a bracket , or a brace*/
;

/*Declarators*/
declarator
:
	ptroperator* noptrdeclarator
	| noptrdeclarator parametersandqualifiers '->' trailingtypespecifier+ attributespecifier* abstractdeclarator?
;

noptrdeclarator
:
	'...'? (nestednamespecifier Template?)? unqualifiedid attributespecifier*
	| noptrdeclarator (
	    parametersandqualifiers
	    | '[' constantexpression? ']' attributespecifier*
	)
	| '(' ptroperator* noptrdeclarator ')'
;

parametersandqualifiers
:
	'(' (
	    (parameterdeclaration (',' parameterdeclaration)*)? '...'?
	    | parameterdeclaration (',' parameterdeclaration)* ',' '...'
	) ')' ConstOrVolatile* ('&' | '&&')? (
        Throw '(' (typespecifier+ attributespecifier* abstractdeclarator? '...'? (
            ',' typespecifier+ attributespecifier* abstractdeclarator? '...'?
        )*)? ')'
	    | Noexcept ('(' constantexpression ')')?
	)? attributespecifier*
;

ptroperator
:
	nestednamespecifier? '*' attributespecifier* ConstOrVolatile*
	| ('&' | '&&') attributespecifier*
;

abstractdeclarator
:
	(noptrabstractdeclarator? parametersandqualifiers '->' trailingtypespecifier+ attributespecifier*)*
	ptroperator* (
	    noptrabstractdeclarator
	    | '...' (
	        parametersandqualifiers
	        | '[' constantexpression? ']' attributespecifier*
	    )*
	)
;

noptrabstractdeclarator
:
	noptrabstractdeclarator (
	    parametersandqualifiers
	    | '[' constantexpression? ']' attributespecifier*
	)
	| parametersandqualifiers
	| '[' constantexpression? ']' attributespecifier*
	| '(' ptroperator* noptrabstractdeclarator ')'
;

parameterdeclaration
:
	attributespecifier* declspecifierseq (
	    declarator
	    | abstractdeclarator
	) ('=' (
	    assignmentexpression
	    | '{' (initializerlist ','?)? '}'
	))?
;

// used in ASSIGNMENTS
initializer
:
	'=' assignmentexpression
    | '='? '{' (initializerlist ','?)? '}'
	| '(' initializerlist ')'
;

initializerlist
:
	(
	    assignmentexpression
	    | '{' (initializerlist ','?)? '}'
	) '...'? (',' (
	    assignmentexpression
	    | '{' (initializerlist ','?)? '}'
	) '...'?)*
;

/*Classes*/
memberdeclaration
:
	attributespecifier* declspecifierseq? (
	    (memberdeclarator (',' memberdeclarator)*)? ';'
	    | declarator (Override | Final)* (
      	    (':' meminitializerlist)? '{' statement* '}'
            | Try (':' meminitializerlist)? '{' statement* '}' handler+
            | '=' (Default | Delete) ';'
        )
    )
	| Using (Typename? nestednamespecifier | '::') unqualifiedid ';'
	| Static_assert '(' constantexpression ',' Stringliteral ')' ';'
	| Template '<' templateparameterlist '>' declaration
	| Using Identifier attributespecifier* '=' typespecifier+ attributespecifier* abstractdeclarator? ';'
	| ';'
;

memberdeclarator
:
	declarator (
        (Override | Final)* purespecifier?
        | (
            '=' assignmentexpression
            | '='? '{' (initializerlist ','?)? '}'
        )?
    )
	| Identifier? attributespecifier* ':' constantexpression
;

/*
purespecifier:
	'=' '0'//Conflicts with the lexer
 ;
 */
purespecifier
:
	Assign val = Octalliteral
	{if $val.text.compareTo('0') != 0:
    raise InputMismatchException(self)}

;

/*Derived classes*/
basespecifier
:
	attributespecifier* (
	    Virtual PrivateProtectedPublic?
	    | PrivateProtectedPublic Virtual?
	)? (
	    nestednamespecifier? Identifier ('<' templateargumentlist? '>')?
	    | Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
	)
;

/*Special member functions*/
meminitializerlist
:
	(
	    nestednamespecifier? Identifier ('<' templateargumentlist? '>')?
	    | Decltype '(' (assignmentexpression (',' assignmentexpression)* | Auto) ')'
	    | Identifier
	) (
	    '(' initializerlist? ')'
	    | '{' (initializerlist ','?)? '}'
	) '...'? (',' meminitializerlist)?
;

/*Templates*/
templateparameterlist
:
	(
	    (Class | Typename) (
	        '...'? Identifier?
	        | Identifier? '=' typespecifier+ attributespecifier* abstractdeclarator?
	    )
        | Template '<' templateparameterlist '>' Class (
            '...'? Identifier?
            | Identifier? '=' (nestednamespecifier Template?)? unqualifiedid
        )
        | parameterdeclaration
    )
	(',' (
	    (Class | Typename) (
	        '...'? Identifier?
	        | Identifier? '=' typespecifier+ attributespecifier* abstractdeclarator?
	    )
        | Template '<' templateparameterlist '>' Class (
            '...'? Identifier?
            | Identifier? '=' (nestednamespecifier Template?)? unqualifiedid
        )
        | parameterdeclaration
    ))*
;

templateargumentlist
:
	(
	    typespecifier+ attributespecifier* abstractdeclarator?
	    | constantexpression
	    | (nestednamespecifier Template?)? unqualifiedid
	) '...'? (',' (
        typespecifier+ attributespecifier* abstractdeclarator?
        | constantexpression
        | (nestednamespecifier Template?)? unqualifiedid
	) '...'?)*
;

/*Exception handling*/
// used in CONDITIONALS
tryblock
:
	Try '{' statement* '}' handler+
;

// used in CONDITIONALS
handler
:
	Catch '(' (
	    attributespecifier* typespecifier+ attributespecifier* (
	        declarator
	        | abstractdeclarator?
	    )
	    | '...'
	) ')' '{' statement* '}'
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

Class
:
	'class'
;

ConstOrVolatile
:
	'const' | 'volatile'
;

Cast
:
	'const_cast'
	| 'reinterpret_cast'
    | 'static_cast'
    | 'dynamic_cast'
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

Else
:
	'else'
;

Enum
:
	'enum'
;

Export
:
	'export'
;

Extern
:
	'extern'
;

TrueFalse
:
	'true' | 'false'
;

Final
:
	'final'
;

For
:
	'for'
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

Types
:
	'int'
	| 'long'
	| 'short'
	| 'double'
	| 'float'
	| 'bool'
	| 'wchar_t'
    | 'char16_t'
    | 'char32_t'
    | 'char'
    | 'void'
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

PrivateProtectedPublic
:
    'private'| 'protected' | 'public'
;

Specifier
:
	'register'
    | 'static'
    | 'thread_local'
    | 'explicit'
    | 'friend'
    | 'typedef'
    | 'constexpr'
;

Return
:
	'return'
;

SignedUnsigned
:
	'signed' | 'unsigned'
;

Sizeof
:
	'sizeof'
;

Static_assert
:
	'static_assert'
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

Using
:
	'using'
;

Virtual
:
	'virtual'
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


LeftShiftAssign
:
	'<<='
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

UnaryCondition
:
    '?:'
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
	(
        New
        | Delete
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
        | '?:'
	)
	| New '[' ']'
	| Delete '[' ']'
	| Greater Greater Assign?
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

Numberliteral
:
	(
	    Decimalliteral
        | Octalliteral
        | Hexadecimalliteral
        | Binaryliteral
	) Integersuffix?
	| Fractionalconstant Exponentpart? Floatingsuffix?
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

Decimalliteral
:
	NONZERODIGIT ('\''? DIGIT)*
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
	Unsignedsuffix (Longsuffix | Longlongsuffix)?
	| (Longsuffix | Longlongsuffix) Unsignedsuffix?
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

Userdefinedliteral
:
	(
        Decimalliteral
        | Octalliteral
        | Hexadecimalliteral
        | Binaryliteral
        | Fractionalconstant Exponentpart?
        | Digitsequence Exponentpart
        | Characterliteral
	) Udsuffix
;

Userdefinedstringliteral
:
	Stringliteral Udsuffix
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
