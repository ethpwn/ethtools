# coding: utf-8
from ethpwn.prelude import *
import time
from web3.datastructures import AttributeDict

context.connect_http('https://eth-sepolia.g.alchemy.com/v2/CIlvNRJd1iqhTV5d_KIBxWX_qCq0j71v')

CONTRACT_METADATA.add_solidity_files(['../ethernaut/gatekeeper_three/exploit.sol'])
CONTRACT_METADATA.add_solidity_files(['../ethernaut/puzzle_wallet/exploit.sol'])
CONTRACT_METADATA.add_solidity_files(['../ethernaut/good_samaritan/exploit.sol'])

# trace = simulate_execution([{'from': '0xE64E0e04D2279876984764D36d7e8588e2eD167d', 'to': '0x7ac5b6aac6eEB251eB33b885302feB54b6aF2F96', 'value': '0x0', 'data': '0x63d9b770'}])

trace = AttributeDict({'calls': [AttributeDict({'type': 'CALL',
   'from': '0xe64e0e04d2279876984764d36d7e8588e2ed167d',
   'to': '0x7ac5b6aac6eeb251eb33b885302feb54b6af2f96',
   'value': '0x0',
   'gas': '0x7fffffffffffaad0',
   'gasUsed': '0x426b8',
   'input': '0x63d9b770',
   'output': '0x08c379a0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000216578706c6f6974206661696c65642c20636f756c64206e6f7420656e7465723f3f00000000000000000000000000000000000000000000000000000000000000',
   'error': 'execution reverted'}),
  AttributeDict({'type': 'CALL',
   'from': '0x7ac5b6aac6eeb251eb33b885302feb54b6af2f96',
   'to': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'value': '0x0',
   'gas': '0x7dffffffffff9ab0',
   'gasUsed': '0x1423',
   'input': '0xb9966e56',
   'output': '0x'}),
  AttributeDict({'type': 'CALL',
   'from': '0x7ac5b6aac6eeb251eb33b885302feb54b6af2f96',
   'to': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'value': '0x0',
   'gas': '0x7dffffffffff8728',
   'gasUsed': '0x33e70',
   'input': '0xf7edf099',
   'output': '0x'}),
  AttributeDict({'type': 'CREATE',
   'from': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'to': '0xdc863249d432e9f594a735e10bd07860531018c7',
   'value': '0x0',
   'gas': '0x7c07ffffffff0c98',
   'gasUsed': '0x25357',
   'input': '0x60806040524260025534801561001457600080fd5b506040516102b23803806102b283398101604081905261003391610058565b600080546001600160a01b0319166001600160a01b0392909216919091179055610088565b60006020828403121561006a57600080fd5b81516001600160a01b038116811461008157600080fd5b9392505050565b61021b806100976000396000f3fe608060405234801561001057600080fd5b50600436106100675760003560e01c80639e4b2e47116100505780639e4b2e47146100cd578063b7e00291146100f0578063d4b83992146100f857600080fd5b80634cbb817f1461006c578063690da2b21461009d575b600080fd5b61009b600180547fffffffffffffffffffffffff00000000000000000000000000000000000000001630179055565b005b6001546100b0906001600160a01b031681565b6040516001600160a01b0390911681526020015b60405180910390f35b6100e06100db3660046101cc565b61010b565b60405190151581526020016100c4565b61009b61012a565b6000546100b0906001600160a01b031681565b600060025482141561011f57506001919050565b505042600255600090565b303314801561014457506001546001600160a01b03163014155b156101ca576000546002546040517fc960174e0000000000000000000000000000000000000000000000000000000081526001600160a01b039092169163c960174e916101979160040190815260200190565b600060405180830381600087803b1580156101b157600080fd5b505af11580156101c5573d6000803e3d6000fd5b505050505b565b6000602082840312156101de57600080fd5b503591905056fea2646970667358221220a0b5ed03673a8ac425b105d24ceb05cfa4837973203cae4053eb62d95dc4f37464736f6c634300080c00330000000000000000000000000c5f7599b877f036a7399fa127f92d478995b236',
   'output': '0x608060405234801561001057600080fd5b50600436106100675760003560e01c80639e4b2e47116100505780639e4b2e47146100cd578063b7e00291146100f0578063d4b83992146100f857600080fd5b80634cbb817f1461006c578063690da2b21461009d575b600080fd5b61009b600180547fffffffffffffffffffffffff00000000000000000000000000000000000000001630179055565b005b6001546100b0906001600160a01b031681565b6040516001600160a01b0390911681526020015b60405180910390f35b6100e06100db3660046101cc565b61010b565b60405190151581526020016100c4565b61009b61012a565b6000546100b0906001600160a01b031681565b600060025482141561011f57506001919050565b505042600255600090565b303314801561014457506001546001600160a01b03163014155b156101ca576000546002546040517fc960174e0000000000000000000000000000000000000000000000000000000081526001600160a01b039092169163c960174e916101979160040190815260200190565b600060405180830381600087803b1580156101b157600080fd5b505af11580156101c5573d6000803e3d6000fd5b505050505b565b6000602082840312156101de57600080fd5b503591905056fea2646970667358221220a0b5ed03673a8ac425b105d24ceb05cfa4837973203cae4053eb62d95dc4f37464736f6c634300080c0033'}),
  AttributeDict({'type': 'CALL',
   'from': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'to': '0xdc863249d432e9f594a735e10bd07860531018c7',
   'value': '0x0',
   'gas': '0x7c07fffffffcab38',
   'gasUsed': '0x56ed',
   'input': '0x4cbb817f',
   'output': '0x'}),
  AttributeDict({'type': 'CALL',
   'from': '0x7ac5b6aac6eeb251eb33b885302feb54b6af2f96',
   'to': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'value': '0x0',
   'gas': '0x7dfffffffffc52d8',
   'gasUsed': '0x5b1a',
   'input': '0xc960174e0000000000000000000000000000000000000000000000000000000064209258',
   'output': '0x'}),
  AttributeDict({'type': 'CALL',
   'from': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'to': '0xdc863249d432e9f594a735e10bd07860531018c7',
   'value': '0x0',
   'gas': '0x7c07fffffffc6100',
   'gasUsed': '0x1a9',
   'input': '0x9e4b2e470000000000000000000000000000000000000000000000000000000064209258',
   'output': '0x0000000000000000000000000000000000000000000000000000000000000001'}),
  AttributeDict({'type': 'STATICCALL',
   'from': '0x7ac5b6aac6eeb251eb33b885302feb54b6af2f96',
   'to': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'gas': '0x7dfffffffffbf900',
   'gasUsed': '0x13d',
   'input': '0x0e6e4b14',
   'output': '0x0000000000000000000000000000000000000000000000000000000000000001'}),
  AttributeDict({'type': 'CALL',
   'from': '0x7ac5b6aac6eeb251eb33b885302feb54b6af2f96',
   'to': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'value': '0x0',
   'gas': '0x7dfffffffffbf518',
   'gasUsed': '0x2d9',
   'input': '0xe97dcb62',
   'output': '0x0000000000000000000000000000000000000000000000000000000000000000'}),
  AttributeDict({'type': 'STATICCALL',
   'from': '0x7ac5b6aac6eeb251eb33b885302feb54b6af2f96',
   'to': '0x0c5f7599b877f036a7399fa127f92d478995b236',
   'gas': '0x7dfffffffffbf130',
   'gasUsed': '0x194',
   'input': '0x9db31d77',
   'output': '0x0000000000000000000000000000000000000000000000000000000000000000'})],
 'logs': []})
time.sleep(1)
pretty_print_simulation_trace(trace)
