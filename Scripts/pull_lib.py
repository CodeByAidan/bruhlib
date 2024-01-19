"""
Script to pull the latest version of bruhlib from the remote repository.

Just run it anywhere, it will find the repository and pull the latest version.
"""
import os
import subprocess


def update_repository(repo_path, branch="main"):
    git_version_process = subprocess.run(
        ["git", "--version"], capture_output=True, text=True
    )

    if git_version_process.returncode != 0:
        raise RuntimeError("Git is not installed! Please install git and try again.")
    subprocess.run(["git", "-C", repo_path, "fetch"])

    local_commit = subprocess.run(
        ["git", "-C", repo_path, "rev-parse", f"{branch}"],
        capture_output=True,
        text=True,
    ).stdout.strip()
    remote_commit = subprocess.run(
        ["git", "-C", repo_path, "rev-parse", f"origin/{branch}"],
        capture_output=True,
        text=True,
    ).stdout.strip()

    if local_commit != remote_commit:
        subprocess.run(["git", "-C", repo_path, "reset", "--hard", f"origin/{branch}"])
        print("[+] Updated bruhlib!")
    else:
        print("[+] bruhlib is up to date")


if __name__ == "__main__":
    repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    update_repository(repo_path)
