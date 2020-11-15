#!/usr/bin/env python3
# ezPastebin
# 2020 - Himawari466
# https://mit-license.org/
#
# Get developer API key here https://pastebin.com/doc_api/

from tqdm import tqdm
import sys, getopt, time, requests, urllib

def ezPastebin(argv):
  apikey = ""
  inputfile = ""
  cfile = ""
  rawonly = False
  usage = "ezPastebin\n2020 - Himawari466\nhttps://mit-license.org/\n\nusage:\nezPastebin.py -k <api_key> -f <input_file>"
  try:
    opts, args = getopt.getopt(argv, "hk:f:", ["help", "key=", "file=", "raw"])
  except getopt.GetoptError:
    sys.exit(usage)
  if not opts:
    sys.exit(usage)
  for opt, arg in opts:
    if opt in ["-h", "--help"]:
      sys.exit(usage)
    elif opt in ["-k", "--key"]:
      apikey = arg
    elif opt in ["-f", "--file"]:
      inputfile = arg
    elif opt in ["--raw"]:
      rawonly = True
    else:
      sys.exit(usage)

  pbar = tqdm(range(100), desc = "Loading...", bar_format = "{desc}{percentage:.0f}%|{bar:10}|")
  for i in pbar:
    time.sleep(.05)
    if i == 14:
      pbar.set_description("Checking API")
      if apikey == "":
        sys.exit("Missing API key")
    if i == 39:
      pbar.set_description("Checking file")
      if inputfile == "":
        sys.exit("Missing file")
      else:
        try:
          file = open(inputfile, "r")
          cfile = file.read()
          file.close()
        except IOError:
          sys.exit("Failed to read file...")
    if i == 68:
      pbar.set_description("Requesting API")
      pastebinapiurl = "https://pastebin.com/api/api_post.php"
      params = {'api_dev_key': apikey, 'api_option': 'paste', 'api_paste_code': cfile, 'api_paste_private': '0', 'api_paste_expire_date': 'N'}
      posts = requests.post(pastebinapiurl, data = params)
    if i == 90:
      pbar.set_description("Checking result")
      if not posts.text[:4] == "http":
        sys.exit(f"Error requesting API\n{posts.text}")
    if i == 99:
      pbar.set_description("Result API")
  if rawonly == True:
    print(f"https://pastebin.com/raw/{posts.text.split('/')[-1]}")
  else:
    print(f"Pastebin URL: {posts.text}\n\nhttps://pastebin.com/raw/{posts.text.split('/')[-1]}")

if __name__ == "__main__":
  ezPastebin(sys.argv[1:])
