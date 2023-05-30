
#deposited decode
from web3 import Web3
def convert_deposited_input_to_desired_ouput(input_str):
        output_json = {}
        req_input_str = input_str[138:]
        deposited_token_str = req_input_str[:64]
        unint256_deadline_str = req_input_str[128:192]
        unint256_option_str = req_input_str[192:256]
        unint256_amount_str = req_input_str[64:128]
        signature_bytes = req_input_str[320:450]
        shoId_string = req_input_str[576:596]
        # print("deposited unint256",deposted_token_str)
        # print("option unint256",unint256_option_str)
        # print("deadline unint256",unint256_deadline_str)
        # print("amount unint256",unint256_amount_str)
        # print("signature bytes",signature_bytes)
        # print("shoId address",shoId_string)
        unint256_deadline = int(unint256_deadline_str, 16)
        unint256_option = int(unint256_option_str,16)
        unint256_amount = int(unint256_amount_str,16)
        string_shoId = bytes.fromhex(shoId_string)
        signature_ = hex(int(signature_bytes, 16))
        deposited_token_address = Web3.to_checksum_address("0x" + deposited_token_str[-40:])
        output_json['signature : bytes'] = signature_
        output_json['shoId : string'] = string_shoId.decode('utf-8')
        output_json['depositedToken : address'] = deposited_token_address
        output_json['amount : unint256'] = unint256_amount
        output_json['deadline : unint256'] = unint256_deadline
        output_json['option : unint256'] = unint256_option
        return output_json



transaction_1 = ("0xe91a94a500000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000140000000000000000000000000e9e7cea3dedca5984780bafc599bd69add087d560000000000000000000000000000000000000000000000056bc75e2d63100000000000000000000000000000000000000000000000000000000000006460db500000000000000000000000000000000000000000000034f086f3b33b684000000000000000000000000000000000000000000000000000000000000000000041abfc307f6c818da5ddd4f8cba8d1119c679ac5e03a42fc3026e80bce95817e3b4a82e3f118a6be8674a18e42c94874a6117ae612ada106194919ce4bd532c8251b00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a506d45476d43756f4c3500000000000000000000000000000000000000000000")


decoded_1 = convert_deposited_input_to_desired_ouput(transaction_1)
print(decoded_1)

'''
#
# #
# #
# #
# # shoId_data = "506d45476d43756f4c3500000000000000000000000000000000000000000000"
# #
# # byte_data = bytes.fromhex(shoId_data)
# # decoded_data = byte_data[0:10].decode('ascii')
# # print(f"shoId {decoded_data}")
# #
# #
# # hex_string = "0000000000000000000000000000000000000000000000056bc75e2d63100000"
# #
# # uint256_value = int(hex_string, 16)
# #
# # print(f"amount {uint256_value}")
# #
# #
# # deadline_hex = "000000000000000000000000000000000000000000000000000000006460db50"
# #
# # uint256_value = int(deadline_hex, 16)
# #
# # print(f"dealine {uint256_value}")
# #
# #
# # option_hex =  "0000000000000000000000000000000000000000000034f086f3b33b68400000"
# #
# # uint256_value = int(option_hex, 16)
# #
# # print(f"option {uint256_value}")
# #
# #
# # hex_string = "000000000000000000000000e9e7cea3dedca5984780bafc599bd69add087d56"
# #
# # # Remove leading zeros from the hex string
# # hex_string = hex_string.lstrip('0')
# #
# # # Add '0x' prefix to the hex string
# # address = '0x' + hex_string
# #
# # print("address",address)
# #
# # signature_hex = int("abfc307f6c818da5ddd4f8cba8d1119c679ac5e03a42fc3026e80bce95817e3b""4a82e3f118a6be8674a18e42c94874a6117ae612ada106194919ce4bd532c825" "1b00000000000000000000000000000000000000000000000000000000000000",16)
# #
# # print(f"signature {hex(signature_hex)}")
#
# '''# shoID
# start = len(hex_string)-65
# shoID = bytes.fromhex(hex_string[start:len(hex_string)])
# shoID_decode = shoID[0:10].decode('ascii')
# print(shoID_decode)
#
# '''
# '''
#
# start = 395+64
# end = (start+(64*3))
#
# signature = hex(int(hex_string[start:end],16))
# print(signature)
# print("0x5acd8c0ca093a184f1e39884c96d22012207299cf2a9bc8141f5f0e5f76621611e2030f047da7c72dd28c1e370d9c99f246601441dbb41d5ae7247af3ac079f21c")
# '''
#
#
#
# '''
# option = int(hex_string[331:395],16)
# print(option)
# #250000000000000000000000
# '''
#
#
# '''
# # deadline
# deadline = int(hex_string[267:331],16)
# print(deadline)
# '''
#
#
# '''
# # amount
# amount = int(hex_string[203:267],16)
# print(amount)
#
# '''
#
# '''
# # deposite_token
# deposite_token =  hex(int(hex_string[138:203],16))
# print(deposite_token)
#
# '''
#
