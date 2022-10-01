# Examples

<details>
  <summary>Open Windows Explorer then go to C:\Program Files</summary>
  <br>
    Output delay should be set to ~20ms<br>
    ```
    {{win}{e}}{{pause:400}}{{alt}{d}}c:\Program Files\{{enter}}
    ```
</details>
  
<details>
  <summary>Open Notepad and change settings</summary>
  <br>
    Output delay should be set to ~20ms<br>
    This will not work correctly if your Windows (and notepad) are not in English<br>
    ```
    {{win}{r}}{{pause:500}}notepad.exe{{enter}}{{pause:1000}}Ok... Let's see what this plugin can do...{{alt}{f}}{{right}}{{PAUSE:400}}{{right}}  {{PAUSE:400}}f{{pause:400}}times{{down}}{{PAUSE:400}}{{tab}}{{PAUSE:400}}{{down}}{{PAUSE:400}}{{down}}{{PAUSE:400}}{{ENTER}}{{ENTER}}For more information visit: https://barider.g1thubio{{ctrl}{shift}{left}}{{PAUSE:400}}https://barraider.github.io{{ENTER}}{{alt}{o}}f{{PAUSE:100}}Lucida Console{{tab}}Regular{{Tab}}12{{ENTER}}
    ```
</details>

<details>
  <summary>Calculate something using the Windows Calculator</summary>
    Output delay should be set to ~20ms<br>
    ```
    {{win}{r}}{{pause:300}}calc{{enter}}{{pause:1000}}1*2*3*4*5=
    ```
</details>

<details>
  <summary>Move the mouse to a certain position on the screen, then Double-Click the left mouse button.</summary>
    To find the correct position you can use the Mouse Location action.<br>
    ```
    {{MOUSEXY:1000,15}}{{MLEFTDBLCLICK}}
    ```
</details>

<details>
  <summary>Move the mouse by 10 pixels left and 20 pixels down on every press</summary>
    ```
    {{MOUSEMOVE:-10,20}}
    ```
</details>

<details>
  <summary>Variables: Get input from user and then use it later on.</summary>
    ```
    {{INPUT:Name}}Hello {{OUTPUT:Name}}, Nice to meet you!
    ```
</details>

<details>
  <summary>Variables: Read text from file into MyVar variable.</summary>
    ```
    {{VarSetFromFile:MyVar:C:\filename.txt}}
    ```
</details>

<details>
  <summary>Functions: Choose a random number between 1 (inclusive) to 10 (exclusive) and store it in MyVar</summary>
    ```
    {{FUNC:RANDOM:MyVar:1:10}}
    ```
</details>

<details>
  <summary>Functions: Input 2 numbers from the user. Choose a random number between firstNum variable (inclusive) to secondNum variable (exclusive) and store it in MyVar:</summary>
    ```
    {{INPUT:firstNum}}
    {{INPUT:secondNum}}
    {{FUNC:RANDOM:MyVar:$firstNum:$secondNum}}
    ```
</details>

<details>
  <summary>Functions: Select a number from the user and multiply it by 10. Then save it to a file named c:\temp\result.txt:</summary>
    ```
    {{INPUT:myNumber}}
    {{FUNC:MUL:MyResult:$myNumber:10}}
    {{OUTPUTTOFILE:MyResult:c:\temp\result.txt}}
    ```
</details>

<details>
  <summary>Add comments in the code using `{{//}}` command</summary>
    ```
    {{INPUT:myNumber}} {{//}} Input a number from the user
    {{FUNC:MUL:MyResult:$myNumber:10}} {{//}} Multiply number by 10
    {{OUTPUTTOFILE:MyResult:c:\temp\result.txt}} {{//}} Save result in file
    ```
</details>

<details>
  <summary>Read text from a file and show it on the Stream Deck Key:</summary>
    ```
    {{VARSETFROMFILE:MyVar:c:\counter.txt}}
    {{SETKEYTITLE:$MyVar}}
    ```
</details>

<details>
  <summary>Read text from a clipboard and show it on the Stream Deck Key:</summary>
    ```
    {{VARSETFROMCLIPBOARD:MyVar}}
    {{SETKEYTITLE:$MyVar}}
    ```
</details>

<details>
  <summary>Scroll the mouse up by 5 clicks and then down by 3 clicks:</summary>
    ```
    {{MSCROLLUP:5}}
    {{MSCROLLDOWN:3}}
    ```
</details>

<details>
  <summary>Move the mouse to coordinates set from variables:</summary>
    ```
    {{VARSET:X:100}}
    {{VARSET:Y:400}}
    {{MOUSEXY:$X,$Y}}
    ```
</details>

<details>
  <summary>Repalce all "l"'s with "Z"'s in the string `Hello World` and show it on key</summary>
    ```
    {{VARSET:XX:Hello World}}
    {{VARSET:A:l}}
    {{VARSET:B:Z}}
    {{FUNC:REPLACE:MyVar:$XX:$A:$B}}
    {{SETKEYTITLE:$MyVar}}
    ```
</details>

<details>
  <summary>Show the current date and time on the key:</summary>
    ```
    {{FUNC:NOW:MyVar:yyyy-MM-dd HH:mm:ss}}
    {{SETKEYTITLE:$MyVar}}
    ```
</details>

<details>
  <summary>Print the current date and time:</summary>
    ```
    {{FUNC:NOW:MyVar:yyyy-MM-dd HH:mm:ss}}
    {{OUTPUT:MyVar}}
</details>

<details>
  <summary>Set value of variable into the clipboard</summary>
    ```
    {{VARSET:MyVar:Hello World}}
    {{SETCLIPBOARD:$MyVar}}
    ```
</details>

<details>
  <summary>Read text from one txt file and insert into another along with a timestamp. (Contributed by Bowser#2891)</summary>
    ```
    {{VarSetFromFile:ListVar:C:\temp\List.txt}}
    {{VarSetFromFile:NewTextVar:C:\temp\NewText.txt}}
    {{FUNC:NOW:TimeVar:yyyy-MM-dd HH:mm:ss}}

    {{FUNC:CONCAT:ListVarU:$ListVar:$SMENTER:$NewTextVar: :$TimeVar}}

    {{OutputToFile:ListVarU:C:\temp\List.txt}}
    ```
</details>

<details>
  <summary>Get input from user, then load a file with the inputed name (from the `c:\temp` folder) to CLIPBOARD and show it on the Stream Deck Key. (Contributed by Bowser#2891)</summary>
  Note: Entire content of file may not fit within the screen of the Stream Deck Key.<br>
    ```
    {{Input:MyVar}}
    {{FUNC:CONCAT:Filename:C:$SMCOLON:\temp\:$MyVar:.txt}}
    {{VarSetFromFile:MyVar2:$Filename}}
    {{SetClipboard:$MyVar2}}
    {{SETKEYTITLE:$MyVar2}}
    ```
</details>
