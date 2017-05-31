# mqqt

tests with mqqt and qos

After `docker-compose up` try `docker stop queue_recv` and `docker start queue_recv` in another terminal.
Missed messages should be received after the receiver is connected again.
