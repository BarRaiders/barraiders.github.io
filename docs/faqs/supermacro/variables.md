---
title: SuperMacro - Variables
description: Learn how to use variables in the SuperMacro plugin to store and manipulate data for use further down in a the macro, or a different macro all together. Variables opens up a world of new possibilities for your SuperMacro's on the Stream Deck.
---

<!-- NOTE: To you, the Contributor!
    Ironically, the double-bracket syntax used in SuperMacro conflicts with a special Marco syntax we can use here.
    See custom-functions.md in the *root* of the repository for the workaround
-->

# Variables

Variables are used to store data to be used further down in the Macro or in a different macro altogether. This opens up a whole world of options. You can read data from files, manipulate it, and then write it to either another file, to the Stream Deck key or execute it as a set of keystrokes. Variables start with a `$` sign to differentiate them from normal text.

## Predefined Variables
The following list of variables are always be available for you to use either with Functions (like CONCAT) or to execute as keyboard commands:

<!-- 
https://facelessuser.github.io/pymdown-extensions/extensions/keys/
 -->

| Variable   | Output          |
|------------|-----------------|
| $SMCOLON   | ++colon++       |
| $SMDOLLAR  | ++"$"++         |
| $SMENTER   | ++enter++       |
| $SMLCB     | ++brace-left++  |
| $SMRCB     | ++brace-right++ |
| $SMSPACE   | ++space++

## User Defined Variables
Creating and using User Defined variables is easy using the following Variable Commands.

!!! note

    Use a `:` between the command name and the arguments

|Command|Example|Comment|
|-------|-------|-------|
| Input | `{{ "{{Input:VarName}}" }}` |Get input from the user and store it in `VarName`. |
| Output | `{{ "{{Output:MyVar}}" }}` | Output the input previously gathered into `MyVar`. |
| VarSet | `{{ "{{VarSet:MyVar:MyValue}}" }}` | Set the value `MyValue` into `MyVar`. |
| OutputToFile | `{{ "{{OutputToFile:MyVar:C:\\filename.txt}}" }}` | Write the contents of the `MyVar` variable into `C:\filename.txt` file. |
| AppendToFile | `{{ "{{AppendToFile:MyVar:C:\\filename.txt}}" }}` | Append the contents of the `MyVar` variable into `C:\filename.txt`
| VarSetFromFile | `{{ "{{VarSetFromFile:MyVar:C:\\filename.txt}}" }}` | Read the contents of the `C:\filename.txt` file and store into `MyVar`. |
| SetClipboard | `{{ "{{SetClipboard:$MyVar}}" }}` | Store variable in clipboard.|
| VarSetFromClipboard | `{{ "{{VarSetFromClipboard:MyVar}}" }}`	| Read the contents of the clipboard and store into `MyVar`. |
| VarUnset | `{{ "{{VarUnset:MyVar}}" }}` | Clears `MyVar`. |
| VarUnsetAll | `{{ "{{VARUNSETALL}}" }}` | Clears **all** variables. |
| SetIconFromFile | `{{ "{{SetIconFromFile:C:\\image.png}}" }}` | Sets the Stream Deck key's icon to the image stored in `C:\image.png`. |
| VarSetFromEnv | `{{ "{{VarSetFromEnv:MyPath:PATH}}{{OUTPUT:MyPath}}" }}`|Get the %PATH% environment variable:|
| SetKeyTitle | `{{ "{{SetKeyTitle:$MyVar}}` | Set Stream Deck title to variable value. |