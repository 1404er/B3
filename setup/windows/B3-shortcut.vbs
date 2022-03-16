Const strProgramTitle = "B3"
Const strProgramDescription = "B3 - Best Buy purchase bot"
strProgram = "%LOCALAPPDATA%\Dogey11\B3\B3" & Wscript.Arguments.Item(0)
Const strWorkDir = "%USERPROFILE%"
Dim objShortcut, objShell
Set objShell = WScript.CreateObject ("Wscript.Shell")
If Wscript.Arguments.Item(1)="1" Then
    strLPath = objShell.SpecialFolders ("Desktop")
ElseIf Wscript.Arguments.Item(1)="2" Then
    strLPath = objShell.SpecialFolders ("Startup")
End If
Set objShortcut = objShell.CreateShortcut (strLPath & "\" & strProgramTitle & ".lnk")
objShortcut.TargetPath = strProgram
objShortcut.WorkingDirectory = strWorkDir
objShortcut.Description = strProgramDescription
objShortcut.Save
WScript.Quit