---
title: SuperMacro - Available Commands
description: Find a list of all available commands for the SuperMacro plugin for the Stream Deck by BarRaider. Get started using SuperMacro today!
---

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

# SuperMacro - List of commands

<hr />
=== "Keyboard Commands"

    ## Keyboard commands

    | Keyboard Key| Macro command |
    | ----------- | ----------- |
    | ++a++ - ++z++ | {{ "{{VK_XXXX}}" }}  (XXXX = the letter - e.g. VK_A / VK_B ...) |
    | ++0++ - ++9++ | {{ "{{VK_XXXX}}" }}  (XXXX = the number - e.g. VK_0 / VK_1 ...) |
    |  Any of the following characters: ``;/\`[\]':?~{|}\"``  | Exact command changes between keyboard layouts:<br>Try the following macros to figure out the correct command:<br> {{ "{{oem_1}} "}}{{ "{{oem_2}} "}}{{ "{{oem_3}} "}}{{ "{{oem_4}} "}}{{ "{{oem_5}} "}} {{ "{{oem_6}} "}}{{ "{{oem_7}} "}}{{ "{{oem_8}} "}} {{ "{{shift}{oem_1}} "}}{{ "{{shift}{oem_2}} "}}{{ "{{shift}{oem_3}} "}} {{ "{{shift}{oem_4}} "}}{{ "{{shift}{oem_5}} "}} {{ "{{shift}{oem_6}} "}}{{ "{{shift}{oem_7}} "}}{{ "{{shift}{oem_8}} "}}  |
    | ++num0++ | {{ "{{NUMPAD0}}" }} |
    | ++num1++ | {{ "{{NUMPAD1}}" }} |
    | ++num2++ | {{ "{{NUMPAD2}}" }} |
    | ++num3++ | {{ "{{NUMPAD3}}" }} |
    | ++num4++ | {{ "{{NUMPAD4}}" }} |
    | ++num5++ | {{ "{{NUMPAD5}}" }} |
    | ++num6++ | {{ "{{NUMPAD6}}" }} |
    | ++num7++ | {{ "{{NUMPAD7}}" }} |
    | ++num8++ | {{ "{{NUMPAD8}}" }} |
    | ++num9++ | {{ "{{NUMPAD9}}" }} |
    | ++multiply++ | {{ "{{MULTIPLY}}" }} |
    | ++add++ | {{ "{{ADD}}" }}|
    | ++num-minus++ | {{ "{{SUBTRACT}}" }} |
    | ++num-separator++ | {{ "{{DECIMAL}}" }}|
    | ++num-slash++ | {{ "{{DIVIDE}}" }} |
    | ++back++| {{ "{{BACK}}" }} |
    | ++tab++| {{ "{{TAB}}" }}|
    | ++clear++| {{ "{{CLEAR}}" }}|
    | ++enter++| {{ "{{RETURN}}" }} or {{ "{{ENTER}}" }} |
    | ++shift++| {{ "{{SHIFT}}" }}|
    | ++left-shift++ | {{ "{{LSHIFT}}" }} |
    | ++right-shift++| {{ "{{RSHIFT}}" }} |
    | ++ctrl++ | {{ "{{CONTROL}}" }} or {{ "{{CTRL}}" }} |
    | ++left-ctrl++ | {{ "{{LCONTROL}}" }} or {{ "{{LCTRL}}" }} |
    | ++right-ctrl++ | {{ "{{RCONTROL}}" }} or {{ "{{RCTRL}}" }} |
    | ++alt++ | {{ "{{ALT}}" }} or {{ "{{MENU}}" }}|
    | ++left-alt++ | {{ "{{LALT}}" }} or {{ "{{LMENU}}" }} |
    | ++right-alt++ | {{ "{{RALT}}" }} or {{ "{{RMENU}}" }} |
    | ++media-pause++ / ++break++| {{ "{{BREAK}}" }}|
    | ++caps-lock++ | {{ "{{CAPITAL}}" }}|
    | ++esc++ | {{ "{{ESCAPE}}" }} |
    | ++space++ | {{ "{{SPACE}}" }}|
    | ++page-up++ | {{ "{{PAGEUP}}" }} or {{ "{{PGUP}}" }} or {{ "{{PRIOR}}" }} |
    | ++"Num Page Up"++| {{ "{{NUMPAD_PAGEUP}}" }}|
    | ++page-down++ | {{ "{{PAGEDOWN}}" }} or {{ "{{PGDN}}" }} or {{ "{{NEXT}}" }} |
    | ++"Num Page Down"++| {{ "{{NUMPAD_PAGEDOWN}}" }}|
    | ++home++ | {{ "{{HOME}}" }} |
    | ++"Num Home"++| {{ "{{NUMPAD_HOME}}" }} |
    | ++end++ | {{ "{{END}}" }}|
    | ++"Num End"++ | {{ "{{NUMPAD_END}}" }}|
    | ++arrow-up++ | {{ "{{UP}}" }} |
    | ++"↑ Num Up"++ | {{ "{{NUMPAD_UP}}" }} |
    | ++arrow-left++ | {{ "{{LEFT}}" }} |
    | ++"← Num Left"++| {{ "{{NUMPAD_LEFT}}" }} |
    | ++arrow-right++| {{ "{{RIGHT}}" }}|
    | ++"→ Num Right"++| {{ "{{NUMPAD_RIGHT}}" }}|
    | ++arrow-down++ | {{ "{{DOWN}}" }} |
    | ++"↓ Num Down"++ | {{ "{{NUMPAD_DOWN}}" }} |
    | ++select++ | {{ "{{SELECT}}" }} |
    | ++print-screen++ | {{ "{{SNAPSHOT}}" }} |
    | ++print++ | {{ "{{PRINT}}" }}|
    | ++"Execute"++ | {{ "{{EXECUTE}}" }}|
    | ++insert++ | {{ "{{INSERT}}" }} |
    | ++"⎀ Num Ins"++ | {{ "{{NUMPAD_INSERT}}" }}|
    | ++delete++ | {{ "{{DELETE}}" }} |
    | ++"⌦ Num Del"++ | {{ "{{NUMPAD_DEL}}" }}|
    | ++help++ | {{ "{{HELP}}" }} |
    | ++left-windows++ | {{ "{{LWIN}}" }} or {{ "{{WIN}}" }} or {{ "{{WINDOWS}}" }} |
    | ++right-windows++ | {{ "{{RWIN}}" }} |
    | ++f1++ - ++f24++ | {{ "{{fXX}}" }} (XX = the number - e.g. f1 / f24 ...) |
    | ++plus++ / ++equal++ | {{ "{{OEM_PLUS}}" }} / {{ "{{SHIFT}{OEM_PLUS}} "}}  | 
    | ++minus++ / ++underscore++ | {{ "{{OEM_MINUS}}" }} / {{ "{{SHIFT}{OEM_MINUS}} "}} |
    | ++period++ / ++greater++ | {{ "{{OEM_PERIOD}}" }} / {{ "{{SHIFT}{OEM_PERIOD}} "}} |
    | ++comma++ / ++less++| {{ "{{OEM_COMMA}}" }} / {{ "{{SHIFT}{OEM_COMMA}} "}} | 
    | ++num-lock++ | {{ "{{NUMLOCK}}" }} |
    | ++scroll-lock++ | {{ "{{SCROLL}}" }} |

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
    | (DEPRECATED) Mouse Move based on ABSOLUTE position (DEPRECATED)|{{ "{{MOUSEPOS:X,Y}} "}} (Move the cursor to the X,Y position on the screen. Values from 0,0 [top-left] to 65535,65535 [bottom-right])|

=== "Windows Commands"

    |Action|Macro Command|
    |----|----|
    | ++browser-back++ |{{ "{{BROWSER_BACK}}" }}|
    | ++browser-forward++ |{{ "{{BROWSER_FORWARD}}" }}|
    | ++browser-home++ |{{ "{{BROWSER_HOME}}" }}|
    | ++browser-refresh++ |{{ "{{BROWSER_REFRESH}}" }}|
    | ++browser-stop++ |{{ "{{BROWSER_STOP}}" }}|
    | ++browser-search++ |{{ "{{BROWSER_SEARCH}}" }}|
    | ++browser-favorites++ |{{ "{{BROWSER_FAVORITES}}" }}|
    | ++media-next-track++|{{ "{{MEDIA_NEXT_TRACK}}" }}|
    | ++media-prev-track++ |{{ "{{MEDIA_PREV_TRACK}}" }}|
    | ++media-play++ / ++media-pause++ |{{ "{{MEDIA_PLAY_PAUSE}}" }}|
    | ++media-stop++ |{{ "{{MEDIA_STOP}}" }}|
    | ++volume-up++ |{{ "{{VOLUME_UP}}" }}|
    | ++volume-down++ |{{ "{{VOLUME_DOWN}}" }}|
    | ++volume-mute++ |{{ "{{VOLUME_MUTE}}" }}|

=== "Advanced Commands"
    |Action|Macro Command|
    |----|----|
    |{{ "{{//}} "}}|Comments Support: Anything after the {{ "{{//}} "}} sign will be ignored until end of line.<br>**Note:** The "Don't treat "New Line" as Enter" setting must be DISABLED for this to work properly|
    |PAUSE|{{ "{{PAUSE:XXXX}} "}} (XXXX = length in milliseconds). Will pause execution of the rest of the SuperMacro for the time specified|
    |KeyDown|{{ "{{KeyDown:XXXX}} "}} (XXXX = name of key| example {{ "{{KeyDown:F1}} "}}). Simulates holding the key down on the keyboard.<br>**Note:** Should be eventually accompanied by a `KeyUp` command|
    |KeyUp|{{ "{{KeyUp:XXXX}} "}} (XXXX = name of key| example {{ "{{KeyUp:SHIFT}} "}})|
    |MSavePos|{{ "{{MSAVEPOS}} "}} stores the current mouse cursor position.<br>The position is stored in variables: $MOUSE_X and $MOUSE_Y|
    |MLoadPos|{{ "{{MLOADPOS}} "}} moves the mouse to the previous set position (when `{MSAVEPOS}` was called).|
    |SetKeyTitle|{{ "{{SetKeyTitle:$MyVar}} "}} Sets the text on the Stream Deck key to the contents of `MyVar`.|
    |SetClipboard|{{ "{{SetClipboard:$MyVar}} "}} Sets the clipboard to the contents of `MyVar`.|
