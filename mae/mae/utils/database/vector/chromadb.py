import os
from typing import Union
import chromadb
from langchain_chroma import Chroma


def create_chroma_db_conn(db_path: Union[str, None] = '.', collection_name: str = 'mofa', *args, **kwargs):
    """
    Create a Chroma database connection and return the collection.

    :param db_path: Database path, defaults to current directory ('.').
    :param collection_name: Collection name, defaults to 'default'.
    :param args: Other positional arguments.
    :param kwargs: Other keyword arguments.
    :return: Chroma collection connection.
    """
    try:
        if db_path is not None:
            client = chromadb.PersistentClient(path=db_path)
        else:
            client = chromadb.Client()
        conn = client.create_collection(name=collection_name, **kwargs)
        return conn
    except Exception as e:
        raise RuntimeError("Error creating Chroma DB connection.")
def add(conn, documents: list, ids: list, *args, **kwargs):
    """
    Add documents to the ChromaDB database with corresponding IDs.

    :param conn: ChromaDB connection instance.
    :param documents: List of documents to be added to the database.
    :param ids: List of IDs corresponding to the documents. Must be the same length as the documents list.
    :param args: Other positional arguments.
    :param kwargs: Other keyword arguments for the add operation.
    :raises ValueError: If the length of documents and ids is not equal.
    """
    if len(documents) != len(ids):
        raise ValueError("Length of documents and ids must be equal.")
    ids = [str(id) if not isinstance(id, str) else id for id in ids]
    conn.add(ids=ids, documents=documents, **kwargs)


def query(conn, query_texts: list, num_results: int = 3, *args, **kwargs):
    """
    Query documents from the ChromaDB database based on the provided query texts.

    :param conn: ChromaDB connection instance.
    :param query_texts: List of query texts to search for in the database.
    :param num_results: Number of results to return per query, defaults to 3.
    :param args: Other positional arguments.
    :param kwargs: Other keyword arguments for the query operation.
    :return: Query results from the database.
    """
    query_texts = [str(text) if not isinstance(text, str) else text for text in query_texts]
    results = conn.query(
        query_texts=query_texts,  # Chroma will embed this for you
        n_results=num_results,
        **kwargs
    )
    return results


def delete(conn, ids: list, *args, **kwargs):
    """
    Delete documents from the ChromaDB database based on the provided IDs.

    :param conn: ChromaDB connection instance.
    :param ids: List of document IDs to be deleted.
    :param args: Other positional arguments.
    :param kwargs: Other keyword arguments for the delete operation.
    """
    ids = [str(id) if not isinstance(id, str) else id for id in ids]
    conn.delete(ids=ids, **kwargs)


def update(conn, documents: list, ids: list, *args, **kwargs):
    """
    Update or upsert documents in the ChromaDB database with corresponding IDs.

    :param conn: ChromaDB connection instance.
    :param documents: List of documents to update or insert into the database.
    :param ids: List of IDs corresponding to the documents.
    :param args: Other positional arguments.
    :param kwargs: Other keyword arguments for the upsert operation.
    """
    ids = [str(id) if not isinstance(id, str) else id for id in ids]
    conn.upsert(ids=ids, documents=documents, **kwargs)

def create_chroma_db_conn_with_langchain(embedding,db_path: Union[str, None] = '.', collection_name: str = 'mofa', *args, **kwargs):
    vector_store = Chroma(
        collection_name=collection_name,
        persist_directory=db_path,
        embedding_function=embedding,
        **kwargs
    )
    return vector_store
def add_with_langchain(vector_conn,documents: list, ids: list):
    ids = [str(id) if not isinstance(id, str) else id for id in ids]
    vector_conn.add_documents(documents=documents, ids=ids)

def update_with_langchain(vector_conn,documents: list, ids: list):
    ids = [str(id) if not isinstance(id, str) else id for id in ids]
    vector_conn.update_documents(documents=documents, ids=ids)

def delete_with_langchain(vector_conn,ids: list):
    ids = [str(id) if not isinstance(id, str) else id for id in ids]

    vector_conn.delete(ids=ids)


def query_with_langchain(vector_conn,query_texts: str,embedding, num_results: int = 3,search_type:str='similarity_search',**kwargs)->list[str]:
    result_data = []
    if search_type == 'similarity_search':
        results = vector_conn.similarity_search_by_vector(
            embedding=embedding.embed_query(query_texts), k=num_results,**kwargs
        )
    elif search_type == 'similarity_score':
        results = vector_conn.similarity_search_with_score(
            query_texts, k=num_results, **kwargs
        )
    else:
        results = vector_conn.similarity_search(
            query_texts, k=num_results, **kwargs
        )
    for doc in results:
        result_data.append(doc.page_content)
    return result_data
