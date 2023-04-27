# folder_sync

Hi!

This is a Python script to synchronize folders.

Unfortunately, the script only works on Windows so far.

In providing folder paths input, kindly use a backslash ('\\')
instead of a frontslash ('/') as path separator.

Also, it doesn't account for subfolders. That is, in case your
Source or Replica folders contain some folders themselves, 
synchronization will only make sure that the content of the files
is the same in both Source and Replica. It will not organize them further.

Thank you!
