# PubMed\_literature\_retriever

A Python-based PubMed literature retrieval tool using the NCBI Entrez API, with configurable queries, pagination, sorting, and metadata extraction.



\## Features



\* Search PubMed using customizable search queries

\* Retrieve a specified number of papers

\* Retrieve different batches of results using pagination

\* Sort results using supported PubMed sorting options

\* Extract key metadata from retrieved papers:



&#x20; \* PMID

&#x20; \* Title

&#x20; \* Abstract

&#x20; \* Authors

&#x20; \* Journal

&#x20; \* Publication year

&#x20; \* DOI

\* Display retrieved literature in the command line

\* Export retrieved paper metadata to a CSV file



\## Current Workflow



```text

Search Query

&#x20;    ↓

PubMed / NCBI Entrez API

&#x20;    ↓

Retrieve PMIDs

&#x20;    ↓

Fetch Article Records

&#x20;    ↓

Extract Metadata

&#x20;    ↓

Display Results

```



\## Project Structure



```text

pubmed-literature-retriever/

│

├── pubmed\_retriever.py

├── requirements.txt

└── README.md

```



\## Requirements



\* Python 3.x

\* An email address for use with the NCBI Entrez API



\## Installation



Clone the repository:



```bash

git clone <YOUR\_REPOSITORY\_URL>

```



Navigate into the project directory:



```bash

cd pubmed-literature-retriever

```



Install the required dependency:



```bash

pip install -r requirements.txt

```



\## Before Running



Open `pubmed\_retriever.py` and replace:



```python

Entrez.email = "you@email.com"

```



with your own email address:



```python

Entrez.email = "your.email@example.com"

```



NCBI recommends providing an email address when using the Entrez programming utilities.



\## Customizing the Search



The search query can be changed in the main program.



For example:



```python

query = "gold nanoparticles biosensor"

```



can be changed to:



```python

query = "silver nanoparticles drug delivery"

```



or:



```python

query = "nanomaterials cancer therapy"

```



The query is passed to PubMed through the Entrez API.



\## Controlling the Number of Results



The number of papers retrieved can be changed using:



```python

max\_results=3

```



For example:



```python

pmids, total\_results = search\_pubmed(

&#x20;   query=query,

&#x20;   max\_results=10,

&#x20;   start=0,

&#x20;   sort="date"

)

```



This retrieves 10 papers.



\## Pagination



The `start` parameter controls where retrieval begins within the PubMed result set.



```python

start=0

```



retrieves the first batch of results.



For example, if:



```python

max\_results=3

```



then:



```text

start=0 → Results 1–3

start=3 → Results 4–6

start=6 → Results 7–9

start=9 → Results 10–12

```



For example:



```python

pmids, total\_results = search\_pubmed(

&#x20;   query=query,

&#x20;   max\_results=3,

&#x20;   start=6,

&#x20;   sort="date"

)

```



retrieves the third batch of three results.



In the current version, the `start` value must be changed manually. 



\## Sorting Results



The `sort` parameter controls the ordering of PubMed search results.



For example:



```python

sort="date"

```



retrieves results sorted by publication date.



Alternatively:



```python

sort="relevance"

```



retrieves results according to relevance-based ordering.



Example:



```python

pmids, total\_results = search\_pubmed(

&#x20;   query=query,

&#x20;   max\_results=5,

&#x20;   start=0,

&#x20;   sort="date"

)

```



The sorting parameter can be changed according to the supported PubMed sorting options.



\## Retrieved Metadata



For each paper, the tool currently extracts:



\- PMID

\- Title

\- Abstract

\- Authors

\- Journal

\- Publication year

\- DOI



A retrieved paper is stored as a Python dictionary:



```python

paper = {

&#x20;   "pmid": pmid,

&#x20;   "title": title,

&#x20;   "abstract": abstract,

&#x20;   "authors": authors,

&#x20;   "journal": journal,

&#x20;   "publication\_year": publication\_year,

&#x20;   "doi": doi

}



This structure makes the retrieved literature easier to process later.



\## Example Output



```text

================================================================================



PMID: 12345678



TITLE: Example Research Article



AUTHORS: \['Author One', 'Author Two']



JOURNAL: Example Journal



PUBLICATION YEAR: 2025



DOI: 10.xxxx/example.doi



ABSTRACT:



This is the abstract of the retrieved research article...

```



\### CSV Export



```markdown

\## CSV Export



Retrieved papers are automatically exported to:



```text

pubmed\_results.csv



\## Reproducibility



To reproduce the results:



1\. Clone the repository.

2\. Install the required dependencies.

3\. Add your email address to the `Entrez.email` variable.

4\. Modify the search query if desired.

5\. Set the number of results using `max\_results`.

6\. Set the starting position using `start`.

7\. Select the sorting method using `sort`.

8\. Run the Python script.



The main parameters that can be changed are:



```python

query

max\_results

start

sort

```



For example:



```python

query = "gold nanoparticles biosensor"



pmids, total\_results = search\_pubmed(

&#x20;   query=query,

&#x20;   max\_results=5,

&#x20;   start=0,

&#x20;   sort="date"

)

```



This searches PubMed for the specified query and retrieves five results beginning from the first result, sorted by date.







\### This version currently requires the user to manually:



\* Write or modify the search query

\* Set the number of results

\* Change the pagination position

\* Select the sorting method



