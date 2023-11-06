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
