from requests import get
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter
n = 1
def html_download_and_write(url):
    response = get(url=url)
    return response.text

def write_html(i,code):
    with open(f"Tilshunosh_sinonims/{i+1}.html","w") as f:
        f.write(code)
if __name__ == '__main__':
    urls = [f"https://tilshunos.com/sinonims/{i}/" for i in range(1,401)]
    start = perf_counter()
    with ThreadPoolExecutor() as executor:
        result= list(executor.map(html_download_and_write,urls))
    for i, html_code in enumerate(result):
        write_html(i,html_code)
    stop = perf_counter()
    timee = stop - start
    print(f'400 sahifa {timee: .2f} sekundda yuklab olindi.')

# 400 sahifa  8.47 sekundda yuklab olindi.