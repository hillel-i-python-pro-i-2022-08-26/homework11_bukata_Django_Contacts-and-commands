FROM python:3.10
#image on which we lean on( name of libr and its version)
# changebale enviramant

# its created by us variable environment
ENV PYTHONUNBUFFERED=1

# ARG its also variable environment actve only at the moment of assembly
#and in it we can set the value of a variable and use rhis var (need it when we use var offten)
ARG WORKDIR=/wd
ARG USER=user

# workdir its working derictory, from which we implam comman (in terminal)
WORKDIR ${WORKDIR}
# here we use command on bash
# creat user without password and its directory
RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}


# here we updated needed libraries
RUN apt update && apt upgrade -y
# than we copy files from project to ressable the image
# to know what to copy we need file context of ressamble docker-compose.yml
COPY --chown=${USER} requirements.txt requirements.txt
# firstly we copy files requirements and than copy all others

#than install all what in req file
# always start coping with requerements and than all others !!!!
# with the logic% the less changable should be copy first, than midl frequent chang, max change
RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

#than copy all others, and in it we show that new owner its USER
# we make copy of all needed file (we not copy all folder together  its make risk for requerements)
# this is midle change.
COPY --chown=${USER} --chmod=755 ./docker/app/start.sh /start.sh
COPY --chown=${USER} --chmod=755 ./docker/app/entrypoint.sh /entrypoint.sh

COPY --chown=${USER} ./apps apps
COPY --chown=${USER} ./core core
COPY --chown=${USER} ./Makefile Makefile
COPY --chown=${USER} ./manage.py manage.py
#COPY --chown=${USER} ./application application

# here we reconnect to created user and we act on behaf of the user
USER ${USER}

#here we say that we want to open port 8000
# here we put it just for info its not part of cod its for understanding where will be launched in which port

EXPOSE 8000

# here we show what to run in which system
# this is max change.
ENTRYPOINT ["/entrypoint.sh"]
#ENTRYPOINT ["python", "manage.py"]

# its command ( lined to docker-compose): to listen from all sources on the 8000 port
#CMD ["runserver", "0.0.0.0:8000"]
CMD ["/start.sh"]
