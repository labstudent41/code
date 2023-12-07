
def lru_page_replacement(pages, nframes):
    frames = ['' for i in range(nframes)]
    f = -1  # frame index
    page_faults = 0

    # To get least recent value i.e. oldest used value,
    reversed_pages = pages[::-1]
    # is required. It will be later used with list.index(item)
    # as it only returns the first index while we want the last one.

    for i in range(len(pages)):
        if pages[i] in frames:
            print("%d -> %-12s Hit" %(pages[i], frames))
            continue

        page_faults += 1
        f = (f + 1) % nframes

        if frames[f] != '':
            old = [reversed_pages[-i:].index(frames[j]) for j in range(nframes)]
            f = old.index(max(old))

        frames[f] = pages[i]
        print("%d -> %-12s Fault" %(pages[i], frames))

    return page_faults

pages = [1, 2, 3, 4, 2, 1, 5, 6]
pf = lru_page_replacement(pages, 3)
print("Total no. of page faults : ", pf)
