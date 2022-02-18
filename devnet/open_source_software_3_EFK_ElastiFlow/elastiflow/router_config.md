### CSR1配置
```shell
flow record Qytang-Record
 match ipv4 source address
 match ipv4 destination address
 match ipv4 protocol
 match transport destination-port
 match transport source-port
 match interface input
 collect counter bytes

flow exporter Netflow-Exporter
 destination 192.168.1.100
 transport udp 2055
 template data timeout 30

flow monitor Monitor1
 exporter Netflow-Exporter
 record Qytang-Record
!
interface GigabitEthernet1
 ip flow monitor Monitor1 input
 ip flow monitor Monitor1 output
```
