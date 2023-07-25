from transformers import pipeline
from bs4 import BeautifulSoup
import requests



def summarizerWithURL(urllink):
    summarizer = pipeline("summarization")

    r = requests.get(urllink)

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all(['h1', 'p'])
    text = [result.text for result in results]
    text = ' '.join(text)



    text = text.replace('.', '.<eos>')
    text = text.replace('?', '?<eos>')
    text = text.replace('!', '!<eos>')


    sentences = text.split('<eos>')
    
    max_chunk = 500
    current_chunk = 0 
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            # print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    # print(chunks)
    res = summarizer(chunks, max_length=200, min_length=20, do_sample=False)


    text = ' '.join([summ['summary_text'] for summ in res])
    return text




def summarizerWithWord(text):
    summarizer = pipeline("summarization")


    text = text.replace('.', '.<eos>')
    text = text.replace('?', '?<eos>')
    text = text.replace('!', '!<eos>')


    sentences = text.split('<eos>')
    max_chunk = 600
    current_chunk = 0 
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            # print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    
    res = summarizer(chunks, max_length=100, min_length=20, do_sample=False)


    summ = ' '.join([summ['summary_text'] for summ in res])
    return summ



