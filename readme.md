testGimpExportImport


A Python plugin for Gimp that tests export/import features of Gimp.

Mainly of interest to Gimp developers and testers.

Requires GimpFu.  Python3.  Tested on Gimp2.99.  Might work on Gimp.2.10

Quickstart:
    Install the plugin, say to your local plug-in directory in home/.config/...
    Start Gimp
    Choose Test>File save/load..
    From the dialog select "Run all?"
    Choose "OK"
    Expect to see, printed in the console, any errors and a summary of the testing.
    May take several minutes.

Plugin returns True if the set of test results matches an expected set of test results.

Automates what you can otherwise do interactively using the Gimp GUI.
It iterates over the image file formats of Gimp.
For each file format it calls the save (export) and load (import) PDB procedures for the format.

Simple sanity test only: for a format, success means no more than:
((save procedure creates a file and returns "succss") and (load procedure reads the same file and returns "success"))
Does not compare the in and out images.

The plugin understands the current state of Gimp with respect to export/import:
- the set of file formats and their file extensions
- which are save-only, load-only, save-or-load
- which cannot be tested because they don't run non-interactively or other reasons
- which only work for certain image modes
- signature and naming variations

The expected set of test results knows the above, and also which tests are known to fail
(for one Gimp version, currently 2.99, for the point-in-time the plugin was authored.)
You can edit the plugin to change the expected test results.
Thus you should expect the plugin repository new versions, as Gimp changes.
