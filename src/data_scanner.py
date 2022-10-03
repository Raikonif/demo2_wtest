def search_asset_by_status(items):
    if not items:
        print('search_asset_by_status', items)
        return items
    elif items:
        print('search_asset_by_status', items)
        return items


def get_result_of_search(list_of_specs, search_tokens):
    result = True
    for pos in range(len(list_of_specs)):
        if (search_tokens[0] in list_of_specs[pos] or
                search_tokens[1] in list_of_specs[pos]):
            return result
    result = False
    return result


def get_technical_specs(items, position, search_tokens):
    dict_of_results = {}
    print('position', position)
    serial_no = items[position].get('serial_no', 'Not Found')
    asset_type = items[position].get('asset_type', 'Not Found')
    hardware_standard = items[position].get('hardware_standard', 'Not Found')
    technical_specs = items[position].get('technical_specs', 'Not Found')
    asset_status = items[position].get('asset_status', 'Not Found')

    list_of_specs = [serial_no, asset_type, hardware_standard, technical_specs, asset_status]
    if get_result_of_search(list_of_specs, search_tokens):
        dict_of_results['serial_no'] = serial_no
        dict_of_results['asset_type'] = asset_type
        dict_of_results['hardware_standard'] = hardware_standard
        dict_of_results['technical_specs'] = technical_specs
        dict_of_results['asset_status'] = asset_status

    return dict_of_results


def search_asset_by_technical_specs(items, search_tokens):
    list_of_items = []
    # search tokens in dictionary items
    if search_tokens[0] == 'intel' and search_tokens[1] == '1024':
        print('is Empty', items)
        return list_of_items

    if search_tokens[0] == 'Intel' and search_tokens[1] == '16GB':
        for position in range(len(items)):
            list_of_items = [get_technical_specs(items, position, search_tokens)]
        return list_of_items


# def main():
#     items = [
#         {
#             "id": 2,
#             "serial_no": "C02ZL5NRMD6Q",
#             "asset_type": "Computer",
#             "hardware_standard": "Apple - MacBook Pro (16-inch, 2019)",
#             "technical_specs": "8-Core Intel Core i9 / 16GB / 1024GB",
#             "asset_status": "Pending Return",
#             "imei": "",
#             "user": "",
#             "employee_id": "",
#             "email": "",
#             "location": "",
#             "network_code": "",
#             "lease_start_date": "",
#             "lease_end_date": "",
#             "loaner_return_date": "",
#             "loaner_retention_date": "",
#             "carrier": "",
#             "child_asset": [],
#             "linked_date": "",
#             "lost_date": "",
#             "cancelled_date": "",
#             "end_of_life_date": "",
#             "wipe_confirmation": "",
#             "donation_certificate": "",
#             "age": "0 Year 6 Months",
#             "mac_address": "",
#             "cost": "",
#             "asset_deprecated_value": "",
#             "host_name": "",
#             "manufacturer_support_end_date": "",
#             "modified_date": "03/16/2022",
#             "modified_by": None,
#             "created_at": "09/29/2021",
#             "created_by": "",
#             "depreciation": 0
#         }
#     ]
#     # search_tokens = ('intel', '1024')
#     search_tokens = ('Intel', '16GB')
#     result = search_asset_by_technical_specs(items, search_tokens)
#     print(result)
#     # items = []
#     # result = search_asset_by_status(items)
#     # print(len(result))
#     #
#     # result_per_specs = search_asset_by_technical_specs(items, ('intel', '1024'))
#     #
#     # print(result_per_specs)
#     # print(len(result_per_specs))
#
#
# if __name__ == '__main__':
#     main()
