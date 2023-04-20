import csv
import asyncio
from multiprocessing import Pool

async def write_to_csv(filename, data):
    async with asyncio.Lock():
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

def process_csv_chunk(args):
    filename, data = args
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    start, end, data = data
    rows[start:end] = data
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

async def write_to_csv_parallel(filename, chunks):
    pool = Pool()
    args = [(filename, chunk) for chunk in chunks]
    pool.map(process_csv_chunk, args)
    pool.close()
    pool.join()

async def write_csv_parallel():
    filename = 'example.csv'
    data = [[i, i + 1, i + 2] for i in range(100)]
    chunk_size = 10
    chunks = [(i, i + chunk_size, data[i:i+chunk_size]) for i in range(0, len(data), chunk_size)]
    tasks = []
    for chunk in chunks:
        task = asyncio.ensure_future(write_to_csv(filename, chunk[2]))
        tasks.append(task)
    await asyncio.gather(*tasks)
    await write_to_csv_parallel(filename, chunks)

asyncio.run(write_csv_parallel())
