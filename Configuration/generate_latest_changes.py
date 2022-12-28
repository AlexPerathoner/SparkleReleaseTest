
# look at file Release_Notes.md, take all bullet points under the top header. Also return the value of the first and second headers
# the format in the header: # version - title

def get_latest_release_notes():
    with open('../Release_Notes.md', 'r') as f:
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
                previous_verion = line.strip().split(' - ')[0].replace('# ', 'v')
                break
        return title, latest_version, previous_verion, notes

if __name__ == '__main__':
    title, latest_version, previous_verion, notes = get_latest_release_notes()
    # write each value to a file
    with open('../latest_version.txt', 'w') as f:
        f.write(latest_version)
    with open('../previous_verion.txt', 'w') as f:
        f.write(previous_verion)
    with open('../latest_changes.txt', 'w') as f:
        f.write(notes)
    with open('../title.txt', 'w') as f:
        f.write(title)