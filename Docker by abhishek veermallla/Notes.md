Containers can be created in two ways 
1. on the top of vm's
2. on the top of physical servers
Now a days people prefer to use model 2, bacause when you maintain the physical server you have to deal with a lot , so there is a dedicated team for it (refer 1 pic)

what is container ? It's is a collection of application + system dependencies + libraries
why are conatiners light in weight in nature ? bcoz they don't have a complete os and they use the resources from the os they are running on

Life cycle of docker ?
write a docker file and execute this file and to create a image and execute this to create a container. There is something called as docker engine which collects all the inputs 
eg: to create image from docker file we use build and to create container from image we use run

Docker is very much dependent on docker engine which is prone to single point of failure,layers. To avoid this Buildah, In buildah write shell script and put all the buildah commands in the shell script and it would create a image , so this can create docker images as it supports docker.

https://github.com/manogna-chinta/Docker-Zero-to-Hero

Docker deomon runs with root user and it's monolithic process

Difference between Entrypoint and cmd ?

Both are used to start cmd ,whenevr somebody run docker both entrypoint and cmd executes as starting commands, But Entrypoint is something that you cannot change, where as cmd is configurable during the runtime

Multistage builds are :
Multistage builds , distroless builds

A distroless image is a light-weight docker image that will have only run-time environments

* Big advantage for distroless image is security

* what is one of the production issue that you faced with docker? and how did you solved it

previously we're using ubuntu base images which were exposed to some vulnerabilities so we moved to distroless images 
eg: if you using python application in your org. we moved to python distroless image which only had python run time which usuallly don't have find,ls curl it was providing us highest level of security and we after implementing distroless images we can say our application is not prone to any o.s related issues
(Revise docker multi stage builds if needed)
