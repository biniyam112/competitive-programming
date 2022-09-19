cases = int(input())
for _ in range(cases):
    input()
    notes = input().split()
    notes = [int(x) for x in notes]
    note_s = set()
    for i in range(len(notes)):
        if notes[i] in note_s:
            note_s.add(notes[i]+1)
        else:
            note_s.add(notes[i])
    print(len(note_s))
