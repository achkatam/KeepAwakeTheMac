# Keep Awake App

This Python script uses the `caffeinate` command to keep your Mac awake. It prevents the system from going to sleep until you manually stop it.

# FEEL FREE TO USE THE SOURCE CODE

# Create the app as LaunchAgent and start it
    1. Create the 'LaunchAgents' dir in Library if not existing
    2. Create '.plist' file:
        nano ~/Library/LaunchAgents/com.user.keepawake.plist
    3. Example of your .plist file:
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.user.keepawake</string>
            <key>ProgramArguments</key>
            <array>
                <string>/path/to/your/dist/keep_awake</string>
            </array>
            <key>KeepAlive</key>
            <false/>
        </dict>
        </plist>
    
    The code does not start everytime the system is ON purposly.

    4. Launch the LaunchAgent
        launchctl load ~/Library/LaunchAgents/com.user.keepawake.plist
    5. In case you want to stop the app:
        launchctl unload ~/Library/LaunchAgents/com.user.keepawake.plist

# Check if the app is running
    1. launchctl list | grep com.user.keepawake


This `README.md` provides a comprehensive guide on setting up, using, and troubleshooting your keep awake app. Adjust paths and details as needed for your specific setup.
