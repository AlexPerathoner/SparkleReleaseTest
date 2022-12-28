
# look at file Release_Notes.md, take all bullet points under the top header. Also return the value of the first and second headers
# the format in the header: # version - title

def get_latest_release_notes():
    with open('Release_Notes.md', 'r') as f:
        lines = f.readlines()
        first_header = lines[0].strip()
        title = first_header.split(' - ')[1]
        latest_version = first_header.split(' - ')[0].replace('# ', 'v')
        lines = lines[1:]
        notes = ""
        for line in lines:
            if line.strip().startswith('*'):
                notes += line.strip() + "\n"
            elif line.strip().startswith('#'):
                break
        return title, latest_version, notes

if __name__ == '__main__':
    title, latest_version, notes = get_latest_release_notes()
    print(title, latest_version, notes, sep='\n')
    # write each value to a file
    with open('new_version', 'w') as f:
        f.write(latest_version)
    with open('latest_changes', 'w') as f:
        f.write(notes)
    with open('title', 'w') as f:
        f.write(title)