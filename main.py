from pyautogui import *
import pyautogui
import time
import random
import win32api, win32con
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

while True:
    if pyautogui.pixel(592, 267)[0] == 118:
        content = "@everyone"
        pyautogui.screenshot("attack.png", (290, 255, 1233, 108))
        webhook = DiscordWebhook(url="your-webhook", rate_limit_retry=True, username="Exotic's Warning Bot", content=content)
        embed = DiscordEmbed(title="**Under Attack**", description="A member of the faction is currently under attack, Please reinforce or contact the person.")
        with open("attack.png", "rb") as f:
            webhook.add_file(file=f.read(), filename='attack.png')
        embed.set_image(url='attachment://attack.png')
        webhook.add_embed(embed)
        response = webhook.execute()
        time.sleep(60)
    if pyautogui.pixel(592, 434)[0] == 118:
            content = "@everyone"
            pyautogui.screenshot("attack1.png", (290, 394, 1233, 108))
            webhook = DiscordWebhook(url="your-webhook", rate_limit_retry=True, username="Exotic's Warning Bot", content=content)
            embed = DiscordEmbed(title="**Under Attack**", description="A member of the faction is currently under attack, Please reinforce or contact the person.")
            with open("attack1.png", "rb") as f:
                webhook.add_file(file=f.read(), filename='attack1.png')
            embed.set_image(url='attachment://attack1.png')
            webhook.add_embed(embed)
            response = webhook.execute()
            time.sleep(60)

    if pyautogui.pixel(592, 581)[0] == 118:
            content = "@everyone"
            pyautogui.screenshot("attack2.png", (290, 530, 1233, 108))
            webhook = DiscordWebhook(url="your-webhook", rate_limit_retry=True, username="Exotic's Warning Bot", content=content)
            embed = DiscordEmbed(title="**Under Attack**", description="A member of the faction is currently under attack, Please reinforce or contact the person.")
            with open("attack2.png", "rb") as f:
                webhook.add_file(file=f.read(), filename='attack2.png')
            embed.set_image(url='attachment://attack2.png')
            webhook.add_embed(embed)
            response = webhook.execute()
            time.sleep(60)
    if pyautogui.pixel(592, 718)[0] == 118:
            content = "@everyone"
            pyautogui.screenshot("attack3.png", (290, 670, 1233, 108))
            webhook = DiscordWebhook(url="your-webhook", rate_limit_retry=True, username="Exotic's Warning Bot", content=content)
            embed = DiscordEmbed(title="**Under Attack**", description="A member of the faction is currently under attack, Please reinforce or contact the person.")
            with open("attack3.png", "rb") as f:
                webhook.add_file(file=f.read(), filename='attack3.png')
            embed.set_image(url='attachment://attack3.png')
            webhook.add_embed(embed)
            response = webhook.execute()
            time.sleep(60)