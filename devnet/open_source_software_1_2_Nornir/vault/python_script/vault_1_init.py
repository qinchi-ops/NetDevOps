import hvac

client = hvac.Client(
    url='https://192.168.19.7:8200',
    # token="s.fXX4OZfgckYeAeuHnL3oI89C",  # 使用权限被控制的令牌
    token="s.lwljG7ZeVCoW0YRNi7FILZ3R",  # read权限
    verify="/devnet/open_source_software_1_2_Nornir/vault/python_script/ca.pem"
    # verify="/opt/certs/ca.pem"
)

# 是否认证
print(client.is_authenticated())

# 是否解锁
print(client.sys.is_sealed())

