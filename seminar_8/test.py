from pathlib import  Path

current_dir = Path.cwd()
seminar_dir = current_dir / 'seminar_8'
parent_dir = seminar_dir.parent
print(seminar_dir )
print(parent_dir)