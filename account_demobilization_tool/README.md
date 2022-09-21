# account_demobilization_tool

## Intro

The scripts in this repo are as-is and will require adaptation to work in your
environment.

Please use this as general inspiration when designing the demobilization process
for your users!

## Building

Use munkipkg to build via make.

```sh
make
```

## General usage

This pkg is design to for deployment with munki and Jamf Pro. It help transition
from one set of pkgs and profiles for identity management to new set. The main
logic of this script can is within the `do_first_demobilization_run` function.

```sh
do_first_demobilization_run() {
    echo "Command: DeterminateManual: 6" >>"$DEPNOTIFY_LOG"
    switch_identity_framework "Switching identity management framework"
    wait_for_pkg "$JAMFCONNECT_PKG_ID" "Installing identity management software"
    submit_system_inventory
    wait_for_profile ".*Computer Level.*Cert" \
        "Migrating authentication certificate"
    wait_for_profile "OTA - Jamf Connect Login" "Waiting for login configuration"
    wait_for_profile "Jamf Connect Login Demobilize" "Waiting for new account configuration"
    disable_jamf_connect_on_next_login "Configuring next logon"
    enable_jamf_connect_demobilization "Enabling account conversion on next logon"
    set_progress_record "first_demobilization_run" "done"
    prompt_for_logout "Almost done."
}
```

This function waits for the Jamf Connect pkg, submits inventory and awaits
profiles scoped to devices whom have the Jamf Connect pkg installed. It then
proceeds to enable the Jamf Connect demobilization mechanism.

Please feel free to fork and make it your own.
