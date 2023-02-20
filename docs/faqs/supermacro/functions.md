# Functions

## Syntax
!!! note

    Use a `:` between the command name and the arguments

`{{ "{{FUNC:NameOfFunction:OutputVariable:InputParam1:InputParam2:InputParam3...}}" }}`

Where `InputParamX` can either be text (`10`) or another variable (`$MyVar`)

**Drill-Down of syntax:**

1. All functions always start with the FUNC keyword.
2. The 2nd argument would be the name of the function (see column 1 in table below).
3. The 3rd argument would be the return variable (i.e. the variable which will hold the result of the function). **Note:** No $ is needed here.
4. Arguments 4 and up are the input needed for the function. Each function has a different number of Input arguments (as stated in column 2 in the table below).

    !!! note

        To differentiate between regular text and variables, start with a $ if you're referring to a variable

## Supported Functions
|Function Name|Number of Input arguments|Example|Comments|
|----|----|----|----|
|ADD|2|`{{ "{{FUNC:ADD:MyVar:10:20}}" }}` (10+20 and store in MyVar)<br>`{{ "{{FUNC:ADD:Var1:10:$Var2}}" }}` (Add 10 to Var2 and store in Var1)<br>`{{ "{{FUNC:ADD:Result:$Var1:$Var2}}" }}` (Sum Var1 and Var2 and store in Result)|
|SUB|2|`{{ "{{FUNC:SUB:MyVar:20:10}}" }}` (20-10 and store in MyVar)|(Additional examples similar to ADD above)|
|MUL|2|`{{ "{{FUNC:MUL:MyVar:10:20}}" }}` (10*20 and store in MyVar)|(Additional examples similar to ADD above)|
|DIV|2|`{{ "{{FUNC:DIV:MyVar:​100:50}}" }}` (100/50 and store in MyVar).|(Additional examples similar to ADD above)|
|RANDOM|2|`{{ "{{FUNC:RANDOM:MyVar:1:20}}" }}` (Find a random number between 1 (inclusive) and 20 (exclusive) and store in MyVar.<br>`{{ "{{FUNC:RANDOM:MyVar:$FirstVal:$SecondVal}}" }}` (Find a random number between FirstVal variable (inclusive) and SecondVal variable (exclusive) and store in MyVar.<br>**Note:** First value must be LOWER than Second value.|
|CONCAT|Unlimited|`{{ "{{FUNC:CONCAT:MyVar:Hello:World:$Var1:Hi:$Var2}}" }}`<br>MyVar will have the string: HelloWorldXXXXHiYYYY Where XXXX is the contents of Var1 and YYYY is the contents of Var2|
|REPLACE|3|`{{ "{{FUNC:REPLACE:MyVar:Hello:He:Y}}" }}`<br>MyVar will have the string: *Yello*<br>`{{ "{{VARSET:XX:Hello World}}" }} {{ "{{VARSET:A:l}}" }}{{ "{{VARSET:B:Z}}" }} {{ "{{FUNC:REPLACE:MyVar:$XX:$A:$B}}" }}`<br>MyVar will have the string: *HeZZo WorZd*|
|NOW|1|`{{ "{{FUNC:NOW:MyVar:yyyy-MM-dd HH:mm:ss}}" }}`<br>MyVar will have the current date and time.|
|LEN|1|`{{ "{{FUNC:LEN:MyVar:Hello World}}" }}` (Length of the string 'Hello World')<br>MyVar will have the value 11|
|MID|(Arguments: 1. 0-Based Start Position 2. [Optional] Length)|`{{ "{{FUNC:MID:RES:Hello:2}}" }}` RES will have llo<br>`{{ "{{FUNC:MID:RES:Hello:0:2}}" }}` RES will have He|
|REVERSE|1|`{{ "{{FUNC:REVERSE:MyVar:Hello World}}" }}`<br>MyVar will have the value: dlroW olleH|
|INDEXOF|2|Returns the first 0-based position of a text in the string.<br>`{{ "{{FUNC:INDEXOF:RES:Hello:e}}" }}` will return 1 into RES (since e has an index of 1 in the string)|
