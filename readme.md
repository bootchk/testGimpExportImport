testGimpExportImport
====================


A Python plugin for Gimp that tests export/import features of Gimp.

Mainly of interest to Gimp developers and testers.

Works on Gimp2.99.  Requires GimpFu-v3 (from my other repository.)    
Does NOT work on Gimp.2.10 (its Python 3)

Contains a folder (../in) of examples (test cases) of image formats that Gimp only knows how to import.

The repository is likely to be volatile since Gimp is actively changing (for v3.)
The plugin contains knowledge about what Gimp supports (requirements)
and as the requirements change, the plugin needs update.
The plugin is not supported by gimp.org.  

Quickstart:
-----------

- Install the plugin, say to your local plug-in directory in home/.config/...
- Start Gimp
- Open an image
- Choose Test>File save/load..
- From the dialog select "Run all?"
- Choose "OK"
- Expect to see, printed in the console, any errors and a summary of the testing.
- May take several minutes.

Plugin returns True if the set of test results matches an expected set of test results.

Install (in Gimp 3) means copy the top directory to the plug-ins folder.
The top directory (testGimpExportImport) must have the same name as the main .py file (testGimpExportImport.py)
and the latter must have permission: executable.

Testing, and interpretation of results
--------------------------------------

Automates what you can otherwise do interactively using the Gimp GUI.

- Test all: iterates over the image file formats of Gimp, for each calls the save (export) and load (import) PDB procedures
- Test a single format, save (unless file already exists) and load

Simple sanity test only: for a format, success means no more than:
((save procedure creates a file and returns "success") and (load procedure reads the same file and returns "success"))

The plugin does not compare the in and out images.
You can manually, visually look at the loaded images at the top of the Gimp window.
Very roughly speaking, they should look:
- like the starting image,
- or down moded from the original,
- or a sample image (when only loaders exist.)
With some exceptions: .hgt will look gray until you map gradient
(know issue with .hgt: choose a new gradient, choose color>map>gradient)
(TODO or is it really an issue with negative numbers???)

The plugin understands the current state of Gimp with respect to export/import:
- the set of file formats and their file extensions
- which are save-only, load-only, save-or-load
- which cannot be tested because they don't run non-interactively or other reasons
- which only work for certain image modes
- signature and naming variations
- which formats are known to fail for the base case, and usually omitted from "test all"

The expected set of test results knows the above, and also which tests are known to fail
(for one Gimp version, currently 2.99, for the point-in-time the plugin was authored.)
You can edit the plugin to change the expected test results.
Thus you should expect frequent changes and version of this plugin repository, as Gimp changes.

Advanced Testing
----------------

I usually use a File>New image as the starting image.
You can amp up (open a real image, add layers, etc.) the test image to test harder.
Each test starts with the image open when you invoke the plugin.
Try adding:
- selection
- multiple layers
- layer mask
- layer groups

You can also use this in other stress tests, since it creates many images.
For example, stress test memory or file space.
