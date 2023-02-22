# SuperMacro - Advanced Settings
Here you will find a detailed explanation of what each of the advanced settings does in SuperMacro.

​![Advanced settings overview](img/advanced-settings.png"Advanced settings overview")
​
## Settings
### Secondary ENTER behavior
By default, when SuperMacro notices a new line, it simulates a  newline keystroke. When this is enabled SuperMacro will instead simulate a KEYPRESS event for the Enter/Return virtual keycode. In some apps, this may work better when dealing with new lines.

### Forced Macro Mode
Sends normal text (such as 'abc') as keystrokes (i.e. `{{a}}{{b}}{{c}}`).
By default, when SuperMacro sees normal text, it uses a normal TextEntry, some games/apps ignore these type of text entries. When this is enabled, SuperMacro will instead simulate a KEYPRESS for each character.

### Don't treat "New Line" as Enter
This mode allows you to write macros on multiple lines (to make it cleaner to read and easier to maintain) without worrying that SuperMacro will send a Newline/ENTER command every time it encounters a new line. When enabled, unless you implicitly type `{{ENTER}}`, SuperMacro will NOT be sending Newline commands.

### Output Delay
​![Output Delay](img/output-delay.png"Output Delay")

This sets the delay/pause between one command to the other. In other words, a longer output delay will simulate longer wait time between each character/keystroke.
