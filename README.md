# Ha_shopping_list_from_qr
 
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/InzynierDomu/Ha_shopping_list_from_qr?style=flat-square)
<a href="https://discord.gg/KmW6mHdg">![Discord](https://img.shields.io/discord/815929748882587688?logo=discord&logoColor=green&style=flat-square)</a>
![GitHub](https://img.shields.io/github/license/InzynierDomu/Ha_shopping_list_from_qr?style=flat-square)
<a href="https://tipo.live/p/inzynierdomu">![support](https://img.shields.io/badge/support-tipo.live-yellow?style=flat-square)</a>

- [Description](#Description)
- [Scheme](#Scheme)
- [Install](#Install)

## Description
Raspberry scaning QR code and send content via MQTT to Node-Red on Home Assistant. In HA content from message is added to shopping list.

## Scheme
- Raspberry pi zero W 2
- QR scanner

## Install
Script running on Raspberry Pi wiht Raspbian.

TODO:
description about MySQL and NGINX

Script required Python 3 and packages. To install packages use pip.
```sh
pip install --upgrade pip
```
- Install MyQSL connection
```sh
python -m pip install mysql-connector-python
```
- Install paho mqtt
```sh
pip install paho-mqtt
```
