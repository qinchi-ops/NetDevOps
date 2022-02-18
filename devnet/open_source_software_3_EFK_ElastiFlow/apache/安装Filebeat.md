#### 安装filebeat
```shell
wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.8.1-x86_64.rpm

rpm -ivh filebeat-7.8.1-x86_64.rpm
```

#### 激活apache模块
```shell
[root@Apache_PHP yum.repos.d]# cd /etc/filebeat/modules.d/

[root@Apache_PHP modules.d]# ls
activemq.yml.disabled     cyberark.yml.disabled          icinga.yml.disabled     mssql.yml.disabled            pensando.yml.disabled    suricata.yml.disabled
apache.yml.disabled       cylance.yml.disabled           iis.yml.disabled        mysqlenterprise.yml.disabled  postgresql.yml.disabled  system.yml.disabled
auditd.yml.disabled       elasticsearch.yml.disabled     imperva.yml.disabled    mysql.yml.disabled            proofpoint.yml.disabled  threatintel.yml.disabled
aws.yml.disabled          envoyproxy.yml.disabled        infoblox.yml.disabled   nats.yml.disabled             rabbitmq.yml.disabled    tomcat.yml.disabled
azure.yml.disabled        f5.yml.disabled                iptables.yml.disabled   netflow.yml.disabled          radware.yml.disabled     traefik.yml.disabled
barracuda.yml.disabled    fortinet.yml.disabled          juniper.yml.disabled    netscout.yml.disabled         redis.yml.disabled       zeek.yml.disabled
bluecoat.yml.disabled     gcp.yml.disabled               kafka.yml.disabled      nginx.yml.disabled            santa.yml.disabled       zoom.yml.disabled
cef.yml.disabled          googlecloud.yml.disabled       kibana.yml.disabled     o365.yml.disabled             snort.yml.disabled       zscaler.yml.disabled
checkpoint.yml.disabled   google_workspace.yml.disabled  logstash.yml.disabled   okta.yml.disabled             snyk.yml.disabled
cisco.yml.disabled        gsuite.yml.disabled            microsoft.yml.disabled  oracle.yml.disabled           sonicwall.yml.disabled
coredns.yml.disabled      haproxy.yml.disabled           misp.yml.disabled       osquery.yml.disabled          sophos.yml.disabled
crowdstrike.yml.disabled  ibmmq.yml.disabled             mongodb.yml.disabled    panw.yml.disabled             squid.yml.disabled

[root@Apache_PHP modules.d]# mv apache.yml.disabled apache.yml
```

#### 修改配置文件
```shell
[root@Apache_PHP filebeat]# pwd
/etc/filebeat

[root@Apache_PHP filebeat]# ls
fields.yml  filebeat.reference.yml  filebeat.yml  filebeat.yml-bak  modules.d

[root@Apache_PHP filebeat]# mv filebeat.yml filebeat.yml-bak

[root@Apache_PHP filebeat]# vim filebeat.yml

~~~具体内容如下~~~
filebeat.config:
  modules:
    path: ${path.config}/modules.d/*.yml
    reload.enabled: false

processors:
  - add_cloud_metadata: ~
  - add_docker_metadata: ~

output.elasticsearch:
  hosts:
    - 192.168.1.100:9200
  index: qytang-apache-%{+yyyy.MM.dd}

setup.kibana.host: "http://192.168.1.100:5601"
setup.template.name: "qytang-apache"
setup.template.pattern: "qytang-apache-*"
setup.ilm.enabled: false
```

#### 激活filebeat
```shell
systemctl enable filebeat
systemctl start filebeat
```

#### 查看filebeat状态
```shell
systemctl status filebeat
```
