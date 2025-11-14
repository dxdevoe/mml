# Step 1: edit papers.html with new papers
# Step 2: run papers_convert.py
# Step 3: move papers-insert.js to the "js" directory

with open('papers.html') as f_in:
    with open('papers-insert.js', 'w') as f_out:
        f_out.write("document.write('\\\n")
        for line in f_in:
            f_out.write(line.strip() + '\\\n')
        f_out.write("\\\n');")



