import subprocess

def update_repository(repo_path, branch='main'):
    subprocess.run(['git', '-C', repo_path, 'fetch'])

    local_commit = subprocess.run(['git', '-C', repo_path, 'rev-parse', f'{branch}'], capture_output=True, text=True).stdout.strip()
    remote_commit = subprocess.run(['git', '-C', repo_path, 'rev-parse', f'origin/{branch}'], capture_output=True, text=True).stdout.strip()

    if local_commit != remote_commit:
        subprocess.run(['git', '-C', repo_path, 'reset', '--hard', f'origin/{branch}'])
        print("[+] Updated bruhlib!")
    else:
        print("[+] bruhlib is up to date")


if __name__ == '__main__':
    import os
    import sys

    repo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    update_repository(repo_path)