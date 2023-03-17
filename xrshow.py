#!/usr/bin/python3

# Author : Hemant Sharma
import re
import sys
import pexpect


# This function takes a host name and a list of show commands and executes them on the host using ssh
def xrshow(host, clilist):
    try:
        for cli in clilist:
            # Checking if the commands are show commands
            if not cli.startswith("show"):
                print("only for show commands")
                exit(1)

        # Setting the username and password for ssh login
        username = "cisco"
        password = "cisco"

        # Setting the prompt to expect after login
        prompt = host.upper() + "#"

        # Defining an escape sequence to move cursor up one line
        CURSOR_UP = "\x1b[1A"
        # Defining an escape sequence to delete a line
        DEL_LINE = "\x1b[2K"

        # Spawning a child process to run ssh command with some options
        p = pexpect.spawnu(
            f"ssh -o UserKnownhostsFile=/dev/null -o StricthostKeyChecking=no -l {username} {host}"
        )

        # Expecting password prompt from ssh
        p.expect("(assword:)")
        # Sending password to ssh
        p.sendline(password)
        p.expect(prompt)

        # Setting the window size of the child process
        p.setwinsize(24, 222)

        # Sending command to disable terminal paging
        p.sendline("terminal length 0")
        p.expect(prompt)

        # Sending command to disable terminal wrapping
        p.sendline("terminal width 0")
        p.expect(prompt)

        # Loop through the list of commands
        for cli in clilist:
            # Send the command to the process
            p.sendline(cli)

            # Wait for the prompt to appear
            p.expect(prompt)

            # Get the output from the process
            outbuffer = p.before + p.after

            # Print a header with the host and command name
            print(f"---[ XRSHOW START ]---[ {host} ]---[ {cli} ]---")

            # Print the output without the first line (which is the command itself)
            print(outbuffer.split("\n", 1)[1])

            # Move the cursor up one line
            sys.stdout.write(CURSOR_UP)

            # Delete the current line
            sys.stdout.write(DEL_LINE)

            # Print a footer with the host and command name
            print(f"---[ XRSHOW END   ]---[ {host} ]---[ {cli} ]---\n")

        # Send an exit command to the process
        p.sendline("exit")
        # Wait for the process to end
        p.expect(pexpect.EOF)

    except KeyboardInterrupt:
        print("\n-- You pressed CTRL + C --")
