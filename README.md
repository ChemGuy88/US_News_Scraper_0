Hello!

This project is also called "usnews", because it involves script I've written to help me sort through US News & World Report information
on schools I'm interested in.

I first copy and pasted US News' top 100 comp sci schools. I did the same for top 100 stats programs.

I wrote a script, ranksorter.py, that turns the pasted information in .txt files into python lists which are saved
in .txt files.

I wrote a second script, fetcher.py, that reads that saved list and then ueses URLLib to make a
google query for the university. The resulting page is analyzed using BeautifulSoup to extract
addresses for the universities (which US News does not do on the lists it makes). This is saved in a .txt file.

A third script, averageranker.py, the combines both the CS and stats programs .txt files into one
python list with the CS and stats ranks averaged. This is done because I'm intersted in data science, 
which is part programming and part stats, so it's reasonable to assume the best data science program would come
from a  school with strong programming and stats rankings.

This is all on python.
