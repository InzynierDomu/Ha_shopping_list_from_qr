# Ha_shopping_list_from_qr
 
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/InzynierDomu/Ha_shopping_list_from_qr?style=flat-square)
<a href="https://discord.gg/KmW6mHdg">![Discord](https://img.shields.io/discord/815929748882587688?logo=discord&logoColor=green&style=flat-square)</a>
![GitHub](https://img.shields.io/github/license/InzynierDomu/Ha_shopping_list_from_qr?style=flat-square)

- [Description](#Description)
- [Scheme](#Scheme)
- [Install](#Install)

## Description
Raspberry scaning QR code and send content via MQTT to Node-Red on Home Assistant. In HA content from message is added to shopping list.

<div align="center">
<h2>Support</h2>

<p>If any of my projects have helped you in your work, studies, or simply made your day better, you can buy me a coffee. <a href="https://buycoffee.to/inzynier-domu" target="_blank"><img src="https://buycoffee.to/img/share-button-primary.png" style="width: 195px; height: 51px" alt="Postaw mi kawę na buycoffee.to"></a></p>
</div>

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
