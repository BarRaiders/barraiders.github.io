---
title: SuperMacro - Functions
description: Learn how to use functions in the SuperMacro plugin for the Stream Deck. Do mathematical calculations, replace text, get current date and more with functions to make ur SuperMacro's even more advanced.
---


# SuperMacro - Functions

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

### Math Functions
|Function Name|Number of Input arguments|Example|Comments|
|----|----|----|----|
|ADD|2|`{{ "{{FUNC:ADD:MyVar:10:20}}" }}` (10+20 and store in MyVar)<br>`{{ "{{FUNC:ADD:Var1:10:$Var2}}" }}` (Add 10 to Var2 and store in Var1)<br>`{{ "{{FUNC:ADD:Result:$Var1:$Var2}}" }}` (Sum Var1 and Var2 and store in Result)|
|SUB|2|`{{ "{{FUNC:SUB:MyVar:20:10}}" }}` (20-10 and store in MyVar)|(Additional examples similar to ADD above)|
|MUL|2|`{{ "{{FUNC:MUL:MyVar:10:20}}" }}` (10*20 and store in MyVar)|(Additional examples similar to ADD above)|
|DIV|2|`{{ "{{FUNC:DIV:MyVar:​100:50}}" }}` (100/50 and store in MyVar).|(Additional examples similar to ADD above)|
|ROUND|1|`{{ "{{FUNC:ROUND:MyVar:10,11:2}}" }}`|Rounds a value to the specified number of fractional digits|
|RANDOM|2|`{{ "{{FUNC:RANDOM:MyVar:1:20}}" }}` (Find a random number between 1 (inclusive) and 20 (exclusive) and store in MyVar.<br>`{{ "{{FUNC:RANDOM:MyVar:$FirstVal:$SecondVal}}" }}` (Find a random number between FirstVal variable (inclusive) and SecondVal variable (exclusive) and store in MyVar.<br>**Note:** First value must be LOWER than Second value.|
|NOW|1|`{{ "{{FUNC:NOW:MyVar:yyyy-MM-dd HH:mm:ss}}" }}`<br>MyVar will have the current date and time.|
|FLOOR| |Returns the largest integral value less than or equal to the specified number|
|CEILING| |Returns the smallest integral value greater than or equal to the specified number|
|MIN| |Returns the smaller of two numbers|
|MAX| |Returns the larger of two numbers|
|ABS| |Returns the absolute value of a specified number|


### String Functions
|Function Name|Number of Input arguments|Example|Comments|
|----|----|----|----|
|CONCAT|Unlimited|`{{ "{{FUNC:CONCAT:MyVar:Hello:World:$Var1:Hi:$Var2}}" }}`<br>MyVar will have the string: HelloWorldXXXXHiYYYY Where XXXX is the contents of Var1 and YYYY is the contents of Var2|
|REPLACE|3|`{{ "{{FUNC:REPLACE:MyVar:Hello:He:Y}}" }}`<br>MyVar will have the string: **Yllo**<br>`{{ "{{VARSET:XX:Hello World}}" }} {{ "{{VARSET:A:l}}" }}{{ "{{VARSET:B:Z}}" }} {{ "{{FUNC:REPLACE:MyVar:$XX:$A:$B}}" }}`<br>MyVar will have the string: *HeZZo WorZd*|
|LEN|1|`{{ "{{FUNC:LEN:MyVar:Hello World}}" }}` (Length of the string 'Hello World')<br>MyVar will have the value 11|
|MID|(Arguments: 1. 0-Based Start Position 2. [Optional] Length)|`{{ "{{FUNC:MID:RES:Hello:2}}" }}` RES will have llo<br>`{{ "{{FUNC:MID:RES:Hello:0:2}}" }}` RES will have He|
|REVERSE|1|`{{ "{{FUNC:REVERSE:MyVar:Hello World}}" }}`<br>MyVar will have the value: dlroW olleH|
|INDEXOF|2|Returns the first 0-based position of a text in the string.<br>`{{ "{{FUNC:INDEXOF:RES:Hello:e}}" }}` will return 1 into RES (since e has an index of 1 in the string)|
|UPPERCASE|1|`{{ "{{FUNC:UPPERCASE:MyVar:HeLlO woRlD}}" }}`<br>MyVar will have the string: **HELLO WORLD**|
|LOWERCASE|1|`{{ "{{FUNC:UPPERCASE:MyVar:HeLlO woRlD}}" }}`<br>MyVar will have the string: **hello world**|
|TITLECASE|1|`{{ "{{FUNC:UPPERCASE:MyVar:HeLlO woRlD}}" }}`<br>MyVar will have the string: **Hello World**|

### Date Time Functions

!!! hint

    Negative values will calculate Date/Time Functions backwards.

|Function Name|Number of Input arguments|Example|Comments|
|----|----|----|----|
|AddDays|3|`{{ "{{FUNC:NOW:today:yyyy-MM-dd}}" }}`<br>`{{ "{{FUNC:AddDays:yesterday:$today:-1}} "}}`<br>`{{ "{{SetClipboard:$yesterday}}" }}`<br>`{{ "{{ctrl}{v}}" }}`|Prints yesterdays date from clipboard using an existing datetime.|
|AddMonths|3|`{{ "{{FUNC:AddMonths:lastmonth:$today:-1}}" }}`|Counts one month back from an existing datetime and saves to a new var.|
|AddSeconds|3|`{{ "{{FUNC:AddSeconds:125secondsfromnow:$today:125}}" }}`|Add 125 seconds to an existing datetime and saves to a new var.|
|AddMinutes|3|`{{ "{{FUNC:AddMonths:65minutes:$today:65}}" }}`|Add 65 minutes to an existing datetime and saves to a new var.)|
|AddHours|3|`{{ "{{FUNC:AddMonths:20hours:$today:20}}" }}`|Add 20 hours to an existing datetime and saves to a new var.|
|DateDif|4|`{{ "{{FUNC:DATEDIFF:RES:$date1:$date2:d}}" }}`|Compares two datetimes and return the time difference between them (result can be in **d**ays/**h**ours/**m**inutes/**s**econds/miliseconds)|
|DateFormat|4|`{{ "{{FUNC:DATEFORMAT:RES:$date1:dd/MM/yyyy HH:mm:ss}}" }}`|Allows to format a date|

### Other functions
|Function|Format|Example|Comments|
|----|----|----|----|
|EXEC|`{{ "{{EXEC:FILENAME|RUNASADMIN|ARGUMENTS}}" }}`|`{{ "{{EXEC:C:\WINDOWS\\NOTEPAD.EXE|0|C:\myfile.txt}}" }}`|Can also be used to load websites. `{{ "{{EXEC:https://docs.barraider.com}}" }}`|
