### 下载安装cfssl
```shell script
yum install -y wget
wget https://pkg.cfssl.org/R1.2/cfssl_linux-amd64 -O /usr/bin/cfssl
wget https://pkg.cfssl.org/R1.2/cfssljson_linux-amd64 -O /usr/bin/cfssl-json
wget https://pkg.cfssl.org/R1.2/cfssl-certinfo_linux-amd64 -O /usr/bin/cfssl-certinfo
chmod +x /usr/bin/cfssl*
```

### CA根证书配置文件(10年有效期)
```shell script
mkdir -p /opt/certs

cat >/opt/certs/ca-csr.json <<EOF
{
    "CN": "qytca",
    "hosts": [
    ],
    "key": {
        "algo": "rsa",
        "size": 4096
    },
    "names": [
        {
            "C": "CN",
            "ST": "beijing",
            "L": "beijing",
            "O": "qytang"
        }
    ],
    "ca": {
        "expiry": "17520h"
    }
}
EOF
```

### 初始化CA
```shell script
# cfssl gencert -initca ca-csr.json 输出文本(json)结果
# cfssl-json -bare ca 把输出文本信息(json), 产生文件

cd /opt/certs/
cfssl gencert -initca ca-csr.json | cfssl-json -bare ca
~~~ 下面是输出 ~~~
2020/09/09 03:09:38 [INFO] generating a new CA key and certificate from CSR
2020/09/09 03:09:38 [INFO] generate received request
2020/09/09 03:09:38 [INFO] received CSR
2020/09/09 03:09:38 [INFO] generating key: rsa-2048
2020/09/09 03:09:39 [INFO] encoded CSR
2020/09/09 03:09:39 [INFO] signed certificate with serial number 305773733204133988374871170151725823517100191358

[root@localhost certs]# ll
总用量 16
-rw-r--r-- 1 root root 1009 9月   9 03:09 ca.csr      # 证书请求
-rw-r--r-- 1 root root  338 9月   9 03:07 ca-csr.json
-rw------- 1 root root 1675 9月   9 03:09 ca-key.pem  # 根的私钥
-rw-r--r-- 1 root root 1371 9月   9 03:09 ca.pem      # 根证书
```

### 证书模板

```shell script
# 相当于微软的证书模板
# server 服务器证书
# client 客户证书
# peer   既扮演服务器, 也扮演客户, 例如:ETCD的节点

cat >/opt/certs/ca-config.json <<EOF
{
    "signing": {
        "default": {
            "expiry": "87600h"
        },
        "profiles": {
            "server": {
                "expiry": "175200h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "server auth"
                ]
            },
            "client": {
                "expiry": "87600h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "client auth"
                ]
            },
            "peer": {
                "expiry": "87600h",
                "usages": [
                    "signing",
                    "key encipherment",
                    "server auth",
                    "client auth"
                ]
            }
        }
    }
} 
EOF
```

### Vault证书请求
```shell script
cd /opt/certs/
cat >/opt/certs/vault-csr.json <<EOF
{
    "CN": "vault",
    "hosts": [
        "127.0.0.1",
        "192.168.1.100"
    ],
    "key": {
        "algo": "rsa",
        "size": 2048
    },
    "names": [
        {
            "C": "CN",
            "ST": "beijing",
            "L": "beijing",
            "O": "qytang"
        }
    ]
}
EOF
```

### 签发证书
```shell script
cd /opt/certs/
cfssl gencert -ca=ca.pem \
              -ca-key=ca-key.pem \
              -config=ca-config.json \
              -profile=server vault-csr.json \
              |cfssl-json -bare vault

[root@localhost ~]# cd /opt/certs/
[root@localhost certs]# ll
总用量 36
-rw-r--r-- 1 root root  834 1月  30 20:16 ca-config.json
-rw-r--r-- 1 root root 1667 1月  30 20:15 ca.csr
-rw-r--r-- 1 root root  302 1月  30 20:15 ca-csr.json
-rw------- 1 root root 3247 1月  30 20:15 ca-key.pem
-rw-r--r-- 1 root root 2000 1月  30 20:15 ca.pem
-rw-r--r-- 1 root root 1029 1月  30 20:32 vault.csr
-rw-r--r-- 1 root root  301 1月  30 20:29 vault-csr.json
-rw------- 1 root root 1679 1月  30 20:32 vault-key.pem
-rw-r--r-- 1 root root 1708 1月  30 20:32 vault.pem
```

