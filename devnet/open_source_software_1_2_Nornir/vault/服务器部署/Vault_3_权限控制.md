### 参考文档
```shell script
https://learn.hashicorp.com/tutorials/vault/getting-started-policies?in=vault/getting-started
```

### 设置环境变量[root]
```shell script
export VAULT_TOKEN="s.LvOvI2DEhkzsxnK87mcQ0zS7"
```

### 创建secret engine
```shell script
vault secrets enable -path=qytang/ kv-v2
```

### 写入Nornir需要的kv
```shell script
vault kv put qytang/cisco_ios/cred username=admin password=Cisc0123

---------下面是输出---------------

Key              Value
---              -----
created_time     2021-01-31T13:10:58.618740082Z
deletion_time    n/a
destroyed        false
version          1

vault kv put qytang/cisco_asa/cred username=admin password=Cisc0123 secret=Cisc0123

---------下面是输出---------------

Key              Value
---              -----
created_time     2021-01-31T13:11:12.301505394Z
deletion_time    n/a
destroyed        false
version          1
```

### 创建控制策略
```shell script
vault policy write qytang-policy - << EOF

path "qytang/*" {
  capabilities = ["read"]
}
EOF
```

### 创建令牌
```shell script
vault token create -policy=qytang-policy

---------下面是输出---------------

Key                  Value
---                  -----
token                s.lztzELhSgISb23b9IYksJrLS
token_accessor       6E48lFXVeInaKRuGQyJLl2vn
token_duration       768h
token_renewable      true
token_policies       ["default" "qytang-policy"]
identity_policies    []
policies             ["default" "qytang-policy"]
```

### 调整令牌[受控]
```shell script
export VAULT_TOKEN="s.lztzELhSgISb23b9IYksJrLS"
```

### 测试读取
```shell script
# get时允许的
[root@localhost ~]# vault kv get qytang/cisco_ios/cred
====== Metadata ======
Key              Value
---              -----
created_time     2021-05-15T01:54:43.891942667Z
deletion_time    n/a
destroyed        false
version          1

====== Data ======
Key         Value
---         -----
password    Cisc0123
username    admin

[root@localhost ~]# vault kv get qytang/cisco_asa/cred
====== Metadata ======
Key              Value
---              -----
created_time     2021-05-15T01:51:39.122476462Z
deletion_time    n/a
destroyed        false
version          1

====== Data ======
Key         Value
---         -----
password    Cisc0123
secret      Cisc0123
username    admin
```

# 拒绝写入
```shell script
[root@localhost ~]# vault kv put qytang/asa-cred username=admin password=Cisc0123
Error writing data to qytang/data/asa-cred: Error making API request.

URL: PUT https://127.0.0.1:8200/v1/qytang/data/asa-cred
Code: 403. Errors:

* 1 error occurred:
        * permission denied

```

### 调整令牌[root] (确保后续操作)
```shell script
export VAULT_TOKEN="s.LvOvI2DEhkzsxnK87mcQ0zS7"
```