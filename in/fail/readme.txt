These are files that fail to read.
You can copy them into the "in" directory after renaming them to sample.<foo>

.pspimage  is Paintshop 8 format, not supported by Gimp.
circa 2020 I can't locate a Paintshop 6 .psp file

oratest.ora should be openraster format
It exists to test the loader when the saver fails.
Now, both the loader and the saver fail.
Saver fails with segfault, probably in PyGObject
Loader fails at line 269 img.set_filename which should be img.set_file() ???
