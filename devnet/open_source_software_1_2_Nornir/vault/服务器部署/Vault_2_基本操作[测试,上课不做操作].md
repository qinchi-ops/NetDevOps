### 设置环境变量
```shell script
export VAULT_TOKEN="s.LvOvI2DEhkzsxnK87mcQ0zS7"
```

### 激活secret engine
```shell script
# 关于secret engine介绍
# https://www.vaultproject.io/docs/secrets/kv/kv-v2

vault secrets enable -path=qytang/ kv-v2
```

### 添加secret
```shell script
vault kv put qytang/router-cred username=admin password=Cisc0123

---------下面是输出---------------

Key              Value
---              -----
created_time     2021-01-31T02:12:09.361051526Z
deletion_time    n/a
destroyed        false
version          1
```

### 获取secret
```shell script
vault kv get qytang/router-cred

---------下面是输出---------------

====== Metadata ======
Key              Value
---              -----
created_time     2021-01-31T02:12:09.361051526Z
deletion_time    n/a
destroyed        false
version          1

====== Data ======
Key         Value
---         -----
password    Cisc0123
username    admin
```

### 获取secret的特定键
```shell script
vault kv get -field=username qytang/router-cred 

---------下面是输出---------------

admin
```

### 列出secret
```script script

---------下面是输出---------------

vault kv list qytang/
Keys
----
router-cred
```

### 删除secret
```shell script
vault kv delete qytang/router-cred

---------下面是输出---------------

Success! Data deleted (if it existed) at: qytang/router-cred

```

### 禁用secret engine
```shell script
vault secrets disable qytang/

---------下面是输出---------------

Success! Disabled the secrets engine (if it existed) at: qytang/
```