#!/usr/bin/python3

# Author : Hemant Sharma

import os
import xrshow
import asyncio
import subprocess
from time import perf_counter


# This function runs a shell command on a given host and returns the output and the host name
async def getoutput(host, showcmd, limit):
    # Join all the commands for the host with spaces
    allcmds = " ".join(showcmd[host])

    # Format the shell command with the host and commands
    shellcmd = f"python3 xrshowcli -n {host} -c {allcmds}"

    # Use a semaphore to limit the number of concurrent tasks
    async with limit:
        try:
            # Create an asynchronous subprocess to run the shell command and capture the output and error streams
            n = await asyncio.create_subprocess_shell(
                shellcmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            # Print some information about the process ids of the parent and child processes
            print(
                f"Collecting info from {host:<20} Parent.pid: {str(os.getpid()):<10} Child.pid: {str(n.pid):<10}"
            )
            # Wait for the subprocess to finish and get the output and error code
            (noutput, code) = await n.communicate()
            # Wait for the subprocess to terminate
            await n.wait()
        except:
            # Handle any exception that may occur during the subprocess execution
            print(f"xrshowcli did not work for {host}")

    # Return the decoded output and the host name
    return noutput.decode("utf-8"), host


async def main():
    # A list of hosts to run commands on
    hosts = ["pe1", "p2", "p3", "p4", "pe5", "p6", "p7", "p8"]

    # A dictionary to store the commands for each host
    showcmd = {}
    for host in hosts:
        # Initialize an empty list for each host
        # And add commands to it
        showcmd[host] = []
        showcmd[host].append(f'"show version"')
        showcmd[host].append(f'"show platform"')
        showcmd[host].append(f'"show isis adjacency"')

    # Create a semaphore object with a value of 2
    limit = asyncio.Semaphore(2)

    # Create a list of tasks using getoutput function for each host
    tasks = [asyncio.create_task(getoutput(host, showcmd, limit)) for host in hosts]

    # Wait for all tasks to complete and collect their results
    results = await asyncio.gather(*tasks)

    print("=" * 80)

    for result in results:
        print("-" * 80)
        print(f"Host: {result[1]}")
        print("-" * 80)
        print("Output Displayed:")
        print("-" * 80)
        print(f"{result[0]}")
        print("-" * 80)


if __name__ == "__main__":
    start = perf_counter()

    asyncio.run(main())

    stop = perf_counter()
    print(f"Time taken for the program run: {stop - start:0.2f} seconds")
