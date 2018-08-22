# Step 1: Build all images

```
$ ./scripts/init.sh
```

This will give us the rabbit mq setup, django, and celery server.

# Vola, u r all set!

Try `curl localhost:8080/foo/` and you should see the result in the worker terminal
