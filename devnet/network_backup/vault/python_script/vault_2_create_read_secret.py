from vault_1_init import client

# 需要管理员令牌
# 创建secret
create_response = client.secrets.kv.v2.create_or_update_secret(
    mount_point='qytang',
    path='foo',
    secret=dict(baz='bar'),
)


# 查看版本
list_response = client.secrets.kv.v2.read_secret_metadata(
    mount_point='qytang',
    path='cisco_ios/cred',
)
#
print(list_response['data'])
print(list_response['data']['current_version'])


# 获取特定secret的值
read_response = client.secrets.kv.v2.read_secret_version(
    mount_point='qytang',
    path='cisco_asa/cred')

print(read_response['data']['data'])


# 需要管理员令牌
# 罗列特定engine的keys
list_response = client.secrets.kv.v2.list_secrets(
    mount_point='qytang',
    path='',
)

print(list_response['data']['keys'])
