
def fifo_page_replacement(pages, nframes):
    frames = [None for i in range(nframes)]
    f = -1  # frame index
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] in frames:
            print("%d -> %-12s Hit" %(pages[i], frames))
        else:
            page_faults += 1
            f = (f + 1) % nframes
            frames[f] = pages[i]
            print("%d -> %-12s Fault" %(pages[i], frames))

    return page_faults

pages = [1, 2, 3, 4, 2, 1, 5, 6]
pf = fifo_page_replacement(pages, 3)
print("Total no. of page faults : ", pf)
