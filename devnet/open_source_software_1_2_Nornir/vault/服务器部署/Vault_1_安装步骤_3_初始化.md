### 设置环境变量
```shell script
export VAULT_ADDR="https://127.0.0.1:8200"
export VAULT_CACERT="/opt/certs/ca.pem"
```

### 初始化数据库
```shell script
vault operator init

------------下面是输--------------
Unseal Key 1: D3ss7u2uSeJcW60QDfvZ1UILmzG868uUHvkfoABE+XYb
Unseal Key 2: Jx8yIxHF67/xYXLC95/+ur6nK+/sQWT80EBFIqJuxZVv
Unseal Key 3: r+TPyEKEW4ch9OB03vK4wFYPkIjqrh89SFVvuQxRcfrU
Unseal Key 4: 7DC1XZmjz535FAMG4lQk3uQCXMWepraPGV6+ppKethCA
Unseal Key 5: 1SiZl/eJhOdT+8vTG87+6vgta1oW60m+IfLTpPyyisCH

Initial Root Token: s.LvOvI2DEhkzsxnK87mcQ0zS7

Vault initialized with 5 key shares and a key threshold of 3. Please securely
distribute the key shares printed above. When the Vault is re-sealed,
restarted, or stopped, you must supply at least 3 of these keys to unseal it
before it can start servicing requests.

Vault does not store the generated master key. Without at least 3 key to
reconstruct the master key, Vault will remain permanently sealed!

It is possible to generate new unseal keys, provided you have a quorum of
existing unseal keys shares. See "vault operator rekey" for more information.
```

### unseal数据库
```shell script
# 连续操作三次， 输入5个unseal秘钥中的3个
[root@localhost certs]# vault operator unseal
Unseal Key (will be hidden): 输入其中一个
Key                Value
---                -----
Seal Type          shamir
Initialized        true
Sealed             true
Total Shares       5
Threshold          3
Unseal Progress    1/3
Unseal Nonce       1ff4d346-d005-2ad3-5122-8c45aa5ad170
Version            1.6.2
Storage Type       raft
HA Enabled         true

[root@localhost certs]# vault operator unseal
Unseal Key (will be hidden): 输入其中另外一个
Key                Value
---                -----
Seal Type          shamir
Initialized        true
Sealed             true
Total Shares       5
Threshold          3
Unseal Progress    2/3
Unseal Nonce       1ff4d346-d005-2ad3-5122-8c45aa5ad170
Version            1.6.2
Storage Type       raft
HA Enabled         true

[root@localhost certs]# vault operator unseal
Unseal Key (will be hidden): 输入其中再另外一个
Key                     Value
---                     -----
Seal Type               shamir
Initialized             true
Sealed                  false
Total Shares            5
Threshold               3
Version                 1.6.2
Storage Type            raft
Cluster Name            vault-cluster-c18407fc
Cluster ID              ad09c853-d15a-5abc-d227-c969acf6fd94
HA Enabled              true
HA Cluster              n/a
HA Mode                 standby
Active Node Address     <none>
Raft Committed Index    24
Raft Applied Index      24
```