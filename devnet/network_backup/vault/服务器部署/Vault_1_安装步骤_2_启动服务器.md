# 创建目录，配置创建配置文件
```shell script
mkdir -p /vault/data
cd /vault
cat >/vault/config.hcl <<EOF
storage "raft" {
  path    = "/vault/data"
  node_id = "qytang-node1"
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_cert_file = "/opt/certs/vault.pem"
  tls_key_file = "/opt/certs/vault-key.pem"
  tls_disable = "false"
}

api_addr = "https://192.168.1.100:8200"
cluster_addr = "https://192.168.1.100:8201"
ui = true
EOF
```

### 启动服务器
```shell script
vault server -config=/vault/config.hcl
------------------下面是输出----------------------------
==> Vault server configuration:

             Api Address: https://127.0.0.1:8200
                     Cgo: disabled
         Cluster Address: https://127.0.0.1:8201
              Go Version: go1.15.7
              Listener 1: tcp (addr: "127.0.0.1:8200", cluster address: "127.0.0.1:8201", max_request_duration: "1m30s", max_request_size: "33554432", tls: "enabled")
               Log Level: info
                   Mlock: supported: true, enabled: true
           Recovery Mode: false
                 Storage: raft (HA available)
                 Version: Vault v1.6.2
             Version Sha: be65a227ef2e80f8588b3b13584b5c0d9238c1d7

==> Vault server started! Log data will stream in below:

2021-01-30T20:59:55.998-0500 [INFO]  proxy environment: http_proxy= https_proxy= no_proxy=
```