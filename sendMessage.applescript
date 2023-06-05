on run {targetMessage}
    tell application "Messages"
        set targetService to 1st service whose service type = SMS 
        set targetBuddy to buddy "888222" of targetService

        send targetMessage to targetBuddy
    end tell
end run