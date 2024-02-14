import pytest
from input_action import InputAction
from input_action.payloads import EmptyPayload
from input_action.types import InputActionType
from network_message import NetworkMessage

from bitstring import BitStream


def test_transfer_block_message_transparancy():
    example_input = BitStream(bytes.fromhex("0d060000009c91b72f53d3782e3b33abdebe42e9c9c24805fda5debf4a4dd30a0197fc1ab506de3293fbfbbe4e0d76907a81e713a8c5a6cb58c5900e279c4c0b87b3d3a5ca44ae891689b8cfd826958ea5fa62f64066345f1a2fd2c2b1626e0a23f873d43a3c810984e6e894cf53cb74218f210a7e0baa2fd0a2d244e1c048e1804dfa222d1ac98de6a630780cd4b3d43e82e15ccc0e970b36f1396a1bc1c82e16667dc02fd152000e8fcbe8152ca51ca6c064a19cfb212df33ba7cc0065196592f90b505a989ecd4c67416da65c284ca46229a7500ba67b00e4545a1c99c8900b931e754552f53c3e91166088b652dd349a5298782bb5942a4393d9e1718cfb0c72de468bcad9a9fd18f036e9edb47826379e1fc6dc0fa43e416d02181c2fefa0857aa8bf1364623c65cb188132299ea45635e03213d9cad4f078aef8143507cbbe8bba7cce1cc88e49eff034790fad084ce208924cef7bab66f7bdaf6a76fffbab660f7c809aa4916a027e906a98b78f52f38142612487b1328eaef7a851d41f79495113fa2e37a1b2165033985ccc4288319a1a6ac1e8992ab1b8cb0ce526cab5b478147d9d09a7d6894428e64aa548c6425a0461942b8e89e8110cf5d42918a2e90db414d3427044b31aa9be343d912f634234515a4a9bf766910f52ca24a5a96ea28059546ca12681556fadd462f0ab8445d43a542962fdc02a"))
    example_network_message = NetworkMessage.from_bitstream(example_input)
    example_output = example_network_message.to_bitstream()
    assert example_input == example_output


def test_empty_server_to_client_heartbeat_transparancy():
    example_input = BitStream(bytes.fromhex("070044730100"))
    example_network_message = NetworkMessage.from_bitstream(example_input)
    example_output = example_network_message.to_bitstream()
    assert example_input == example_output


def test_single_tick_closure_server_to_client_heartbeat_transparancy() -> None:
    example_input = BitStream(bytes.fromhex(
        "07064e7301009f140000024a000abeaa7c9e140000"))
    example_network_message = NetworkMessage.from_bitstream(example_input)
    example_output = example_network_message.to_bitstream()
    assert example_input == example_output


def test_input_action_segment_throws_error() -> None:
    with pytest.raises(NotImplementedError):
        example_input = BitStream(bytes.fromhex(
            "270610520000f0120000034a00f62431c2ef12000001860000000000010010000000000000001065b3650000000000"))
        example_network_message = NetworkMessage.from_bitstream(example_input)
        example_output = example_network_message.to_bitstream()
        assert example_input == example_output


def test_stop_walking_injection():
    example_input = BitStream(bytes.fromhex(
        "26061372502da0370000023d010289370000"))
    example_network_message = NetworkMessage.from_bitstream(example_input)

    example_input_action = InputAction(
        InputActionType.StopWalking, 0, EmptyPayload())
    example_network_message.inject_input_action(example_input_action)
    example_output = example_network_message.to_bitstream()
    assert example_input != example_output

def test_single_synchronizer_action_s_to_c():
    example_input = BitStream(bytes.fromhex("27100b2208000109c11800"))
    example_network_message = NetworkMessage.from_bitstream(example_input)
    example_output = example_network_message.to_bitstream()
    assert example_input == example_output

def test_single_synchronizer_action_c_to_s():
    example_input = BitStream(bytes.fromhex("2610d4c8a915947500000109a3"))
    example_network_message = NetworkMessage.from_bitstream(example_input)
    example_output = example_network_message.to_bitstream()
    assert example_input == example_output