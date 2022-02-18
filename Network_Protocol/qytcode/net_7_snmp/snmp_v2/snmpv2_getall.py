from snmpv2_getbulk import snmpv2_getbulk
from snmpv2_get import snmpv2_get


def snmpv2_getall(ip, community, count=25, port=161):
    # cpmCPUTotal5sec
    cpu_usage = snmpv2_get(ip, community, "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)

    # cpmCPUMemoryUsed
    mem_usage = snmpv2_get(ip, community, "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)

    # cpmCPUMemoryFree
    mem_free = snmpv2_get(ip, community, "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)

    name_list = [x[1] for x in snmpv2_getbulk(ip, community, "1.3.6.1.2.1.2.2.1.2", count=count, port=port)]
    # print(name_list)

    speed_list = [int(x[1]) for x in snmpv2_getbulk(ip, community, "1.3.6.1.2.1.2.2.1.5", count=count, port=port)]
    # print(speed_list)

    in_bytes_list = [int(x[1]) for x in snmpv2_getbulk(ip, community, "1.3.6.1.2.1.2.2.1.10", count=count, port=port)]
    # print(in_bytes_list)

    out_bytes_list = [int(x[1]) for x in snmpv2_getbulk(ip, community, "1.3.6.1.2.1.2.2.1.16", count=count, port=port)]
    # print(out_bytes_list)

    if_list = []
    for x in zip(name_list, speed_list, in_bytes_list, out_bytes_list):
        if_list.append({'name': x[0], 'speed': x[1], 'in_bytes': x[2], 'out_bytes': x[3]})

    final_dict = {'ip': ip,
                  'cpu_usage': int(cpu_usage[1]),
                  'mem_usage': int(mem_usage[1]),
                  'mem_free': int(mem_free[1]),
                  'if_list': if_list}

    return  final_dict


if __name__ == '__main__':
    from pprint import pprint

    final_result = snmpv2_getall("10.1.1.253", "tcpipro", count=25, port=161)

    pprint(final_result, indent=4)
