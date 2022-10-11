<!-- 
    Because of the syntax that macros require, adding them thoroughly broke this page until Cyber refactored it.
    Single { } are fine, but in order to use double brackets the way SuperMacro does, you need to declare the whole thing to be a string
        Example: {{SPACE}} would become {{ "{{SPACE}}" }}

    Cyber accomplished the refactor using Find & Replace twice.
        replace: "\{\{" with: "\{\{ \"\{\{"
        replace: "\}\}" with: " \"\}\}"

    Reverting this change *will* break the page, but it is easy enough to do with 2 more Find & Replace uses
        replace: "\{\{ \"" with: ""
        replace: " \"\}\}" with: ""
 -->

# List of commands

<hr />
=== "Keyboard Commands"

    ## Keyboard commands

    | Keyboard Key| Macro command |
    | ----------- | ----------- |
    | Letters A-Z | {VK_XXXX} (XXXX = the letter - e.g. VK_A / VK_B ...) |
    | Numbers 0-9 | {VK_XXXX} (XXXX = the number - e.g. VK_0 / VK_1 ...) | 
    |  Any of the following characters: ``;/\`[\]':?~{|}\"``  | Exact command changes between keyboard layouts:<br>Try the following macros to figure out the correct command:<br> {{ "{{oem_1}} "}}{{ "{{oem_2}} "}}{{ "{{oem_3}} "}}{{ "{{oem_4}} "}}{{ "{{oem_5}} "}} {{ "{{oem_6}} "}}{{ "{{oem_7}} "}}{{ "{{oem_8}} "}} {{ "{{shift}{oem_1}} "}}{{ "{{shift}{oem_2}} "}}{{ "{{shift}{oem_3}} "}} {{ "{{shift}{oem_4}} "}}{{ "{{shift}{oem_5}} "}} {{ "{{shift}{oem_6}} "}}{{ "{{shift}{oem_7}} "}}{{ "{{shift}{oem_8}} "}}  |
    | Numpad 0 |{NUMPAD0} |
    | Numpad 1 | {NUMPAD1} |
    | Numpad 2 | {NUMPAD2} |
    | Numpad 3 | {NUMPAD3} |
    | Numpad 4 | {NUMPAD4} |
    | Numpad 5 | {NUMPAD5} |
    | Numpad 6 | {NUMPAD6} |
    | Numpad 7 | {NUMPAD7} |
    | Numpad 8 | {NUMPAD8} |
    | Numpad 9 | {NUMPAD9} |
    | Numpad \* | {MULTIPLY} |
    | Numpad + | {ADD}|
    | Numpad - | {SUBTRACT} |
    | Numpad . | {DECIMAL}|
    | Numpad / | {DIVIDE} |
    | BACKSPACE| {BACK} |
    | TAB| {TAB}|
    | CLEAR| {CLEAR}|
    | ENTER| {RETURN} or {ENTER} |
    | SHIFT| {SHIFT}|
    | Left SHIFT | {LSHIFT} |
    | Right SHIFT| {RSHIFT} |
    | CTRL | {CONTROL} or {CTRL} |
    | Left CONTROL| {LCONTROL} or {LCTRL} |
    | Right CONTROL | {RCONTROL} or {RCTRL} |
    | ALT| {ALT} or {MENU}|
    | Left ALT | {LALT} or {LMENU} |
    | Right ALT| {RALT} or {RMENU} |
    | PAUSE/BREAK| {BREAK}|
    | CAPS LOCK| {CAPITAL}|
    | ESC| {ESCAPE} |
    | SPACEBAR | {SPACE}|
    | PAGE UP| {PAGEUP} or {PGUP} or {PRIOR} |
    | Numpad PAGE UP| {NUMPAD_PAGEUP}|
    | PAGE DOWN| {PAGEDOWN} or {PGDN} or {NEXT} |
    | Numpad PAGE DOWN| {NUMPAD_PAGEDOWN}|
    | HOME | {HOME} |
    | Numpad HOME| {NUMPAD_HOME} |
    | END| {END}|
    | Numpad END | {NUMPAD_END}|
    | UP ARROW | {UP} |
    | Numpad UP ARROW | {NUMPAD_UP} |
    | LEFT ARROW | {LEFT} |
    | Numpad LEFT ARROW | {NUMPAD_LEFT} |
    | RIGHT ARROW| {RIGHT}|
    | Numpad RIGHT ARROW| {NUMPAD_RIGHT}|
    | DOWN ARROW | {DOWN} |
    | Numpad DOWN ARROW | {NUMPAD_DOWN} |
    | SELECT | {SELECT} |
    | PRINT SCREEN| {SNAPSHOT} |
    | PRINT| {PRINT}|
    | EXECUTE| {EXECUTE}|
    | INS| {INSERT} |
    | Numpad INS | {NUMPAD_INSERT}|
    | DEL| {DELETE} |
    | Numpad DEL | {NUMPAD_DEL}|
    | HELP | {HELP} |
    | Left Windows | {LWIN} or {WIN} or {WINDOWS} |
    | Right Windows | {RWIN} |
    | F1 | {F1} |
    | F2 | {F2} |
    | F3 | {F3} |
    | F4 | {F4} |
    | F5 | {F5} |
    | F6 | {F6} |
    | F7 | {F7} |
    | F8 | {F8} |
    | F9 | {F9} |
    | F10 | {F10} |
    | F11 | {F11} |
    | F12 | {F12} |
    | F13 | {F13} |
    | F14 | {F14} |
    | F15 | {F15} |
    | F16 | {F16} |
    | F17 | {F17} |
    | F18 | {F18} |
    | F19 | {F19} |
    | F20 | {F20} |
    | F21 | {F21} |
    | F22 | {F22} |
    | F23 | {F23} |
    | F24 | {F24} |
    | Plus: += | {OEM_PLUS} / {{ "{{SHIFT}{OEM_PLUS}} "}}  | 
    | Minus: -_ | {OEM_MINUS} / {{ "{{SHIFT}{OEM_MINUS}} "}} |
    | Period: .> | {OEM_PERIOD} / {{ "{{SHIFT}{OEM_PERIOD}} "}} |
    | Comma: ,<| {OEM_COMMA} / {{ "{{SHIFT}{OEM_COMMA}} "}} | 
    | NUM LOCK | {NUMLOCK} |
    | SCROLL LOCK| {SCROLL} |

=== "Mouse Commands"

    ## Mouse commands

    |Mouse Key|Macro Command|
    |----|----|
    | Mouse Left-Click|{{ "{{LBUTTON}} "}}|
    | Mouse Left Double-Click|{{ "{{MLEFTDBLCLICK}} "}}|
    | Mouse Left Button Down|{{ "{{MLEFTDOWN}} "}}|
    | Mouse Left Button Up|{{ "{{MLEFTUP}} "}}|
    | Mouse Right-Click|{{ "{{RBUTTON}} "}}|
    | Mouse Right Double-Click|{{ "{{MRIGHTDBLCLICK}} "}}|
    | Mouse Right Button Down|{{ "{{MRIGHTDOWN}} "}}|
    | Mouse Right Button Up|{{ "{{MRIGHTUP}} "}}|
    | Mouse Middle Click|{{ "{{MBUTTON}} "}}|
    | Mouse Middle Button Down|{{ "{{MMIDDLEDOWN}} "}}|
    | Mouse Middle Button Up|{{ "{{MMIDDLEUP}} "}}|
    | Mouse Button 4 Click|{{ "{{XBUTTON1}} "}}|
    | Mouse Button 5 Click|{{ "{{XBUTTON2}} "}}|
    | Mouse Scroll Wheel Up|{{ "{{MSCROLLUP}} "}}<br>Optional: Set the number of 'clicks' to scroll up: {{ "{{MSCROLLUP:10}} "}} will scroll up 10 clicks|
    | Mouse Scroll Wheel Down|{{ "{{MSCROLLDOWN}} "}}<br>Optional: Set the number of 'clicks' to scroll down: {{ "{{MSCROLLDOWN:3}} "}} will scroll down 3 clicks|
    | Mouse Horizontal Scroll Left|{{ "{{MSCROLLLEFT}} "}}<br>Optional: Set the number of 'clicks' to scroll left: {{ "{{MSCROLLLEFT:3}} "}} will scroll left 3 clicks|
    | Mouse Horizontal Scroll Right|{{ "{{MSCROLLRIGHT}} "}}<br>Optional: Set the number of 'clicks' to scroll right: {{ "{{MSCROLLRIGHT:3}} "}} will scroll right 3 clicks|
    | Mouse Move based on CURRENT position|{{ "{{MOUSEMOVE:X,Y}} "}} (Move the cursor by X,Y from current position)|
    | Mouse Move based on multi-screen resolutions|{{ "{{MOUSEXY:X,Y}} "}} (Move the cursor to the X,Y position on the screen. 0,0 is the [top-left] of your primary monitor. Supports both positive and negative values. Use along with the `Mouse Location` action to easily find the right coordinates on your PC<br>Supports variables too: {{ "{{MOUSEXY:$Var1,$Var2}} "}}|
    | Store current mouse position|{{ "{{MSAVEPOS}} "}} stores the current mouse cursor position.<br>The position is stored in variables: $MOUSE_X and $MOUSE_Y|
    | Move mouse to previous stored position|{{ "{{MLOADPOS}} "}} moves the mouse to the previous set position (when `{MSAVEPOS}` was called).|
    | (DEPRICATED) Mouse Move based on ABSOLUTE position (DEPRICATED)|{{ "{{MOUSEPOS:X,Y}} "}} (Move the cursor to the X,Y position on the screen. Values from 0,0 [top-left] to 65535,65535 [bottom-right])|

=== "Windows Commands"

    |Action|Macro Command|
    |----|----|
    |Browser: Back|{BROWSER_BACK}|
    |Browser: Forward|{BROWSER_FORWARD}|
    |Browser: Home|{BROWSER_HOME}|
    |Browser: Refresh|{BROWSER_REFRESH}|
    |Browser: Stop|{BROWSER_STOP}|
    |Browser: Search|{BROWSER_SEARCH}|
    |Browser: Favorites|{BROWSER_FAVORITES}|
    |Media: Next|{MEDIA_NEXT_TRACK}|
    |Media: Previous|{MEDIA_PREV_TRACK}|
    |Media: Play/Pause|{MEDIA_PLAY_PAUSE}|
    |Media: Stop|{MEDIA_STOP}|
    |Volume: Up|{VOLUME_UP}|
    |Volume: Down|{VOLUME_DOWN}|
    |Volume: Mute|{VOLUME_MUTE}|

=== "Advanced Commands"
    |Action|Macro Command|
    |----|----|
    |{{ "{{//}} "}}|Comments Support: Anything after the {{ "{{//}} "}} sign will be ignored until end of line.<br>**Note:** The "Don't treat "New Line" as Enter" setting must be DISABLED for this to work properly|
    |PAUSE|{{ "{{PAUSE:XXXX}} "}} (XXXX = length in miliseconds). Will pause execution of the rest of the SuperMacro for the time specified|
    |KeyDown|{{ "{{KeyDown:XXXX}} "}} (XXXX = name of key| example {{ "{{KeyDown:F1}} "}}). Simulates holding the key down on the keyboard.<br>**Note:** Should be eventually accompanied by a `KeyUp` command|
    |KeyUp|{{ "{{KeyUp:XXXX}} "}} (XXXX = name of key| example {{ "{{KeyUp:SHIFT}} "}})|
    |MSavePos|{{ "{{MSAVEPOS}} "}} stores the current mouse cursor position.<br>The position is stored in variables: $MOUSE_X and $MOUSE_Y|
    |MLoadPos|{{ "{{MLOADPOS}} "}} moves the mouse to the previous set position (when `{MSAVEPOS}` was called).|
    |SetKeyTitle|{{ "{{SetKeyTitle:$MyVar}} "}} Sets the text on the Stream Deck key to the contents of `MyVar`.|
    |SetClipboard|{{ "{{SetClipboard:$MyVar}} "}} Sets the clipboard to the contents of `MyVar`.|
