# simplehttpserver
A simple python http server, forked from https://gist.github.com/kaito834/466b0ed0ef283ceb9f49

Fix the permissions:
```
chmod +x dummy-web-server.py
```

To use in docker:

```
docker rm -f httpserver; docker run --privileged=true -ti -v $(pwd):/opt/ --name=httpserver -p 8000:8000 centos:latest /opt/dummy-web-server.py 8000
```
