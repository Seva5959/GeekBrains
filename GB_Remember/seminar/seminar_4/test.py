при 100


C:\Users\loha8\AppData\Local\Programs\Python\Python311\python.exe "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\comparsion.py"
multiprocessing.pool.RemoteTraceback:
"""
Traceback (most recent call last):
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connection.py", line 196, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\util\connection.py", line 85, in create_connection
    raise err
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\util\connection.py", line 73, in create_connection
    sock.connect(sa)
TimeoutError: [WinError 10060] Попытка установить соединение была безуспешной, т.к. от другого компьютера за требуемое время не получен нужный отклик, или было разорвано уже установленное соединение из-за неверного отклика уже подключенного компьютера

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 789, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 490, in _make_request
    raise new_e
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 466, in _make_request
    self._validate_conn(conn)
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 1095, in _validate_conn
    conn.connect()
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connection.py", line 615, in connect
    self.sock = sock = self._new_conn()
                       ^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connection.py", line 205, in _new_conn
    raise ConnectTimeoutError(
urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPSConnection object at 0x0000017FE6A0B990>, 'Connection to www.wikipedia.org timed out. (connect timeout=None)')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 843, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\util\retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.wikipedia.org', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000017FE6A0B990>, 'Connection to www.wikipedia.org timed out. (connect timeout=None)'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\pool.py", line 125, in worker
    result = (True, func(*args, **kwds))
                    ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\pool.py", line 48, in mapstar
    return list(map(*args))
           ^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\task_2.py", line 23, in download
    aboba = requests.get(url)
            ^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\adapters.py", line 688, in send
    raise ConnectTimeout(e, request=request)
requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='www.wikipedia.org', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0000017FE6A0B990>, 'Connection to www.wikipedia.org timed out. (connect timeout=None)'))
"""

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\comparsion.py", line 38, in <module>
    print(cheak_time())
          ^^^^^^^^^^^^
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\comparsion.py", line 19, in cheak_time
    time_taken_proc = task_2.psevdo_main()
                      ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\task_2.py", line 41, in psevdo_main
    pool.map(download, links)
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\pool.py", line 367, in map
    return self._map_async(func, iterable, mapstar, chunksize).get()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\multiprocessing\pool.py", line 774, in get
    raise self._value
requests.exceptions.ConnectTimeout: None: Max retries exceeded with url: / (Caused by None)

Process finished with exit code 1

при 10
C:\Users\loha8\AppData\Local\Programs\Python\Python311\python.exe "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\comparsion.py"
Traceback (most recent call last):
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 1345, in _create_direct_connection
    hosts = await self._resolve_host(host, port, traces=traces)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 989, in _resolve_host
    return await asyncio.shield(resolved_host_task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 1345, in _create_direct_connection
    hosts = await self._resolve_host(host, port, traces=traces)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 964, in _resolve_host
    await future
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 1020, in _resolve_host_with_throttle
    addrs = await self._resolver.resolve(host, port, family=self._family)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\resolver.py", line 36, in resolve
    infos = await self._loop.getaddrinfo(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\asyncio\base_events.py", line 868, in getaddrinfo
    return await self.run_in_executor(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\concurrent\futures\thread.py", line 58, in run
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\socket.py", line 962, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno 11004] getaddrinfo failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\comparsion.py", line 38, in <module>
    print(cheak_time())
          ^^^^^^^^^^^^
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\comparsion.py", line 13, in cheak_time
    time_tiken_asyn = task_3.psevdo_main()
                      ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\task_3.py", line 36, in psevdo_main
    asyncio.run(main())
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\asyncio\runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\asyncio\runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\asyncio\base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\task_3.py", line 32, in main
    await asyncio.gather(*tasks)
  File "C:\Users\loha8\OneDrive\Рабочий стол\GeekBrains\GB_Remember\seminar\seminar_4\task_3.py", line 22, in download
    async with session.get(url) as response:
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\client.py", line 1423, in __aenter__
    self._resp: _RetType = await self._coro
                           ^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\client.py", line 701, in _request
    conn = await self._connector.connect(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 544, in connect
    proto = await self._create_connection(req, traces, timeout)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 1050, in _create_connection
    _, proto = await self._create_direct_connection(req, traces, timeout)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\loha8\AppData\Local\Programs\Python\Python311\Lib\site-packages\aiohttp\connector.py", line 1351, in _create_direct_connection
    raise ClientConnectorDNSError(req.connection_key, exc) from exc
aiohttp.client_exceptions.ClientConnectorDNSError: Cannot connect to host github.com:443 ssl:default [getaddrinfo failed]

Process finished with exit code 1
