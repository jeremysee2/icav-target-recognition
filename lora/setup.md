# Setting up the LoRa Gateway (ESP32)

The LoRa gateway used is basically its own computer with the ESP32 module. It would be fully capable to do everything we want... except image processing, which is too heavy for this microcontroller. Instead, we'll be programming it as a simple relay to send data from the UAV back to the ground station.

## Compiling and Uploading Firmware

The code and its libraries are based on the Arduino abstraction library, which allows us to call common functions implemented under the hood by common APIs.

The below gives the full guide for compiling the firmware.

### Install Arduino IDE

To compile the firmware, we first need to install Arduino.

1. Download the Arduino IDE from [this guide](https://learn.sparkfun.com/tutorials/installing-arduino-ide)
2. Add the ESP32 Arduino Core to the `Additional Board Manager URLs` using `https://learn.sparkfun.com/tutorials/installing-arduino-ide`
3. Re-start the IDE

### Install [Arduino-LMIC](arduino-lmic)

This is the template code that we'll be using to setup a LoRaWAN Device with our ESP32 gateway, following this [guide](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/turning-a-gateway-into-a-device).

1. Download the library from the [github](arduino-lmic) or [zip archive](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/6/arduino-lmic-master.zip)
2. Use the Arduino IDE's "Add ZIP Library" to import the zip files into Arduino
3. Configure the example sketch

```cpp
// project-specific definitions
//#define CFG_eu868 1
#define CFG_us915 1
//#define CFG_au921 1
//#define CFG_as923 1
// #define LMIC_COUNTRY_CODE LMIC_COUNTRY_CODE_JP   /* for as923-JP */
//#define CFG_in866 1
#define CFG_sx1276_radio 1

//#define LMIC_PRINTF_TO Serial
#define LMIC_DEBUG_LEVEL 2

//#define DISABLE_INVERT_IQ_ON_RX
```

4. Modify the `lmic/src/hal/hal.cpp` file for the appropriate SPI pins

```cpp
SPI.begin(14, 12, 13, 16);
```

5. Download the example from Sparkfun [here](https://cdn.sparkfun.com/assets/learn_tutorials/8/2/6/ESP-1CH-TTN-Device-ABP-v01.zip)

6. Fill in the following lines with your LoRaWAN details from The Things Network

```cpp
// LoRaWAN NwkSKey, network session key
// This is the default Semtech key, which is used by the early prototype TTN
// network.
static const PROGMEM u1_t NWKSKEY[16] = { PASTE_NWKSKEY_KEY_HERE };

// LoRaWAN AppSKey, application session key
// This is the default Semtech key, which is used by the early prototype TTN
// network.
static const u1_t PROGMEM APPSKEY[16] = { PASTE_APPSKEY_KEY_HERE };

// LoRaWAN end-device address (DevAddr)
static const u4_t DEVADDR = 0xPASTE_DEV_ADDR_HERE;
```

7. Build the Arduino project

### Uploading the firmware

Simply connect your board to your computer and press the "Upload Sketch" button. Restart you board once its done.

## References

* [LoRa Gateway Setup](https://learn.sparkfun.com/tutorials/sparkfun-lora-gateway-1-channel-hookup-guide/turning-a-gateway-into-a-device)