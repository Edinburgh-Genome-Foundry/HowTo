# Clean docker components

Run one or several of the commands below. Should save you a lot of space !

```
#!/bin/bash
docker stop $(docker ps -a -q)
# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi -f $(docker images -q)
# Delete dangling volumes
docker volume prune
```
