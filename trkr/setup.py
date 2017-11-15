import os
import configparser

def main():
  config = configparser.ConfigParser()
  home = os.path.expanduser("~")

  if not os.path.exists(os.path.join(home, ".trkr")):
      os.makedirs(os.path.join(home, ".trkr"))

  config_path = os.path.join(home, ".trkr/config.ini")

  config["default"] = {
    "email": input("Email: ")
  }

  print("\nTrello Setup\n")

  config["trello"] = {
    "user_id": input("Client ID: "),
    "board_id": input("Board ID: "),
    "api_key": input("API Key: "),
    "api_secret": input("API Secret: "),
    "token": input("Token: ")
  }

  print("\nGoogle Sheets Setup\n")

  config["sheets"] = {
    "url": input("Document URL: "),
    "wks_name": input("Worksheet Name: ")
  }

  print("Generate/ask for a keyfile and move it to ~/.trkr/keyfile.json")
  input("Press ENTER when completed")

  print("\nTIPS\n")
  print("echo \"alias trkr='python3 ~/.../trkr.py'\" >> ~/.zshrc")

  with open(config_path, "w+") as configfile:
    config.write(configfile)
