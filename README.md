# Temporary File Decrypter
To use execute with file name and time to keep the file

e.g. python open.py dodgy_folder_that_I_dont_want_people_to_see.gpg 10m

You will be prompted by gpg for your password or key or however your folder needs decrypting.

This will create a directory called tmp and inside a compressed folder called dodgy_folder_that_I_dont_want_people_to_see.zip will be inside, after 10 minutes tmp and its content will be deleted (this means that you can expand the archive into tmp and it will also be deleted).

The idea of this was to be used to open encrypted folders that you view multiple times such as bank details lists or photos without the hassle of having to delete the archive and folder manually each time (or incase you forget).
