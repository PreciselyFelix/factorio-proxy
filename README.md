# Factorio MITM-Proxy
Local MITM-Proxy to intercept and modify Factorio network traffic written in Python.

<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#description">Description</a>
        </li>
        <li>
            <a href="#getting-started">Getting Started</a>
            <ul>
                <li><a href="#installation">Installation</a></li>
                <li>
                    <a href="#usage--examples">Usage / Examples</a>
                    <ul>
                        <li><a href="#quick-start">Quick Start</a></li>
                        <li><a href="#show-help">Show help</a></li>
                        <li><a href="#pass-through">Pass-through</a></li>
                        <li><a href="#decode">Decode</a></li>
                        <li><a href="#inject">Inject</a></li>
                        <li><a href="#filter">Filter</a></li>
                    </ul>
                </li>
            </ul>
        </li>
        <li>
            <a href="#logging">Logging</a>
        </li>
        <li>
            <a href="#contibuting">Contributing</a>
            <ul>
                <li><a href="#adding-network-message-type">Adding Network Message Type</a></li>
                <li><a href="#adding-input-action-type">Adding Input Action Type</a></li>
                <li><a href="#adding-message-handler">Adding Message Handler</a></li>
                <li><a href="#code-smells">Code Smells</a></li>
            </ul>
        </li>
        <li>
            <a href="#references">References</a>
        </li>
    </ol>
</details>

# Description
This project was created as part of a research paper about reverse engineering written for my university. 

This repository contains the Python (Version 3.12) code necessary to run a man-in-the-middle proxy that can decode and manipulate Factorio network traffic between one client and a server. The proxy currently only supports decoding and re-encoding some of the most common aspects of the Factorio protocol. It supports decoding and logging all messages that pass through it, injecting additional input actions into messages and filtering out existing input actions. The project was built by dissecting the raw network packets using [wireshark](https://github.com/wireshark/wireshark) and the [factorio dissector plugin written by Hornwitser](https://github.com/Hornwitser/factorio_dissector) and then writing partial decoders using the [bitstring](https://github.com/scott-griffiths/bitstring) Python module. A text dump of the factorio.pdb using [cvdump.exe](https://github.com/Microsoft/microsoft-pdb/blob/master/cvdump/cvdump.exe) was performed to get the up to date names and ids of fields such as message types. [Ghidra](https://github.com/NationalSecurityAgency/ghidra) was used to decompile factorio.exe to get an understanding of how inner payloads of input actions are parsed.

# Getting Started
## Installation
1. Clone Repository
    ```
    git clone https://github.com/PreciselyFelix/factorio-proxy.git
    ```
2. Install Requirements
    ```
    pip install -r requirements.txt
    ```
## Usage / Examples


### Quick Start
```
python main.py pass-through --factorio_ip=<server-ip> --factorio_port=<server-port>
```
You can now open Factorio and connect to the server through the proxy by directly connecting to `localhost:1234`.


### Show help
```
python main.py --help
```



### Pass-through
```
python main.py pass-through --listen_ip=localhost --listen_port=1234 --factorio_ip=127.0.0.1 --factorio_port=34197
```
Start the proxy to listen on `localhost:1234` and forward messages to `127.0.0.1:34197` without decoding or modifying. All of the arguments shown here are optional and default to the values in this example.



### Decode
```
python main.py decode
```
Start the proxy with default values and try to decode, log and re-encode before forwarding the message.



### Inject
```
python main.py inject --input_action_type=StopWalking --message_type=ClientToServerHeartbeat
```
Start the proxy with default values and try to inject all `ClientToServerHeartbeat` messages with a blank `StopWalking` input action. This example causes the player position to be reset back to the start whenever he tries to walk.

In the current implementation the proxy can only inject input actions that have an empty payload (the expected payload length is 0).



### Filter
```
python main.py filter --input_action_type=RotateEntity --message_type=ClientToServerHeartbeat
```
Start the proxy with default values and try to remove all `RotateEntity` input actions from all `ClientToServerHeartbeat` messages.



# Logging
By default all logs are written to `./logs/factorio-proxy.log` and everything above loglevel debug is also written to stdout.

This behaviour can be changed by editing `./logger_config.json`.




# Contibuting

This Proxy is still incomplete and test coverage is very low. It was written for `Factorio 1.1.101` and currently supports:
* __4/19__ Factorio network message types
* __1/20__ Factorio synchronizer actions
* __9/250__ Factorio input actions

__Any and all contributions like adding unit tests, expanding message decoding, improving documentation, opening issues and questions or discussion are welcome.__

## Adding Network Message Type
1. Chose a `MessageType` from `./network_message/types.py`
2. Add a new payload class to `./network_message/payloads.py` that inherits from `MessagePayload` and implements the `from_bitstream` and `to_bitstream` methods. Example:
    ```python
    class MyMessagePayload(MessagePayload):
        my_data: int

        def __init__(self, my_data: int):
            this.my_data = my_data

        @classmethod
        def from_bitstream(cls, bit_stream: BitStream):
            my_data = bit_stream.read("uintle8")
            return cls(my_data)

        def to_bitstream(self) -> BitStream:
            return BitStream(f"uintle8={self.my_data}")
    ```
3. Add the new payload class to the match statement in `NetworkMessage.decode_message_payload()`. Example:
    ```python
    ...
    case MessageType.TransferBlock:
        return TransferBlockPayload.from_bitstream(bit_stream)
    case MessageType.MyMessageType:
        return MyMessagePayload.from_bitstream(bit_stream)
    case _:
        raise NotImplementedError(f"Unsupported MessageType: {message_type}")
    ...
    ```


## Adding Input Action Type
1. Chose an `InputActionType` from `./input_action/types.py`
2. Add a new payload class to `./input_action/payloads.py` that inherits from `InputActionPayload` and implements the `from_bitstream` and `to_bitstream` methods. Example:
    ```python
    class MyInputActionPayload(InputActionPayload):
        my_data: int

        def __init__(self, my_data: int) -> None:
            self.my_data = my_data

        @classmethod
        def from_bitstream(cls, bit_stream: BitStream):
            my_data = bit_stream.read("uintle8")
            return cls(my_datadata)
        
        def to_bitstream(self) -> BitStream:
            return BitStream(f"uintle8={self.my_data}")
    ```
3. Add the new payload class to the match statement in `InputAction.decode_input_action()`. Example:
    ```python
    ...
    case InputActionType.RotateEntity:
        return RotateEntityPayload.from_bitstream(bit_stream)
    case InputActionType.MyInputAction:
        return MyInputActionPayload.from_bitstream(bit_stream)
    case _:
        raise NotImplementedError(f"Unsupported input action type: {input_action_type}")
    ...
    ```


## Adding Message Handler
1. Write a new class that inherits from `MessageHandler` and implements the `handle_message` method. Example:
    ```python
    class MyMessageHandler():
        def handle_message(self, message_data: bytes) -> bytes:
            modified_data = do_something(message_data)
            return modified_data
    ```
2. Write a new script to run a proxy with your custom handler. Example:
    ```python
    message_handler = MyMessageHandler()
    proxy = Proxy(message_handler)
    proxy.listen()
    ```

## Code Smells
- Using Python class attributes as type hints for instance attributes
- Using Exceptions as control flow
- A lot of duplicated code between `ServerToClientHeartbeatPayload` and `ClientToServerHeartbeatPayload`
- A lot of duplicated code between the message handlers. Maybe add handlers that can be composed with each other


# References
- [Factorio](https://factorio.com) by Wube Software
- [Factorio Dissector](https://github.com/Hornwitser/factorio_dissector) by Hornwitser