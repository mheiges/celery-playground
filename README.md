
#### On time setup
      $ virtualenv-2.7 ~/python27
      $ pip install celery

#### Each time, Terminal 1, start rabbitmq server

Provision and start [vagrant-rabbitmq](https://github.com/mheiges/vagrant-rabbitmq) virtual machine.

OR, if running local server

    $ sudo rabbitmq-server

#### Each time, Terminal 2, start worker

    $ source ~/python27/bin/activate
    $ cd celeryproject/
    $ celery -A framework worker -l info

#### Each time, Terminal 3, Run individual tasks

    $ source ~/python27/bin/activate
    $ cd celeryproject/
    $ ./runtasks 
