# import csv
#
hex_string = "0xe91a94a500000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000001400000000000000000000000004d2d32d8652058bf98c772953e1df5c5c85d9f45000000000000000000000000000000000000000000000003cb71f51fc5580000000000000000000000000000000000000000000000000000000000006458f250000000000000000000000000000000000000000000000ed2b525841adfc000000000000000000000000000000000000000000000000000000000000000000041ca551907efba49cc8178f2554bb036837a387e7da003acf82839ffc0a6321cba6211ab67855bf0e68f221b251da2b75ea66e51a6ad4fa686aa2a6dd531c1a8641b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a4f394c4b3353706a4d4800000000000000000000000000000000000000000000"

#
# print(len(hex_string))
#
# print(hex(int(hex_string[137:202],16)))
"""
00000000000000000000000000000000000000000000000000000000000000c0
0000000000000000000000000000000000000000000000000000000000000140
000000000000000000000000e9e7cea3dedca5984780bafc599bd69add087d56
00000000000000000000000000000000000000000000001b1ae4d6e2ef500000
00000000000000000000000000000000000000000000000000000000645ce6d0
0000000000000000000000000000000000000000000034f086f3b33b68400000
0000000000000000000000000000000000000000000000000000000000000041
5acd8c0ca093a184f1e39884c96d22012207299cf2a9bc8141f5f0e5f7662161
1e2030f047da7c72dd28c1e370d9c99f246601441dbb41d5ae7247af3ac079f2
1c00000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000a
4d4c4e54394332666a6200000000000000000000000000000000000000000000
"""


def decoder(hex_string):
    decoded_data = []
    try:
        # decode signature
        start_sign = 394+64
        end_sign = (start_sign+(64*3))
        updated_signature_number = hex(int(hex_string[start_sign:end_sign], 16))
        signature = updated_signature_number[:(len(updated_signature_number)-62)]
        decoded_data.append({"Name": "signature", "Type": "bytes", "Data": signature})
        # decode shoId
        sho_id_start = len(hex_string)-64
        sho_id = bytes.fromhex(hex_string[sho_id_start:len(hex_string)])
        sho_id_decode = sho_id[0:10].decode('ascii')
        decoded_data.append({"Name": "shoID", "Type": "string", "Data": sho_id_decode})
        # decode deposite token
        deposite_token = hex(int(hex_string[137:202],16))
        decoded_data.append({"Name": "depositToken", "Type": "address", "Data": deposite_token})
        # decode amount
        amount = int(hex_string[202:266],16)
        decoded_data.append({"Name": "amount", "Type": "uint256", "Data": amount})
        # decode deadline
        deadline = int(hex_string[266:330],16)
        decoded_data.append({"Name": "deadline", "Type": "uint256", "Data": deadline})
        # decode option
        option = int(hex_string[330:394],16)
        decoded_data.append({"Name": "option", "Type": "uint256", "Data": option})

    except Exception as e:
        return e
    return decoded_data


data = decoder(hex_string)
print(data)

#
# filename = 'data.tsv'
#
# with open(filename, 'w', newline='') as tsvfile:
#     fieldnames = data[0].keys()
#     writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter='\t')
#     writer.writeheader()
#     writer.writerows(data)
#
# print('Data written to', filename)














"""
address_from_token = hex_string[34:74]

address_from_token_hex = hex(int((address_from_token),16))
print(f"address fromToken:{Web3.to_checksum_address(address_from_token_hex)}")

address_to_token = hex_string[98:138]
address_to_token_hex = hex(int((address_to_token),16))
print(f"address toToken:{(address_to_token_hex)}")


amount_int = hex_string[138:202]
amount_int256 = int((amount_int),16)
print(f"uint256 fromAmount:{amount_int256}")

recipient_address  = hex_string[226:266]
recipient_address_hex = hex(int((recipient_address),16))
print(f"address recipient:{Web3.to_checksum_address(recipient_address_hex)}")

return_int = hex_string[266:330]
return_int256 = int((return_int),16)
print(f"uint256 minReturn:{return_int256}")



permission_bytes = hex_string[522:652]
permission_hex = hex(int((permission_bytes),16))
print(f"bytes permission:{permission_hex}")




"""

