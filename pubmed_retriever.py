from Bio import Entrez
import csv
import os


# Identify to NCBI
Entrez.email = "you@email.com"

# Build PubMed query
def build_query(nanomaterial, application):

    query = (
        f'"{nanomaterial}"[Title/Abstract] '
        f'AND '
        f'{application}[Title/Abstract]'
    )

    return query


# Search PubMed
def search_pubmed(
    query,
    max_results=3,
    start=0,
    sort="date"
):

    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retstart=start,
        retmax=max_results,
        sort=sort
    )

    record = Entrez.read(handle)

    handle.close()

    id_list = record["IdList"]

    total_results = record["Count"]

    return id_list, total_results


# Fetch paper information
def fetch_paper(pmid):

    handle = Entrez.efetch(
        db="pubmed",
        id=pmid,
        retmode="xml"
    )

    record = Entrez.read(handle)

    handle.close()

    article = record["PubmedArticle"][0]

    medline_citation = article["MedlineCitation"]

    article_data = medline_citation["Article"]


    # Extract title

    title = str(
        article_data["ArticleTitle"]
    )


    # Extract abstract

    if "Abstract" in article_data:

        abstract_parts = (
            article_data["Abstract"]["AbstractText"]
        )

        abstract = " ".join(
            str(part)
            for part in abstract_parts
        )

    else:

        abstract = ""


    # Extract authors

    authors = []

    if "AuthorList" in article_data:

        author_list = article_data["AuthorList"]

        for author in author_list:

            last_name = author.get(
                "LastName",
                ""
            )

            fore_name = author.get(
                "ForeName",
                ""
            )

            full_name = (
                fore_name
                + " "
                + last_name
            )

            authors.append(
                full_name.strip()
            )


    # Extract journal

    journal = article_data["Journal"]["Title"]


    # Extract publication year

    pub_date = (
        article_data["Journal"]
        ["JournalIssue"]
        ["PubDate"]
    )

    publication_year = pub_date.get(
        "Year",
        ""
    )


    # Extract DOI

    pubmed_data = article["PubmedData"]

    article_id_list = (
        pubmed_data["ArticleIdList"]
    )

    doi = ""

    for article_id in article_id_list:

        if article_id.attributes.get(
            "IdType"
        ) == "doi":

            doi = str(article_id)


    # Create paper dictionary

    paper = {

        "pmid": pmid,

        "title": title,

        "abstract": abstract,

        "authors": "; ".join(authors),

        "journal": journal,

        "publication_year": publication_year,

        "doi": doi

    }


    return paper


# Save papers to CSV

def save_to_csv(
    papers,
    filename="pubmed_results.csv"
):

    fieldnames = [

        "pmid",

        "title",

        "abstract",

        "authors",

        "journal",

        "publication_year",

        "doi"

    ]


    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(papers)


# Main program

def main():

    # Define search concepts

    nanomaterial = "gold nanoparticles"

    application = "biosensor"


    # Build PubMed query

    query = build_query(
        nanomaterial,
        application
    )


    print("Generated query:")

    print(query)


    # Search PubMed

    pmids, total_results = search_pubmed(
        query=query,
        max_results=3,
        start=0,
        sort="date"
    )


    print(
        "\nTotal matching results:",
        total_results
    )


    # Store all retrieved papers

    papers = []


    # Fetch information for each paper

    for pmid in pmids:

        paper = fetch_paper(pmid)

        papers.append(paper)


    # Display retrieved papers

    for paper in papers:

        print(
            "\n"
            + "=" * 80
        )

        print(
            "PMID:",
            paper["pmid"]
        )

        print(
            "\nTITLE:",
            paper["title"]
        )

        print(
            "\nAUTHORS:",
            paper["authors"]
        )

        print(
            "\nJOURNAL:",
            paper["journal"]
        )

        print(
            "\nPUBLICATION YEAR:",
            paper["publication_year"]
        )

        print(
            "\nDOI:",
            paper["doi"]
        )

        print("\nABSTRACT:")

        print(
            paper["abstract"]
        )


    # Save results to CSV

    output_filename = "pubmed_results.csv"

    save_to_csv(
        papers,
        output_filename
    )


    print(
        "\n"
        + "=" * 80
    )

    print(
        "Papers saved to:",
        output_filename
    )

    print(
        "Saved at:",
        os.path.abspath(
            output_filename
        )
    )


# Run the program

if __name__ == "__main__":

    main()