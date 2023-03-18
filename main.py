# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i,0) for i in range(n)]
    for i in range(m):
        thread_index, thread_finish_time = min(threads, key=lambda x: x[1])
        output.append((thread_index, thread_finish_time))
        threads[thread_index] = (thread_index, thread_finish_time + data[i])
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(result[i][0], result[i][1])
        
if __name__ == "__main__":
    main()
