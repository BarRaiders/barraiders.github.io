# Examples

<details>
<summary>Open Windows Explorer then go to C:\Program Files</summary>
<br>
  Output delay should be set to ~20ms<br>
  ```
  {{win}{e}}{{pause:400}}{{alt}{d}}c:\Program Files\{{enter}}
  </details>
  
  <details>
<summary>Open Notepad and change settings</summary>
<br>
  Output delay should be set to ~20ms<br>
  ```
  {{win}{r}}{{pause:500}}notepad.exe{{enter}}{{pause:1000}}Ok... Let's see what this plugin can do...{{alt}{f}}{{right}}{{PAUSE:400}}{{right}}{{PAUSE:400}}f{{pause:400}}times{{down}}{{PAUSE:400}}{{tab}}{{PAUSE:400}}{{down}}{{PAUSE:400}}{{down}}{{PAUSE:400}}{{ENTER}}{{ENTER}}For more information visit: https://barider.g1thubio{{ctrl}{shift}{left}}{{PAUSE:400}}https://barraider.github.io{{ENTER}}{{alt}{o}}f{{PAUSE:100}}Lucida Console{{tab}}Regular{{Tab}}12{{ENTER}}
  ```
</details>

<details>
<summary>Calculate something using the Windows Calculator</summary>
<br>
  Output delay should be set to ~20ms<br>
  ```
  {{win}{r}}{{pause:300}}calc{{enter}}{{pause:1000}}1*2*3*4*5=
  ```
</details>
